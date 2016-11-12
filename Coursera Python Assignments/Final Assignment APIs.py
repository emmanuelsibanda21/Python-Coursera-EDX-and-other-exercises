import urllib
import json
place = raw_input("Enter a place name: ")
begin = "http://python-data.dr-chuck.net/geojson?sensor=false&"
destination = urllib.urlencode({'address': place})
final = begin + destination

print "Retrieving {0}".format(final)
connect = urllib.urlopen(final)
information = connect.read()
print "Retrieved {0} characters".format(len(information))
data = json.loads(information)
print "Place id", data["results"][0]["place_id"]
