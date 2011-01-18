from urllib import urlencode, urlopen
import json
import re
from time import sleep
from suggest.models import *
def geolocate():
    total = Venue.objects.count()
    counter = 0
    for v in Venue.objects.all():
        if v.lat == "" and v.lng == "":
            querystring = v.address + ", UK"
            #temp
            try:
	        querystring = re.search("[A-Z0-9]{2,4} *[A-Z0-9]{2,4}", v.address).group(0)
            except:
                print "Failed to get postcode for " + v.address 
                print "Will use " + querystring
            if len(querystring) == 7 and not re.search(" ", querystring):
                querystring = querystring[0:-3] + " " + querystring[-3:]
            args = urlencode({'address': querystring, 'sensor': 'false', 'region': 'uk'})
            api_url = "http://maps.googleapis.com/maps/api/geocode/json?"+args

            data = json.load(urlopen(api_url))
            if (data["status"] == "OVER_QUERY_LIMIT"):
                print "Over Google's limit"
                return
            if (data["status"] != "ZERO_RESULTS"):
                try:
                    v.lat = data['results'][0]['geometry']['location']['lat']
                    v.lng = data['results'][0]['geometry']['location']['lng']
                    v.save()
                except Exception as e:
                    print e
                    print data
            else: 
                print "Google gave 0 results for " + querystring

        counter += 1
