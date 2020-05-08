import json
import os
import requests
import sqlite3

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from app.models import Distillery, Scotch, ABCInfo


API_BASE_URL = 'https://www.abc.virginia.gov/coveo/rest/v2'
USE_LOCAL = True

class Command(BaseCommand):
    help = 'Scrape Virginia ABC website for scotch prices'

    def query(self, distillery):
        q = distillery.name.replace('/', ' ').lower()
        data = {'results': []}

        try:
            if USE_LOCAL:
                with open(os.path.join(settings.BASE_DIR, 'data', f'{q}.json'), 'r') as f:
                    data = json.load(f)
            else:
                raise FileNotFoundError
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # params = '&'.join([f'{k}={v}' for k, v in params.items()])
            params = '&'.join([f'q={q}', f'numberOfResults=1000'])
            url = f'{API_BASE_URL}?{params}'
            r = requests.get(url)
            data = r.json()
            # Save to file
            with open(os.path.join(settings.BASE_DIR, 'data', f'{q}.json'), 'w') as f:
                f.write(r.text)

        for result in data['results']:
            attrs = {
                'unique_id': result['uniqueId'],
                'product_uri': result['printableUri']
            }
            raw = result['raw']

            # Check multiple fields for name
            # for lookup in ['productz32xlabelz32xname', 'fpagez32xheading61692', 'fpagez32xtitle61692', 'fproductz32xlabelz32xname61692', 'fnavigationz32xtitle61692']:
            #     if lookup in raw:
            #         attrs.update({'name': raw[lookup]})
            attrs.update({'name': raw['title'].replace('-', ' ')})

            # Description
            if 'description' in raw:
                attrs.update({'description': raw['description']})

            # Hierarchy info
            if 'hierarchyz32xdivision' in raw:
                attrs.update({'hierarchy_division': raw['hierarchyz32xdivision']})
            if 'hierarchyz32ximported' in raw:
                attrs.update({'hierarchy_imported': raw['hierarchyz32ximported']})
            if 'hierarchyz32xfact' in raw:
                attrs.update({'hierarchy_fact': raw['hierarchyz32xfact']})
            if 'hierarchyz32xclass' in raw:
                attrs.update({'hierarchy_class': raw['hierarchyz32xclass']})
            if 'hierarchyz32xflavored' in raw:
                attrs.update({'hierarchy_flavored': raw['hierarchyz32xflavored']})
            if 'hierarchyz32xvap' in raw:
                attrs.update({'hierarchy_vap': raw['hierarchyz32xvap']})
            if 'hierarchyz32xcategory' in raw:
                attrs.update({'hierarchy_category': raw['hierarchyz32xcategory']})
            if 'hierarchyz32xtype' in raw:
                attrs.update({'hierarchy_type': raw['hierarchyz32xtype'][0]})
            if 'hierarchyz32xdetail' in raw:
                attrs.update({'hierarchy_detail': raw['hierarchyz32xdetail'][0]})

            # Image URL
            if 'z95ximagez32xurl' in raw:
                attrs.update({'image_url': f'https://www.abc.virginia.gov/{raw["z95ximagez32xurl"]}'})

            if 'z95xproductz32xsiz122xe' in raw:
                for i in range(len(raw['z95xproductz32xsiz122xe'])):
                    try:
                        attrs.update({
                            'sku': raw['z95xproductz32xskuz32xids'][i],
                            'size': raw['z95xproductz32xsiz122xe'][i],
                            'price': raw['z95xproductz32xprice'][i]
                        })
                    except Exception as e:
                        pass

                    # Get or create Scotch if first term of name matches first term of query
                    if 'sku' in attrs:
                        if attrs['name'].split()[0].lower() == q.split()[0].lower() and 'size' in attrs and attrs['size'] == '750 ml':
                            try:
                                # Get or create Scotch (unique name)
                                scotch, scotch_created = Scotch.objects.get_or_create(
                                    name=attrs['name'],
                                    distillery=distillery)
                                attrs.update({'scotch': scotch})
                            except:
                                # FIXME need a more targeted query to make sure this scotch result actually belongs to the queried distillery
                                # possibly fixed: checking sku and comparing name with distillery (q)
                                pass

                        try:
                            # Update or create
                            abc_obj, abc_created = ABCInfo.objects.update_or_create(**attrs)
                        except (sqlite3.IntegrityError, IntegrityError):
                            pass

    def handle(self, *args, **options):
        # Get all distilleries in database
        distilleries = Distillery.objects.all()
        for distillery in distilleries:
            print(f'Querying data for {distillery.name.replace("/", " ")}...')
            self.query(distillery)
        print('done')
