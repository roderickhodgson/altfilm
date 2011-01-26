# Create your views here
#
from django.http import HttpResponse
from django.template import Context, loader
from urllib import urlencode, urlopen
import json
from suggest.models import *
from operator import itemgetter
from django.core import serializers

def json_lat_lng(request, addr):
    args = urlencode({'address': addr, 'sensor': 'false', 'region': 'uk'})
    api_url = "http://maps.googleapis.com/maps/api/geocode/json?"+args

    data = json.load(urlopen(api_url))
    output = {}
    output['address'] = data['results'][0]['formatted_address']
    output['lat'] = data['results'][0]['geometry']['location']['lat']
    output['lng'] = data['results'][0]['geometry']['location']['lng']
    try:
        f = open('/home/roderick/sites/ukfcsuggest/searchlog.txt', 'a')
        f.write("\n"+addr)
        f.close() 
    except:
        pass #fail silently    
    return HttpResponse(json.dumps(output), mimetype='text/javascript')

def json_find_simple(request, lat, lng):
    return json_find_venues(request, lat, lng, '', '')

def json_find_venues(request, lat, lng, country, director):
    venues_f = {}
    venues_final = []

    venues = Venue.objects.all()
#     if country != "":
#         try: country_obj = Country.objects.get(name__iexact=country)
#         except: country = ""
# 
#     if director != "":
#         try: director_obj = Director.objects.get(name__iexact=director)
#         except: director = ""
# 
#     if country == "" and director == "":
#         venues = Venue.objects.all()
# 
#     if country != "":
#         allvenues = Venue.objects.all()
#         venues = []
#         for v in allvenues:
#             if len(v.film_set.filter(country=country_obj)) > 0:
#                 venues.append(v)
# 
#     if director != "":
#         allvenues = Venue.objects.all()
#         venues = []
#         for v in allvenues:
#             if len(v.film_set.filter(director=director_obj)) > 0:
#                 venues.append(v)

    for v in venues:
         venues_f[v.id] = v.dist_to((lat, lng))

    venues_f = sorted(venues_f.items(), key=itemgetter(1))[0:20]
    for f in venues_f:
        venues_final.append(Venue.objects.get(pk=f[0]))

    venues_json = serializers.serialize("json", venues_final)
                
    return HttpResponse(venues_json, mimetype='text/javascript')

