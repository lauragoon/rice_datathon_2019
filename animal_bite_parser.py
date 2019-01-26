import collections
import matplotlib
import matplotlib.pyplot as plt
from datetime import date
import mplleaflet

def parse_line(string):
	arr = line.split("|")
	zipcode = ""
	year = ""
	month = ""
	day = ""
	lat = ""
	lon = ""
	if (len(arr) >= 8) and (len(arr[7]) >= 33) and (arr[7][:33] == "INVESTIGATION / BITE / Priority 1"):
		zipcode =  arr[3][-5:]
		createdate = arr[4][:10]
		year = createdate[:4]
		month = createdate[5:7]
		day = createdate[8:]
		lat = arr[1]
		lon = arr[2]

	return (zipcode, year, month, day, lat, lon)



file = open("data/barcbites12m_2017-09-11.txt", "r")
info = file.readlines()

#map_bites = collections.defaultdict(int)
lats = []
lons = []
for line in info[1:]:
	(zipcode, year, month, day, lat, lon) = parse_line(line)
	if (len(lat.strip()) > 0):
		lats.append(float(lat.strip()))
		lons.append(float(lon.strip()))

	#if zipcode != "":
		#map_bites[(year, month, day)] += 1

#print(map_bites)
plt.hold()
#for i in range(20):
	#plt.plot(lats[i], lons[i])
plt.plot(lons, lats, "bo",  markersize = "2")
#plt.show()
#mplleaflet.display(ax.figure)
# mplleaflet.show()

def use():
	return lats, lons