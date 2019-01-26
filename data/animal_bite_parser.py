import collections

def parse_line(string):
	arr = line.split("|")
	zipcode = ""
	createdate = ""
	if arr[7] == "INVESTIGATION / BITE / Priority 1":
		zipcode =  arr[3][-5:]
		createdate = arr[4][:9]
	return (zipcode, createdate)



file = open("barcbites12m_2017-09-11.txt", "r")
info = file.readlines()

map_bites = collections.defaultdict(int)
for line in info[1:]:
	(zipcode, createdate) = parse_line(line)
	if zipcode != "":
		map_bites[createdate] += 1

print(map_bites)
