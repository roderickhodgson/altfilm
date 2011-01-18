import csv
from time import sleep
from suggest.models import *
ukfc_data = "/home/roderick/data/Screenings.csv"
f = open(ukfc_data)
def populate():
    hundrediter = 0
    for l in f:
        if hundrediter > 897000:
		name = address = ""
		r = csv.reader(l, delimiter=',', quotechar='"')
		it = 0
		for c in r:
		    if it==8:
			name = c[0]
		    if it==14:
			address += c[0]
		    if it==18:
			address += ", "+ c[0]
		    if it==20:
			address += ", "+ c[0]
		    it += 1

		
		venue, p= Venue.objects.get_or_create(name=name, address=address)
		venue.save()

	hundrediter += 1
	if hundrediter % 100 == 0:
	    print hundrediter 

