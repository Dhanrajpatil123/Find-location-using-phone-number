
import phonenumbers
import folium
from phonenumbers import geocoder
number = "+91 9175172817"


pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, 'en')
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

# install opencage
from opencage.geocoder import OpenCageGeocode

key = "3f5b040c6abd4080a9a3c27f8e082c51"
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)


# install pip install folium 


myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")