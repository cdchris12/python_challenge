#!/usr/bin/python

import urllib
import urllib2
import json
import os.path
import time
import re
from datetime import datetime, timedelta
import sys
import base64


BASEurl = "https://api.xforce.ibmcloud.com/"

sys.path.append('./')

try:
    import iprep_conf as IC
    assert IC.xfex_cred != "key:secret"
except:
    print "Please create a config file which contains a valid set of API credentials."
    sys.exit(1)
# End try/except block

authstring = base64.encodestring(IC.xfex_cred).replace('\n','')

yesterday = datetime.now() - timedelta(days=1)
YEST = yesterday.strftime('20%y-%m-%dT00:00:00Z')

headers = {
    "Authorization": "Basic %s " % authstring,
    "Accept": "application/json",
    'User-Agent': 'Mozilla 5.0'}

def getip(ip):
    try:
        furl = BASEurl + "ipr/%s" % ip
        furl2 = BASEurl + "ipr/malware/%s" % ip

        request = urllib2.Request(furl, None, headers)
        data = urllib2.urlopen(request)
        data2 = json.loads(data.read())

        request = urllib2.Request(furl2, None, headers)
        data = urllib2.urlopen(request)
        data3 = json.loads(data.read())

        merged_dict = {key: value for (key, value) in (data2.items() + data3.items())}
        return merged_dict
        #return str(data2)
        #return [data2[u"history"][0]["geo"]["country"], data2[u"score"], data2[u"reason"], data2[u"categoryDescriptions"]]
    except:
        return [str(data2), "Ups", "Ups", "ups"]
    # End try/except block
# End def

def extractIP(text):
    ip = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b")
    return ip.findall(text)[0]
# End def

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip" , default=None, help="get IP intel", metavar="IP_Address")

    (options, args) = parser.parse_args()

    if options.ip is not None:
        res = extractIP(options.ip)
        if not res:
            print "You entered an invalid IP address. Please retry your query with a valid address."
            sys.exit(1)
        else:
            ip_res = getip(res)
        # End if/else block
    else:
        "Please specify an IP address to retrieve information for."
        sys.exit(1)
    # End if/else block
# End if

