
from __future__ import unicode_literals
import urlquick
import time
import base64
import json
from xbmc import executebuiltin
from xbmcgui import Dialog
from uuid import uuid4
from codequick.storage import PersistentDict
from codequick import Script
from codequick.script import Settings
from functools import wraps
from distutils.version import LooseVersion
from datetime import datetime, timedelta
from .constants import ANM, GSET, SSET, runPg

dtnow = datetime.now()
strdtnow = str(dtnow.strftime("%a, %d %b %Y at %I:%M %p"))
sesTime = 1728000

def secLeft():
    with PersistentDict("headers") as db:
        exp = db.get("exp", 0)
    return int(exp - time.time())

decdaysLeft = secLeft() / 86400
daysLeft = int(decdaysLeft)
hoursLeft =  int(decdaysLeft * 24)

def actstatus():
    strdaysLeft = str(daysLeft) + (" day" if daysLeft == 1 else " days")
    strhoursLeft = str(hoursLeft) + (" hour" if hoursLeft == 1 else " hours")
    strtimeLeft = strhoursLeft if daysLeft < 1 else strdaysLeft
    actdt = ("Active on " + strdtnow + ". Auto-login after " + strtimeLeft)
    SSET("astatus", actdt)

def expstatus():
    expdate = dtnow + timedelta(days=daysLeft)
    SSET("estatus", "Session till " + expdate.strftime("%a, %d %b %Y ") + GSET("exptime"))

def getHeaders():
    with PersistentDict("headers") as db:
        return db.get("headers", False)

def quality_to_enum(quality_str, arr_len):
    mapping = {
        'Best': arr_len-1,
        'High': max(arr_len-2, arr_len-3),
        'Medium+': max(arr_len-3, arr_len-4),
        'Medium': max(2, arr_len-3),
        'Low': min(2, arr_len-3),
        'Lower': 1,
        'Lowest': 0,
    }
    if quality_str in mapping:
        return min(mapping[quality_str], arr_len-1)
    return 0

def notif(msg):
    Script.notify(msg, ANM)

def logstatus(io):
    Logio = "Logged " + io
    tf = "true" if io == "in" else "false"
    SSET("lstatus", Logio + " on " + strdtnow)
    SSET("isloggedin", tf)
    notif(Logio)

def reLogin():
    SSET("isloggedin", "false")
    notif("Login please")
    executebuiltin(runPg + "login/)")

def isLoggedIn(func):
    @wraps(func)
    def login_wrapper(*args, **kwargs):
        with PersistentDict("headers") as db:
            username = db.get("username")
            password = db.get("password")
            headers = db.get("headers")
            exp = db.get("exp", 0)
        if headers and exp > time.time():
            SSET("isloggedin", "true")
            return func(*args, **kwargs)
        elif username and password:
            login(username, password)
            return func(*args, **kwargs)
        elif headers and exp < time.time():
            reLogin()
            return False
        else:
            reLogin()
            return False
    return login_wrapper

def login(username, password, mode="unpw"):
    resp = None
    if (mode == 'otp'):
        mobile = "+91" + username
        otpbody = {
            "number": base64.b64encode(mobile.encode("ascii")).decode("ascii"),
            "otp": password,
            "deviceInfo": {
                "consumptionDeviceName": "ZUK Z1",
                "info": {
                    "type": "android",
                    "platform": {
                        "name": "ham"
                    },
                    "androidId": str(uuid4())
                }
            }
        }
        resp = urlquick.post("https://jiotvapi.media.jio.com/userservice/apis/v1/loginotp/verify", json=otpbody, headers={"User-Agent": "okhttp/4.2.2", "devicetype": "phone", "os": "android", "appname": "RJIL_JioTV"}, max_age=-1, verify=False, raise_for_status=False).json()
    else:
        body = {
            "identifier": username if '@' in username else "+91" + username,
            "password": password,
            "rememberUser": "T",
            "upgradeAuth": "Y",
            "returnSessionDetails": "T",
            "deviceInfo": {
                "consumptionDeviceName": "ZUK Z1",
                "info": {
                    "type": "android",
                    "platform": {
                        "name": "ham",
                        "version": "9.0.0"
                    },
                    "androidId": str(uuid4())
                }
            }
        }
        resp = urlquick.post("https://api.jio.com/v3/dip/user/{0}/verify".format(mode), json=body, headers={"User-Agent": "JioTV", "x-api-key": "l7xx75e822925f184370b2e25170c5d5820a", "Content-Type": "application/json"}, max_age=-1, verify=False, raise_for_status=False).json()
    if resp.get("ssoToken", "") != "":
        _CREDS = {
            "ssotoken": resp.get("ssoToken"),
            "userid": resp.get("sessionAttributes", {}).get("user", {}).get("uid"),
            "uniqueid": resp.get("sessionAttributes", {}).get("user", {}).get("unique"),
            "crmid": resp.get("sessionAttributes", {}).get("user", {}).get("subscriberId"),
            "subscriberid": resp.get("sessionAttributes", {}).get("user", {}).get("subscriberId"),
        }
        headers = {
            "deviceId": str(uuid4()),
            "devicetype": "phone",
            "os": "android",
            "osversion": "9",
            "user-agent": "plaYtv/7.1.2 (Linux;Android 9) ExoPlayerLib/2.11.7",
            "usergroup": "tvYR7NSNn7rymo3F",
            "versioncode": "320",
            "dm": "ZUK ZUK Z1"
        }
        headers.update(_CREDS)
        with PersistentDict("headers") as db:
            db["headers"] = headers
            db["exp"] = time.time() + sesTime
            if mode == "unpw":
                db["username"] = username
                db["password"] = password
        SSET("exptime", dtnow.strftime("at %I:%M %p"))
        SSET("isunpw", "true")
        logstatus("in")        
        return None
    else:
        msg = resp.get("message", ANM)
        SSET("isloggedin", "false")
        notif("Login Failed " + msg)
        return msg

def sendOTP(mobile):
    mobile = "+91" + mobile
    body = {"number": base64.b64encode(mobile.encode("ascii")).decode("ascii")}
    resp = urlquick.post("https://jiotvapi.media.jio.com/userservice/apis/v1/loginotp/send", json=body, headers={"user-agent": "okhttp/4.2.2", "os": "android", "host": "jiotvapi.media.jio.com", "devicetype": "phone", "appname": "RJIL_JioTV"}, max_age=-1, verify=False, raise_for_status=False)
    if resp.status_code != 204:
        return resp.json().get("errors", [{}])[-1].get("message")
    return None

def check_addon(addonid, minVersion=False):
    try:
        curVersion = Script.get_info("version", addonid)
        if minVersion and LooseVersion(curVersion) < LooseVersion(minVersion):
            Script.log('{addon} {curVersion} doesn\'t setisfy required version {minVersion}.'.format(
                addon=addonid, curVersion=curVersion, minVersion=minVersion))
            Dialog().ok("Error", "{minVersion} version of {addon} is required to play this content.".format(
                addon=addonid, minVersion=minVersion))
            return False
        return True
    except RuntimeError:
        Script.log('{addon} is not installed.'.format(addon=addonid))
        if not _install_addon(addonid):
            Dialog().ok("Error",
                        "[B]{addon}[/B] is missing on your Kodi install. This add-on is required to play this content.".format(addon=addonid))
            return False
        return True

def _install_addon(addonid):
    try:
        executebuiltin('InstallAddon({})'.format(addonid), wait=True)
        version = Script.get_info("version", addonid)
        Script.log(
            '{addon} {version} add-on installed from repo.'.format(addon=addonid, version=version))
        return True
    except RuntimeError:
        Script.log('{addon} add-on not installed.'.format(addon=addonid))
        return False

def logout():
    with PersistentDict("headers") as db:
        del db["headers"]
    logstatus("out")
