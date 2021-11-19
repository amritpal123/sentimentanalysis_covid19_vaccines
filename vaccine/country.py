from geopy.geocoders import Nominatim

def Country(dataset):
    for i in range(0, len(dataset)):
        try:
            address = dataset['Location'][i]
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(address)
            print(location.latitude, location.longitude)

            location = geolocator.reverse(str(location.latitude) + ',' + str(location.longitude))

            address = location.raw['address']

            country = address.get('country', '')
            dataset['Country'][i] = country

            print(country)
        except:
            pass
    return dataset