import pandas as pd

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from distilleries.models import Distillery


class Command(BaseCommand):
    help = 'Import distillery data from Data Science Blog'

    def handle(self, *args, **options):

        # Reset database
        Distillery.objects.all().delete()

        # Start wiki data import

        # Active Malt Distilleries
        Distillery.objects.bulk_create([
            Distillery(name='Aberargie', location='Aberargie', region='Lowland', owner='Perth Distilling Co'),
            Distillery(name='Aberfeldy', location='Aberfeldy', region='Highland', owner='Bacardi'),
            Distillery(name='Aberlour', location='Aberlour', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Abhainn Dearg', location='Uig, Isle of Lewis', region='Island', owner='Independent'),
            Distillery(name='Ailsa Bay', location='Girvan', region='Lowland', owner='William Grant & Sons'),
            Distillery(name='Allt-A-Bhainne', location='Glenrinnes', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Annandale', location='Annan', region='Lowland', owner='Annandale Distillery Company'),
            Distillery(name='Arbikie', location='Inverkeilor', region='Highland', owner='Independent'),
            Distillery(name='Ardbeg', location='Port Ellen', region='Islay', owner='LVMH'),
            Distillery(name='Ardmore', location='Kennethmont', region='Highland', owner='Beam Suntory'),
            Distillery(name='Ardnahoe', location='Port Askaig', region='Islay', owner='Hunter Laing & Co Ltd'),
            Distillery(name='Ardnamurchan', location='Ardnamurchan', region='Highland', owner='Adelphi Whisky'),
            Distillery(name='Arran', location='Lochranza', region='Island', owner='Isle of Arran Distillers Ltd.'),
            Distillery(name='Auchentoshan', location='Dalmuir', region='Lowland', owner='Beam Suntory (Morrison Bowmore)'),
            Distillery(name='Auchroisk', location='Mulben', region='Speyside', owner='Diageo'),
            Distillery(name='Aultmore', location='Banffshire', region='Speyside', owner='Bacardi'),
            Distillery(name='Balblair', location='Edderton', region='Highland', owner='ThaiBev'),
            Distillery(name='Ballindalloch', location='Ballindalloch', region='Speyside', owner='Independent'),
            Distillery(name='Balmenach', location='Cromdale', region='Speyside', owner='ThaiBev'),
            Distillery(name='Balvenie', location='Dufftown', region='Speyside', owner='William Grant & Sons'),
            Distillery(name='Barra', location='Borve', region='Island', owner='Uisge Beatha nan Eilean Ltd'),
            Distillery(name='Ben Nevis', location='Fort William', region='Highland', owner='Nikka Whisky Distilling Co Ltd'),
            Distillery(name='BenRiach', location='Morayshire', region='Speyside', owner='Brown-Forman'),
            Distillery(name='Benrinnes', location='Banffshire', region='Speyside', owner='Diageo'),
            Distillery(name='Benromach', location='Forres', region='Speyside', owner='Gordon & MacPhail'),
            Distillery(name='Bladnoch', location='Wigtown', region='Lowland', owner='David Prior'),
            Distillery(name='Blair Athol', location='Pitlochry', region='Highland', owner='Diageo'),
            Distillery(name='Borders', location='Hawick', region='Lowland', owner='The Three Stills Company'),
            Distillery(name='Bowmore', location='Bowmore', region='Islay', owner='Beam Suntory (Morrison Bowmore)'),
            Distillery(name='Royal Brackla', location='Nairn', region='Highland', owner='Bacardi'),
            Distillery(name='Braeval', location='Ballindalloch', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Bruichladdich', location='Rhinns of Islay', region='Islay', owner='Rémy Cointreau'),
            Distillery(name='Bunnahabhain', location='Port Askaig', region='Islay', owner='Distell (Burn Stewart)'),
            Distillery(name='Caol Ila', location='Port Askaig', region='Islay', owner='Diageo'),
            Distillery(name='Cardhu', location='Knockando', region='Speyside', owner='Diageo'),
            Distillery(name='Clydeside', location='Glasgow', region='Lowland', owner='Morrison Glasgow Distillers'),
            Distillery(name='Clynelish', location='Brora', region='Highland', owner='Diageo'),
            Distillery(name='Cragganmore', location='Ballindalloch', region='Speyside', owner='Diageo'),
            Distillery(name='Craigellachie', location='Craigellachie', region='Speyside', owner='Bacardi'),
            Distillery(name='Daftmill', location='Fife', region='Lowland', owner='Independent'),
            Distillery(name='Dailuaine', location='Aberlour', region='Speyside', owner='Diageo'),
            Distillery(name='Dalmore', location='Alness', region='Highland', owner='Alliance Global Group (Emperador Inc)'),
            Distillery(name='Dalmunach', location='Carron', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Dalwhinnie', location='Dalwhinnie', region='Speyside', owner='Diageo'),
            Distillery(name='Deanston', location='Doune', region='Highland', owner='Distell (Burn Stewart)'),
            Distillery(name='Dornoch', location='Dornoch', region='Highland', owner='Independent'),
            Distillery(name='Dufftown', location='Banffshire', region='Speyside', owner='Diageo'),
            Distillery(name='Eden Mill', location='Fife', region='Lowland', owner='Independent'),
            Distillery(name='Edradour', location='Pitlochry', region='Highland', owner='Signatory Vintage Scotch Whisky Co'),
            Distillery(name='Fettercairn', location='Laurencekirk', region='Highland', owner='Alliance Global Group (Emperador Inc)'),
            Distillery(name='Glasgow', location='Glasgow', region='Lowland', owner='Independent'),
            Distillery(name='Glenallachie', location='Banffshire', region='Speyside', owner='The GlenAllachie Distillers Co Limited'),
            Distillery(name='Glenburgie', location='Morayshire', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Glencadam', location='Angus', region='Highland', owner='Angus Dundee Distiller'),
            Distillery(name='Glendronach', location='Aberdeenshire', region='Highland', owner='Brown-Forman'),
            Distillery(name='Glendullan', location='Banffshire', region='Speyside', owner='Diageo'),
            Distillery(name='Glen Elgin', location='Morayshire', region='Speyside', owner='Diageo'),
            Distillery(name='Glenfarclas', location='Ballindalloch', region='Speyside', owner='J. & G. Grant'),
            Distillery(name='Glenfiddich', location='Dufftown', region='Speyside', owner='William Grant & Sons'),
            Distillery(name='Glen Garioch', location='Oldmeldrum', region='Highland', owner='Beam Suntory (Morrison Bowmore)'),
            Distillery(name='Glenglassaugh', location='Portsoy', region='Highland', owner='Brown-Forman'),
            Distillery(name='Glengoyne', location='Dumgoyne', region='Highland', owner='Ian Macleod Distillers'),
            Distillery(name='Glen Grant', location='Rothes', region='Speyside', owner='Campari'),
            Distillery(name='Glengyle', location='Campbeltown', region='Campbeltown', owner='Mitchell\'s Glengyle Ltd'),
            Distillery(name='Glen Keith', location='Keith', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Glenkinchie', location='Pencaitland', region='Lowland', owner='Diageo'),
            Distillery(name='Glenlivet', location='Ballindalloch', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Glenlossie', location='Elgin', region='Speyside', owner='Diageo'),
            Distillery(name='Glenmorangie', location='Tain', region='Highland', owner='LVMH'),
            Distillery(name='Glen Moray', location='Elgin', region='Speyside', owner='La Martiniquaise'),
            Distillery(name='Glen Ord', location='Muir of Ord', region='Highland', owner='Diageo'),
            Distillery(name='Glenrothes', location='Rothes', region='Speyside', owner='Edrington'),
            Distillery(name='Glen Scotia', location='Campbeltown', region='Campbeltown', owner='Loch Lomond Group'),
            Distillery(name='Glen Spey', location='Rothes', region='Speyside', owner='Diageo'),
            Distillery(name='Glentauchers', location='Mulben', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Glenturret', location='Crieff', region='Highland', owner='Highland Distillers'),
            Distillery(name='GlenWyvis', location='Dingwall', region='Highland', owner='Independent (community ownership)'),
            Distillery(name='Harris', location='Tarbert', region='Island', owner='Independent'),
            Distillery(name='Highland Park', location='Kirkwall', region='Island', owner='Edrington'),
            Distillery(name='Inchdairnie', location='Glenrothes', region='Lowland', owner='Independent'),
            Distillery(name='Inchgower', location='Buckie', region='Speyside', owner='Diageo'),
            Distillery(name='Jura', location='Craighouse, Jura', region='Island', owner='Alliance Global Group (Whyte & Mackay)'),
            Distillery(name='Kilchoman', location='Kilchoman', region='Islay', owner='Independent'),
            Distillery(name='Kingsbarns', location='Kingsbarns', region='Lowland', owner='Wemyss Malts'),
            Distillery(name='Kininvie', location='Dufftown', region='Speyside', owner='William Grant & Sons'),
            Distillery(name='Knockando', location='Knockando', region='Speyside', owner='Diageo'),
            Distillery(name='Knockdhu', location='Knock', region='Speyside', owner='ThaiBev'),
            Distillery(name='Lagg', location='Lagg', region='Island', owner='Isle of Arran Distillers Ltd.'),
            Distillery(name='Lagavulin', location='Port Ellen', region='Islay', owner='Diageo'),
            Distillery(name='Laphroaig', location='Port Ellen', region='Islay', owner='Beam Suntory'),
            Distillery(name='Leven', location='Leven', region='Lowland', owner='Diageo'),
            Distillery(name='Lindores Abbey', location='Newburgh', region='Lowland', owner='Independent'),
            Distillery(name='Linkwood', location='Elgin', region='Speyside', owner='Diageo'),
            Distillery(name='Loch Lomond', location='Alexandria', region='Highland', owner='Loch Lomond Group'),
            Distillery(name='Royal Lochnagar', location='Ballater', region='Highland', owner='Diageo'),
            Distillery(name='LoneWolf', location='Ellon', region='Highland', owner='Independent'),
            Distillery(name='Longmorn', location='Elgin', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Macallan', location='Craigellachie', region='Speyside', owner='Edrington'),
            Distillery(name='Macduff', location='Banff', region='Highland', owner='Bacardi'),
            Distillery(name='Mannochmore', location='Elgin', region='Speyside', owner='Diageo'),
            Distillery(name='Miltonduff', location='Elgin', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Mortlach', location='Dufftown', region='Speyside', owner='Diageo'),
            Distillery(name='Nc’nean', location='Lochlaline', region='Highland', owner='Drimnin Distillery Co'),
            Distillery(name='Oban', location='Oban', region='Highland', owner='Diageo'),
            Distillery(name='Pulteney', location='Wick', region='Highland', owner='ThaiBev'),
            Distillery(name='Raasay', location='Isle of Raasay', region='Island', owner='R&B Distillers'),
            Distillery(name='Roseisle', location='Roseisle', region='Speyside', owner='Diageo'),
            Distillery(name='Scapa', location='Kirkwall', region='Island', owner='Pernod Ricard'),
            Distillery(name='Speyburn', location='Rothes', region='Speyside', owner='ThaiBev'),
            Distillery(name='Speyside', location='Drumguish', region='Speyside', owner='Independent'),
            Distillery(name='Springbank', location='Campbeltown', region='Campbeltown', owner='J & A Mitchell & Co Ltd.'),
            Distillery(name='Strathearn', location='Methven', region='Highland', owner='Douglas Laing & Co.'),
            Distillery(name='Strathisla', location='Keith', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Strathmill', location='Keith', region='Speyside', owner='Diageo'),
            Distillery(name='Talisker', location='Carbost, Isle of Skye', region='Island', owner='Diageo'),
            Distillery(name='Tamdhu', location='Knockando', region='Speyside', owner='Ian Macleod Distillers'),
            Distillery(name='Tamnavulin', location='Tomnavoulin', region='Speyside', owner='Alliance Global Group (Whyte & Mackay)'),
            Distillery(name='Teaninich', location='Alness', region='Highland', owner='Diageo'),
            Distillery(name='Tobermory', location='Tobermory, Isle of Mull', region='Island', owner='Distell (Burn Stewart)'),
            Distillery(name='Tomatin', location='Tomatin', region='Highland', owner='Takara Shuzo Co'),
            Distillery(name='Tomintoul', location='Ballindalloch', region='Speyside', owner='Angus Dundee Distiller'),
            Distillery(name='Torabhaig', location='Teangue, Isle of Skye', region='Island', owner='Mossburn Distillers'),
            Distillery(name='Tormore', location='Grantown-on-Spey', region='Speyside', owner='Pernod Ricard'),
            Distillery(name='Tullibardine', location='Blackford', region='Highland', owner='Picard Vins & Spiritueux'),
            Distillery(name='Twin River', location='Banchory', region='Highland', owner='Deeside Brewery & Distillery Ltd'),
            Distillery(name='Wolfburn', location='Thurso', region='Highland', owner='Independent')
            ])

        # Active Grain Distilleries
        Distillery.objects.bulk_create([
            Distillery(name='Cameronbridge', location='Fife', owner='Diageo'),
            Distillery(name='Girvan', location='Girvan', owner='William Grant & Sons'),
            Distillery(name='Invergordon', location='Easter Ross', owner='Emperador Inc'),
            # Distillery(name='Loch Lomond', location='Alexandria', owner='Independent'),
            Distillery(name='North British', location='Edinburgh', owner='Diageo/Edrington'),
            Distillery(name='Starlaw', location='Livingston', owner='La Martiniquaise'),
            Distillery(name='Strathclyde', location='Glasgow', owner='Pernod Ricard')
        ])

        # Inactive Malt Distilleries
        Distillery.objects.bulk_create([
            Distillery(name='Auchinblae', location='Auchenblae', region='Highland', year_closed='1930'),
            Distillery(name='Auchtermuchty', location='Auchtermuchty', region='Lowland', year_closed='1926'),
            Distillery(name='Auchtertool', location='Auchtertool', region='Lowland', year_closed='1927', year_demolished='1985'),
            Distillery(name='Banff', location='Banff', region='Speyside', year_closed='1983', year_demolished='1991'),
            Distillery(name='Ben Wyvis', location='Dingwall', region='Highland', year_closed='1977'),
            Distillery(name='Brora', location='Brora', region='Highland', year_closed='1983'),
            Distillery(name='Caperdonich', location='Rothes', region='Speyside', year_closed='2002'),
            Distillery(name='Coleburn', location='Near Elgin', region='Speyside', year_closed='1992'),
            Distillery(name='Convalmore', location='Dufftown', region='Speyside', year_closed='1985'),
            Distillery(name='Dallas Dhu', location='Near Forres', region='Speyside', year_closed='1983'),
            Distillery(name='Finnieston', location='Glasgow', region='Lowland', year_closed='1827'),
            Distillery(name='Glen Albyn', location='Inverness', region='Highland', year_closed='1983', year_demolished='1988'),
            Distillery(name='Glencraig', location='Near Forres', region='Speyside', year_closed='1981'),
            Distillery(name='Glenesk/Hillside', location='Montrose', region='Highland', year_closed='1985'),
            Distillery(name='Glenflagler', location='Airdrie', region='Lowland', year_closed='1985'),
            Distillery(name='Glenfyne/Glendarroch/Glengilp', location='Ardrishaig', region='Highland', year_closed='1937'),
            Distillery(name='Glenlochy', location='Fort William', region='Highland', year_closed='1983'),
            Distillery(name='Glen Mhor', location='Inverness', region='Highland', year_closed='1983'),
            Distillery(name='Glenskiach', location='Evanton', region='Highland', year_closed='1926'),
            Distillery(name='Glenugie', location='Peterhead', region='Highland', year_closed='1983'),
            Distillery(name='Glenury', location='Stonehaven', region='Highland', year_closed='1985'),
            Distillery(name='Hazelburn', location='Campbeltown', region='Campbeltown', year_closed='1925'),
            Distillery(name='Imperial', location='Carron', region='Speyside', year_closed='1998', year_demolished='2013'),
            Distillery(name='Inverleven', location='Dumbarton', region='Lowland', year_closed='1991'),
            Distillery(name='Killyloch', location='Airdrie', region='Lowland', year_closed='1985'),
            Distillery(name='Kinclaith', location='Glasgow', region='Lowland', year_closed='1976'),
            Distillery(name='Ladyburn', location='Girvan', region='Lowland', year_closed='1975', year_demolished='1976'),
            Distillery(name='Littlemill', location='Bowling', region='Lowland', year_closed='1992'),
            Distillery(name='Lochindaal', location='Port Charlotte', region='Islay', year_closed='1929'),
            Distillery(name='Lochside', location='Montrose', region='Highland', year_closed='1992'),
            Distillery(name='Millburn', location='Inverness', region='Highland', year_closed='1985'),
            Distillery(name='North Port', location='Brechin', region='Highland', year_closed='1983'),
            Distillery(name='Parkmore', location='Dufftown', region='Speyside', year_closed='1931'),
            Distillery(name='Pittyvaich', location='Dufftown', region='Speyside', year_closed='1993'),
            Distillery(name='Port Charlotte', location='Port Charlotte', region='Islay', year_closed='1929'),
            Distillery(name='Port Ellen', location='Port Ellen', region='Islay', year_closed='1983'),
            Distillery(name='Rosebank', location='Falkirk', region='Lowland', year_closed='1993'),
            Distillery(name='St. Magdalene', location='Linlithgow', region='Lowland', year_closed='1983'),
            Distillery(name='Towiemore', location='Near Keith', region='Speyside', year_closed='1930')
        ])

        # Inactive Grain Distilleries
        Distillery.objects.bulk_create([
            Distillery(name='Caledonian', location='Haymarket', owner='Diageo', year_closed='1988'),
            Distillery(name='Cambus', location='Tullibody', owner='Diageo', year_closed='1993'),
            Distillery(name='Carsebridge', location='Alloa', owner='Scottish Grain Distillers', year_closed='1983'),
            Distillery(name='Dumbarton', location='West Dunbartonshire', owner='Pernod Ricard', year_closed='2002'),
            Distillery(name='Garnheath', location='Airdrie', owner='Inver House Distillers', year_closed='1986'),
            Distillery(name='Port Dundas', location='Glasgow', owner='Diageo', year_closed='2010'),
            Distillery(name='Strathmore', location='Tullibody', owner='North of Scotland', year_closed='1980')
        ])

        # Import CSV from Data Science Blog
        df = pd.read_csv(settings.DISTILLERY_CSV)
        for index, row in df.iterrows():
            coordinates = {'longitude': row['lat'], 'latitude': row['long']}
            d, created = Distillery.objects.update_or_create(name=row['Distillery'], defaults=coordinates)

        print(f'{Distillery.objects.count()} distilleries imported')
