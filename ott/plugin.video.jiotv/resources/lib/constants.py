
import xbmcaddon
from xbmcvfs import translatePath

ADD = xbmcaddon.Addon()
AIN = ADD.getAddonInfo
AID = AIN("id")
ANM = AIN("name")
PRO = AIN("profile")
GSET = ADD.getSetting
SSET = ADD.setSetting
runPg = "RunPlugin(plugin://" + AID + "/resources/lib/main/"
filterBy = ["Languages", "Categories", "Broadcasters"]
LMAP = {1: "Hindi", 2: "Marathi", 3: "Punjabi", 4: "Urdu", 5: "Bengali", 6: "English", 7: "Malayalam", 8: "Tamil", 9: "Gujarati", 10: "Odia", 11: "Telugu", 12: "Bhojpuri", 13: "Kannada", 14: "Assamese", 15: "Nepali", 16: "French"}
CMAP = {5: "Entertainment", 6: "Movies", 7: "Kids", 8: "Sports", 9: "Lifestyle", 10: "Infotainment", 12: "News", 13: "Music", 15: "Devotional", 16: "Business News", 17: "Educational", 18: "Shopping"}
BMAP = {1: "General", 3: "Viacom18 Media", 4: "Times Network", 5: "Zee Entertainment", 6: "Sony Pictures Network", 7: "Warner Bros", 8: "TV Today Network", 9: "Sun Network", 10: "Discovery Network", 11: "NDTV Network", 12: "IN10 Media Network", 13: "Turmeric Vision", 14: "9X Media", 15: "ABP Group", 16: "B4U Network", 18: "Doordarshan", 20: "Jio Sports Events", 22: "Raj Network", 23: "Republic Network", 24: "Sahara Network", 25: "TravelFoodxp Network", 26: "Fyi Media Group", 27: "Jio Cinema", 28: "Shemaroo Jio Live", 30: "BAG Network", 32: "ETV Network", 33: "Enterr10 Network", 34: "Education Network", 41: "PTC Network", 44: "TV9 Network", 45: "Tseries", 46: "Merchant Records", 47: "Desi Punjabi Bhojpuri", 48: "Saregama", 49: "KC Global Media", 50: "Wild Earth", 51: "Zee News Media", 52: "Seven Colors Broadcasting", 53: "QYOU Media", 54: "PowerKids Entertainment", 55: "Asianet News Network", 56: "Brit Asia TV Network", 57: "ITV News Network", 58: "Hare Krsna Content Broadcast", 59: "MH One TV Network", 60: "News Nation Network", 61: "SAB Network", 62: "Kalaignar TV Pvt Ltd", 63: "Lex Sportel Vision", 64: "Sidharth TV Network", 65: "Insight Media City", 66: "Fashion India", 67: "Brave TV", 68: "Narikaa Digital", 69: "Red Bull Media", 70: "RS Bharat", 71: "NH Studioz", 72: "Star Entertainment", 73: "INH News Janta TV"}
MAPS = [LMAP, CMAP, BMAP]
CHANNELS_SRC = GSET("channelssource") if bool(GSET("channelssource")) else SSET("channelssource", "https://jiotvapi.cdn.jio.com/apis/v1.4/getMobileChannelList/get/?os=android&devicetype=phone&usertype=tvYR7NSNn7rymo3F")
GET_CHANNEL_URL = GSET("channelurl") if bool(GSET("channelurl")) else SSET("channelurl", "https://tv.media.jio.com/apis/v2.0/getchannelurl/getchannelurl?langId=6")
CATCHUP_SRC = GSET("catchupsource") if bool(GSET("catchupsource")) else SSET("catchupsource", "https://jiotvapi.cdn.jio.com/apis/v1.3/getepg/get?offset={0}&channel_id={1}&langId=6")
FEATURED_SRC = GSET("featuredsource") if bool(GSET("featuredsource")) else SSET("featuredsource", "https://tv.media.jio.com/apis/v1.6/getdata/featurednew?start=0&limit=30&langId=6")
M3U_PATH = GSET("m3ufolder") if bool(GSET("m3ufolder")) else SSET("m3ufolder", translatePath(PRO))
M3U_FILE = (GSET("m3ufile") if bool(GSET("m3ufile")) else SSET("m3ufile", "playlist")) + ".m3u"
EPG_SRC = GSET("epgsource") if bool(GSET("epgsource")) else SSET("epgsource", "https://tobalan.github.io/epg.xml.gz")
M3U_SRC = str(M3U_PATH) + str(M3U_FILE)
IMG = "https://jiotvimages.cdn.jio.com/dare_images/images/%s/-/" % GSET("logosize")
yuppImg = "https://d229kpbsb5jevy.cloudfront.net/tv/150/150/bnw/"
epiconimg = "https://www.epicon.in/img/"
master = "/master.m3u8"
daiurl = "https://dai.google.com/linear/hls/event/%s" + master
epicon = "https://epiconvh.s.llnwi.net/%s" + master
yuppfta = "https://yuppftalive.akamaized.net/080823/%s/playlist.m3u8"
sofast = "https://streams2.sofast.tv/ptnr-yupptv/title-%s-ENG_YuppTV/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/%s/manifest.m3u8"
daikeys = {
        154: "CrTivkDESWqwvUj3zFEYEA", # Sony SAB
        155: "Sle_TR8rQIuZHWzshEXYjQ", # Sony TEN 5 HD
        162: "wG75n5U8RrOKiFzaWObXbA", # Sony TEN 1 HD
        289: "Oc1isQAET3WaNPoABfScmg", # Sony MAX SD
        291: "dBdwOiGaQvy0TA1zOsjV6w", # SET HD
        471: "CrTivkDESWqwvUj3zFEYEA", # Sony SAB HD
        474: "dhPrGRwDRvuMQtmlzppzQQ", # Sony PAL
        476: "UcjHNJmCQ1WRlGKlZm73QA", # Sony MAX HD
        483: "MdQ5Zy-PSraOccXu8jflCg", # Sony MAX2
        514: "6WhVNGKTRXyu588zZv1Lkg", # Sony TEN 1
        523: "LK-ik89MQIi_pWBbg74KNQ", # Sony TEN 2
        524: "BCOFZq1JQjq12fmaO6lAAA", # Sony TEN 3
        525: "r-eLp41YTHWTagvQSXFtAQ", # Sony TEN 5
        697: "j-YEIDwORxubtP_967VcZg", # Sony AATH
        762: "x7rXWd2ERZ2tvyQWPmO1HA", # Sony PIX HD
        823: "x_dFvsORSZWERbxrltEk0g", # Nazaara TV
        852: "6bVWYIKGS0CIa-cOpZZJPQ", # Sony BBC Earth HD English
        853: "le1PgkehT9-fQBK6Q5BCng", # Vikatan TV
        854: "xlbhVAjKQZKnvXGJZHqWnA", # Arré HD
        872: "GPY7RqOrSkmKJ8z1GbVNhg", # Sony YAY Hindi
        873: "GPY7RqOrSkmKJ8z1GbVNhg", # Sony YAY Tamil
        874: "GPY7RqOrSkmKJ8z1GbVNhg", # Sony YAY Telugu
        891: "V9h-iyOxRiGp41ppQScDSQ", # Sony TEN 2 HD
        892: "ltsCG7TBSCSDmyq0rQtvSA", # Sony TEN 3 HD
        1146: "I2phC6tgTDuJngxw9gJgPw", # Sony Marathi SD
        1393: "gX5rCBf6Q7-D5AWY-sovzQ", # Sony WAH
        1396: "dBdwOiGaQvy0TA1zOsjV6w", # SET SD
        1772: "tNzcW2ZhTVaViggo5ocI-A", # Sony TEN 4 HD Tamil
        1773: "tNzcW2ZhTVaViggo5ocI-A", # Sony TEN 4 HD Telugu
        1774: "smYybI_JToWaHzwoxSE9qA", # Sony TEN 4 Tamil
        1775: "smYybI_JToWaHzwoxSE9qA", # Sony TEN 4 Telugu
        2066: "8mB7cHFVQR6EG_MLVVuEow", # Gusto TV
        2745: "G57X2TbRTUed4WQpILYLXg", # 4K TRAVEL TV
        2755: "3D0r9O5ETyyx7UVC2uKz-Q", # Quietude 4K
        2861: "ltsCG7TBSCSDmyq0rQtvSA", # Sony TEN 3 HD Marathi
        3000: "IoTNl-GQShWKit_KdZNY_A", # NDTV Rajasthan
        3001: "sXGilpLZQeWCygKyNIyQig", # NDTV MP Chhattisgarh
        3002: "BaO9Vo1CQw2OmeLAvWeijg", # Kids TV India
        3003: "vAkYbgo7RFa7SUT_MQGU0Q", # EPIC TV
        3004: "GUVq2x8vQz23L9MmgwZsaQ", # Hare Krsna TV
        3005: "3TCgna8YSFOqHlHXF9PHHw", # Food Food
        3006: "yvQpXDAeRMGU25KTu--V6Q" # Bollywood Prime
    }
extUrls = {
        4000: epicon % "epic",
        4001: epicon % "gubbare", 
        4002: epicon % "ishaara",
        4003: epicon % "nazara",
        4004: epicon % "showbox",
        4005: epicon % "filamchi",
        4019: sofast % ("CARTOON-TV-CLASSICS", "d5543c06-5122-49a7-9662-32187f48aa2c"),
        4020: sofast % ("BABYFIRST", "c8d16110-566c-4e95-a1df-55d175e9e201"),
        4021: sofast % ("KIDDO", "5bcf9d24-04f2-401d-a93f-7af54f29461a"),
        4022: sofast % ("BEANI-KIDS-TV", "ae504cae-b81f-49e6-8b40-71d7c0843589"),
        4023: sofast % ("HD-TRAVEL-TV", "e58c3999-b5e1-4322-8d73-db8ebd8acb32"),
        4024: sofast % ("HERITAGE", "e4523706-f2a8-4b0f-b081-40fe59a46f81"),
        4025: sofast % ("HERITAGE-TOURISM-TV", "cff3309e-ded1-40dd-a6dc-e3a6d0a92d72"),
        4026: sofast % ("ENCORE", "390efe7e-4a1a-4f9f-8266-b4d90ab7121a"),
        4027: yuppfta % "jaimaharashtra",
        4028: yuppfta % "anjantv",
        4029: yuppfta % "pasand"
}
extraChannels = [
{"channel_id": 762, "channel_order": "1050", "channel_name": "Sony Pix HD", "channelCategoryId": 6, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 6, "logoUrl": IMG+"Sony_Pix_HD.png"},
{"channel_id": 852, "channel_order": "1051", "channel_name": "Sony BBC Earth HD", "channelCategoryId": 10, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 6, "logoUrl": IMG+"Sony_BBC_Earth_HD_English.png"},
{"channel_id": 823, "channel_order": "1052", "channel_name": "Nazaara TV", "channelCategoryId": 5, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": "http://www.nazarachannel.com/wp-content/uploads/2023/04/nazara-logo-updated.png"},
{"channel_id": 854, "channel_order": "1053", "channel_name": "Arré (non-Jio)", "channelCategoryId": 5, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": IMG+"Arre.png"},
{"channel_id": 853, "channel_order": "1054", "channel_name": "Vikatan TV", "channelCategoryId": 5, "channelLanguageId": 8, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://fea.assettype.com/vikatan/assets/vikatan-logo-7d10e0f8c3899d298242.png"},
{"channel_id": 2066, "channel_order": "1055", "channel_name": "Gusto TV", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://qqcdnpictest.mxplay.com/pic/3187.DistroTv.in/en/1x1/208x208/test_pic1690453571773.jpg"},
{"channel_id": 2745, "channel_order": "1056", "channel_name": "4K TRAVEL TV", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://qqcdnpictest.mxplay.com/pic/3193.DistroTv.in/en/1x1/208x208/test_pic1690462555214.jpg"},
{"channel_id": 2755, "channel_order": "1057", "channel_name": "Quietude 4K", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://qqcdnpictest.mxplay.com/pic/1685.DistroTv.in/en/1x1/208x208/test_pic1690460899275.jpg"},
{"channel_id": 3000, "channel_order": "1058", "channel_name": "NDTV Rajasthan", "channelCategoryId": 12, "channelLanguageId": 1, "isHD": False, "isCatchupAvailable": False, "broadcasterId": 11, "logoUrl": "https://yt3.googleusercontent.com/T5ltIUteczA2n9OJfjCEAYU1PZ_Mqbr3BkUrcgj7IvvkU5w8w3-wieb_KPCk--ZRNfNmesqXGg=s400"},
{"channel_id": 3001, "channel_order": "1059", "channel_name": "NDTV MP Chhattisgarh", "channelCategoryId": 12, "channelLanguageId": 1, "isHD": False, "isCatchupAvailable": False, "broadcasterId": 11, "logoUrl": "https://yt3.googleusercontent.com/qATXIkOUNcKSPZ4GYYpyDR1AaKmBjLKT2ITlIYtCNGThB9FLs-LuGwsnztgQzJarcNgG0Kgdg3k=s400"},
{"channel_id": 3002, "channel_order": "1060", "channel_name": "Kids TV India", "channelCategoryId": 7, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://qqcdnpictest.mxplay.com/pic/3687.DistroTv.in/en/1x1/208x208/test_pic1690454184552.jpg"},
{"channel_id": 3003, "channel_order": "1061", "channel_name": "Epic TV", "channelCategoryId": 9, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": "https://www.epicchannel.co.in/wp-content/uploads/2022/04/Epic-Logo-Alpha-1-Copy.png"},
{"channel_id": 3004, "channel_order": "1062", "channel_name": "Hare Krsna TV", "channelCategoryId": 15, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 58, "logoUrl": IMG+"Harekrsna.png"},
{"channel_id": 3005, "channel_order": "1063", "channel_name": "Food Food", "channelCategoryId": 9, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 13, "logoUrl": IMG+"Food_Food.png"},
{"channel_id": 3006, "channel_order": "1064", "channel_name": "Bollywood Prime", "channelCategoryId": 6, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": "https://distro.tv/desi-eu/img/Bollywood-Prime-thumbnail.png"},
{"channel_id": 4000, "channel_order": "1065", "channel_name": "Epic", "channelCategoryId": 9, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"epic-tv.png"},
{"channel_id": 4001, "channel_order": "1066", "channel_name": "Gubbare", "channelCategoryId": 7, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"gubbare-logo.png"},
{"channel_id": 4002, "channel_order": "1067", "channel_name": "Ishaara", "channelCategoryId": 5, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"ishara-logo.png"},
{"channel_id": 4003, "channel_order": "1068", "channel_name": "Nazaara", "channelCategoryId": 5, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"nazara-logo.png"},
{"channel_id": 4004, "channel_order": "1069", "channel_name": "Showbox", "channelCategoryId": 13, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"new-show-box-logo.png"},
{"channel_id": 4005, "channel_order": "1070", "channel_name": "Filamchi Bhojpuri", "channelCategoryId": 6, "channelLanguageId": 12, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 12, "logoUrl": epiconimg+"new_filamchi_logo.png"},
{"channel_id": 4020, "channel_order": "1071", "channel_name": "Baby First", "channelCategoryId": 7, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"BabyFirstTV_black.png"},
{"channel_id": 4021, "channel_order": "1072", "channel_name": "Kiddo", "channelCategoryId": 7, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"Kiddo512X512_blackz1.png"},
{"channel_id": 4022, "channel_order": "1073", "channel_name": "Beani Kids TV", "channelCategoryId": 7, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"Beani-Kids-TV_black.png"},
{"channel_id": 4023, "channel_order": "1074", "channel_name": "HD Travel TV", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"HD-Travel_TV_black.png"},
{"channel_id": 4024, "channel_order": "1075", "channel_name": "Heritage", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"Heritage_TV_black.png"},
{"channel_id": 4025, "channel_order": "1076", "channel_name": "Heritage Tourism TV", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"heritage_tourism_512X512_balck.png"},
{"channel_id": 4026, "channel_order": "1077", "channel_name": "Encore", "channelCategoryId": 9, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"512X512Encore.png"},
{"channel_id": 4027, "channel_order": "1078", "channel_name": "Jai Maharashtra News (non-Jio)", "channelCategoryId": 12, "channelLanguageId": 2, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"Jai-Maharashtra_TV_black.png"},
{"channel_id": 4028, "channel_order": "1079", "channel_name": "Anjan TV", "channelCategoryId": 13, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"Anjan-TV_black.png"},
{"channel_id": 4029, "channel_order": "1080", "channel_name": "Pasand", "channelCategoryId": 13, "channelLanguageId": 1, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"PASAND_TV_black.png"},
{"channel_id": 4019, "channel_order": "1081", "channel_name": "Cartoon TV Classics", "channelCategoryId": 7, "channelLanguageId": 6, "isHD": True, "isCatchupAvailable": False, "broadcasterId": 1, "logoUrl": yuppImg+"cartoon_classics_512X512_balck.png"}
]
