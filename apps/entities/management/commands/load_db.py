from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import all data'

    def handle(self, *args, **options):
        print('importing distilleries...')
        management.call_command('import_distilleries')

        print('updating prices...')
        management.call_command('update_abc_prices')
