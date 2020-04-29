import os
import requests
import sqlite3

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from app.models import Distillery, Scotch, ABCInfo


API_BASE_URL = 'https://www.abc.virginia.gov/coveo/rest/v2'

class Command(BaseCommand):
    help = 'Scrape Virginia ABC website for scotch prices'

    def query(self, distillery):
        q = distillery.name.lower()
        results = []
        # params = '&'.join([f'{k}={v}' for k, v in params.items()])
        params = '&'.join([f'q={q}', f'numberOfResults=1000'])
        url = f'{API_BASE_URL}?{params}'
        r = requests.get(url)
        j = r.json()
        if len(j['results']) > 0:
            # Save to file
            with open(os.path.join(settings.BASE_DIR, 'data', f'{q}.json'), 'w') as f:
                f.write(r.text)

            for result in j['results']:
                attrs = {}

                try:
                    attrs = {
                        'unique_id': result['uniqueId'],
                        'product_uri': result['printableUri']
                    }
                except KeyError as e:
                    print('\tunique id / product uri not in response')

                raw = result['raw']

                # Check multiple fields for name
                for lookup in ['productz32xlabelz32xname', 'fpagez32xheading61692', 'fpagez32xtitle61692', 'fproductz32xlabelz32xname61692', 'fnavigationz32xtitle61692']:
                    if lookup in raw:
                        attrs.update({'name': raw[lookup]})
                        break

                # Get or create Scotch
                if 'name' in attrs:
                    scotch, scotch_created = Scotch.objects.get_or_create(
                        name=attrs['name'],
                        distillery=distillery)
                    attrs.update({'scotch': scotch})

                # Hierarchy info
                try:
                    attrs.update({'hierarchy_division': raw['hierarchyz32xdivision']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_imported': raw['hierarchyz32ximported']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_fact':     raw['hierarchyz32xfact']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_class':    raw['hierarchyz32xclass']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_flavored': raw['hierarchyz32xflavored']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_vap':      raw['hierarchyz32xvap']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_category': raw['hierarchyz32xcategory']})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_type':     raw['hierarchyz32xtype'][0]})
                except KeyError as e:
                    pass
                try:
                    attrs.update({'hierarchy_detail':   raw['hierarchyz32xdetail'][0]})
                except KeyError as e:
                    pass

                if 'z95xproductz32xsiz122xe' in raw:
                    for i in range(len(raw['z95xproductz32xsiz122xe'])):
                        try:
                            attrs.update({'sku': raw['z95xproductz32xskuz32xids'][i]})
                        except Exception as e:
                            # print(f'\tno sku found for {url}')
                            pass
                        try:
                            attrs.update({
                                'size': raw['z95xproductz32xsiz122xe'][i],
                                'price': raw['z95xproductz32xprice'][i]
                            })
                        except Exception as e:
                            pass

                        # Save ABCInfo
                        try:
                            abc_obj, abc_created = ABCInfo.objects.update_or_create(**attrs)
                        except (sqlite3.IntegrityError, IntegrityError):
                            pass

    def handle(self, *args, **options):
        # Get all distilleries in database
        distilleries = Distillery.objects.all()
        for distillery in distilleries:
            print(f'Querying data for {distillery.name}...')
            self.query(distillery)
        print('done')
