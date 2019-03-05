from pyexcel_ods import get_data
from pyexcel_ods import save_data
import urllib.request
import json

data = get_data("/Users/b-macbook/Desktop/krimewatch.ods")
out = data

#extract dates and times
for x in range(5):
    out['Sheet1'][x][1] = data['Sheet1'][x][2][0:8]
    out['Sheet1'][x][2] = data['Sheet1'][x][2][9:18]

#get Geo Coordinates
for x in range(5):
    streetName = out['Sheet1'][x][3].replace(" ", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + streetName + "&key=AIzaSyAO05QuVhrCC72UUGFDN0Ui3Ouc-I40tIE"
    uri = urllib.request.urlopen(url)
    geoData = json.loads(uri.read().decode())
    out['Sheet1'][x][4] = geoData['results'][0]['geometry']['location']['lat']
    out['Sheet1'][x][5] = geoData['results'][0]['geometry']['location']['lng']

out['Sheet1'][0][1] = "Date"
out['Sheet1'][0][2] = "Time"
out['Sheet1'][0][4] = "Lat"
out['Sheet1'][0][5] = "Lng"
save_data("/Users/b-macbook/Desktop/krimewatch 2.ods", out)


#635 items in dataset