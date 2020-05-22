from django.core import management
from django.core.management.base import BaseCommand
from apps.entities.models import Distillery


class Command(BaseCommand):

    def handle(self, *args, **options):
        logos = [{
            "name": "Aberfeldy",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/21/18/2016112118_aberfeldy_original.png"
        }, {
            "name": "Aberlour",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_aberlour_original.png"
        }, {
            "name": "Allt-A-Bhainne",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_allt_a_bhainne_original.png"
        }, {
            "name": "Ardbeg Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_ardberg_original.png"
        }, {
            "name": "Ardmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_ardmore_original.png"
        }, {
            "name": "Arran",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_arran_original.png"
        }, {
            "name": "Auchentoshan",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_auchentoshan_original.png"
        }, {
            "name": "Auchroisk",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_auchroisk_original.png"
        }, {
            "name": "Aultmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_aultmore_original.png"
        }, {
            "name": "Balblair",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_balbair_original.png"
        }, {
            "name": "Ballechin",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_ballechin_original.png"
        }, {
            "name": "Balmenach",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_balmenach_original.png"
        }, {
            "name": "Balvenie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_balvenie_original.png"
        }, {
            "name": "Banff",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/8/201611228_banff_original.png"
        }, {
            "name": "Ben Nevis"
        }, {
            "name": "Benriach",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_benriach_original.png"
        }, {
            "name": "Benrinnes"
        }, {
            "name": "Benromach",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/24/7/201611247_14799732357422_original.png"
        }, {
            "name": "Ben Wyvis",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_ben_wyvis_original.png"
        }, {
            "name": "Bladnoch",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_bladnoch_original.png"
        }, {
            "name": "Blair Athol",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_blair_athol_original.png"
        }, {
            "name": "Bowmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_bowmore_original.png"
        }, {
            "name": "Braeval",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_braeval_original.png"
        }, {
            "name": "Brora",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/9/201611229_brora_original.png"
        }, {
            "name": "Bruichladdich Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_bruichladdich_original.png"
        }, {
            "name": "Bunnahabhain",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_bunnahabhain_original.png"
        }, {
            "name": "Caledonian",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/10/2016112210_caledonian_original.png"
        }, {
            "name": "Cambus",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/10/2016112210_cambus_original.png"
        }, {
            "name": "Cameronbridge",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/10/2016112210_cameronbridge_original.png"
        }, {
            "name": "Caol Ila",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_caol_ila_original.png"
        }, {
            "name": "Caperdonich",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_caperdonich_original.png"
        }, {
            "name": "Cardhu",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_cardhu_original.png"
        }, {
            "name": "Carsebridge",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_carsebridge_original.png"
        }, {
            "name": "Clynelish",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_clynelish_original.png"
        }, {
            "name": "Coleburn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_coleburn_original.png"
        }, {
            "name": "Convalmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_convalmore_original.png"
        }, {
            "name": "Cragganmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_cragganmore_original.png"
        }, {
            "name": "Craigellachie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_craigellachie_original.png"
        }, {
            "name": "Dailuaine",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_dailuaine_original.png"
        }, {
            "name": "Dallas Dhu",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_dallas_dhu_original.png"
        }, {
            "name": "Dalwhinnie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_dalwhinnie_original.png"
        }, {
            "name": "Deanston",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_deanston_original.png"
        }, {
            "name": "Dufftown",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_dufftown_original.png"
        }, {
            "name": "Edradour",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_edradour_original.png"
        }, {
            "name": "Fettercairn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/11/2016112211_fettercairn_original.png"
        }, {
            "name": "Girvan",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_girvan_original.png"
        }, {
            "name": "Glen Albyn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_albyn_original.png"
        }, {
            "name": "Glenallachie"
        }, {
            "name": "Glenburgie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenburgie_original.png"
        }, {
            "name": "Glencadam"
        }, {
            "name": "GlenDronach",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_glendronach_original.png"
        }, {
            "name": "Glendullan",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glendullan_original.png"
        }, {
            "name": "Glen Elgin",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_elgin_original.png"
        }, {
            "name": "Glen Esk/Hillside",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_eskhillside_original.png"
        }, {
            "name": "Glenfarclas",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_glenfarclas_original.png"
        }, {
            "name": "Glenfiddich",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2019/10/03/12/2019100312_15701056646176_original.png"
        }, {
            "name": "Glen Flagler",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_flagler_original.png"
        }, {
            "name": "Glen Garioch",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_glen_garioci_original.png"
        }, {
            "name": "Glenglassaugh",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenglassaugh_original.png"
        }, {
            "name": "Glengoyne",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glengoyne_original.png"
        }, {
            "name": "Glen Grant",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_grant_original.png"
        }, {
            "name": "Glen Keith",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_keith_original.png"
        }, {
            "name": "Glenkinchie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/14/2015040114_glen_original.png"
        }, {
            "name": "Glenlochy",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenlochy_original.png"
        }, {
            "name": "Glenlossie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenlossie_original.png"
        }, {
            "name": "Glen Mhor",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_mhor_original.png"
        }, {
            "name": "Glenmorangie Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_glenmorangie_original.png"
        }, {
            "name": "Glen Moray",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_glenmoray_original.png"
        }, {
            "name": "Glen Ord",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_ord_original.png"
        }, {
            "name": "Glenrothes",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenrothes_original.png"
        }, {
            "name": "Glen Scotia",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_scotia_original.png"
        }, {
            "name": "Glen Spey",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/22/12/2016112212_glen_spey_original.png"
        }, {
            "name": "Glentauchers",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glentauchers_original.png"
        }, {
            "name": "Glenturret",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenturret_original.png"
        }, {
            "name": "Glenugie",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenugie_original.png"
        }, {
            "name": "Glenury Royal",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_glenury_royal_original.png"
        }, {
            "name": "Highland Park Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2019/07/29/13/2019072913_15644068089185_original.png"
        }, {
            "name": "Imperial",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_imperial_original.png"
        }, {
            "name": "Invergordon"
        }, {
            "name": "Inverleven",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_inverleven_original.png"
        }, {
            "name": "Jura",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_jura_original.png"
        }, {
            "name": "Kilchoman",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_kilchoman_original.png"
        }, {
            "name": "Kinclaith",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/7/201611237_kinclaith_original.png"
        }, {
            "name": "Knockando",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_kockando_original.png"
        }, {
            "name": "Lagavulin",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2019/10/02/11/2019100211_15700165949151_original.png"
        }, {
            "name": "Laphroaig",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_laphroaig_original.png"
        }, {
            "name": "Ledaig",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/8/201611238_ledaig_original.png"
        }, {
            "name": "Linkwood",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_linkwood_original.png"
        }, {
            "name": "Littlemill",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_littlemill_original.png"
        }, {
            "name": "Loch Lomond",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_loch_lomond_original.png"
        }, {
            "name": "Lochside"
        }, {
            "name": "Longmorn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_longmorn_original.png"
        }, {
            "name": "Macallan",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_macallan_original.png"
        }, {
            "name": "Macduff"
        }, {
            "name": "Mannochmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_mannochmore_original.png"
        }, {
            "name": "Millburn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/10/2016112310_millburn_original.png"
        }, {
            "name": "Miltonduff"
        }, {
            "name": "Mortlach",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/11/2016112311_mortlach_original.png"
        }, {
            "name": "North British",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/11/2016112311_north_british_original.png"
        }, {
            "name": "Oban",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/11/2016112311_oban_original.png"
        }, {
            "name": "Old Pulteney",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_oldpulteney_original.png"
        }, {
            "name": "Park Lane Whisky"
        }, {
            "name": "Pittyvaich",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_pittyvaich_original.png"
        }, {
            "name": "Port Dundas",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_port_dundas_original.png"
        }, {
            "name": "Port Ellen",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_port_ellen_original.png"
        }, {
            "name": "Rosebank",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_rosebank_original.png"
        }, {
            "name": "Royal Brackla",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_royal_brackla_original.png"
        }, {
            "name": "Royal Lochnagar",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/18/2016112318_royal_lochnagar_original.png"
        }, {
            "name": "Samaroli"
        }, {
            "name": "Scapa",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_scapa_original.png"
        }, {
            "name": "SIA"
        }, {
            "name": "Speyburn",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_speyburn_original.png"
        }, {
            "name": "Speyside"
        }, {
            "name": "Springbank",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_springbank_original.png"
        }, {
            "name": "Strathisla",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_strathisla_original.png"
        }, {
            "name": "Strathmill",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_strathmill_original.png"
        }, {
            "name": "Sutcliffe & Son"
        }, {
            "name": "Talisker",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_talisker_original.png"
        }, {
            "name": "Tamdhu",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_tamdhu_original.png"
        }, {
            "name": "Tamnavulin",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_tamnavulin_original.png"
        }, {
            "name": "Teaninich",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_teaninich_original.png"
        }, {
            "name": "The Dalmore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_the_dalmore_original.png"
        }, {
            "name": "The Glenlivet Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_theglenlivet_original.png"
        }, {
            "name": "Tobermory",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_tobermory_original.png"
        }, {
            "name": "Tomatin",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_tomatin_original.png"
        }, {
            "name": "Tomintoul",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/01/10/2015040110_tomintoul_original.png"
        }, {
            "name": "Tormore",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_tormore_original.png"
        }, {
            "name": "Tullibardine",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2015/04/16/9/201504169_tullibardine_original.png"
        }, {
            "name": "Wemyss Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2019/10/14/13/2019101413_wemyss_logotype_original.png"
        }, {
            "name": "Wolfburn Distillery",
            "url": "https://d256619kyxncpv.cloudfront.net/gui/img/2016/11/23/15/2016112315_wolfburn_original.png"
        }]

        for logo in logos:
            if 'url' in logo and logo['url'] != '':
                print(f'updating distillery {logo["name"]}...')
                try:
                    d = Distillery.objects.get(name=logo['name'])
                    d.logo_url = logo['url']
                    d.save()
                except Exception as e:
                    print(e)
            else:
                print(f'skipping distillery {logo["name"]}')
