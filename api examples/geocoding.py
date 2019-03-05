import urllib.request, json

#api to access, including street to get coordinates of
uri = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyAO05QuVhrCC72UUGFDN0Ui3Ouc-I40tIE"
url = urllib.request.urlopen(uri)

#get json from api
data = json.loads(url.read().decode())

#print lattitude and lingitude coordinates
print(data['results'][0]['geometry']['location']['lat'])
print(data['results'][0]['geometry']['location']['lng'])

