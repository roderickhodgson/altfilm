from urllib import urlencode, urlopen
import json
from suggest.models import *
def geolocate():
    total = Venue.objects.count()
    counter = 0
    for v in Venue.objects.all():
        if v.lat == "" and v.lng == "":
            querystring = v.address + ", UK"
            args = urlencode({'address': querystring, 'sensor': 'false', 'region': 'uk'})
            api_url = "http://maps.googleapis.com/maps/api/geocode/json?"+args

            print api_url
            data = json.load(urlopen(api_url))
            if (data["status"] != "ZERO_RESULTS"):
                try:
                    v.lat = data['results'][0]['geometry']['location']['lat']
                    v.lng = data['results'][0]['geometry']['location']['lng']
                    v.save()
                except:
                    pass

        counter += 1
        print counter
