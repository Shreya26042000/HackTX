import googlemaps

API_KEY = "AIzaSyA7pSNKto5Cdp-IIi9D0e5msQdmE_2KkeM"

def getLocations(coordinates='30.264980,-97.746597'):
    gmaps = googlemaps.Client(key=API_KEY)

    names = []
    places_result = gmaps.places_nearby(location=coordinates, radius= 10000, open_now=False, keyword='Shelter')
    for place in places_result['results']:
        names.append(place['name'])
    return names