import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand

from distilleries.models import Distillery


class Command(BaseCommand):
    help = 'Import distillery data from Data Science Blog'

    def handle(self, *args, **options):
        data = pd.read_csv(settings.DISTILLERY_CSV)
        # TODO add these columns to Distillery model and create/update Distilleries based on CSV
        print(list(data))
