
import requests
import json
from datetime import date
from get_token import get_token

token = get_token('product.compact')
print(f"bearer {token}")#Save token to a variable

def GetLocationsByZip(token, zipcode, radius, limit):
    '''
    Example Usage:
    locs = GetLocationsByZip(
        token = token, 
        zip = '48085', 
        radius = 2, 
        limit = 4
    )
    print(locs)
    '''

    headers={'Authorization': f'Bearer {token}'}
    url = f'https://api.kroger.com/v1/locations?filter.zipCode.near={zipcode}&filter.radiusInMiles={radius}&filter.limit={limit}'
    locations = requests.get(url, headers=headers)
    # with open("./DataLake/Locations/locations_{}.json".format(str('date_{}').format(date.today())), "w") as file:
    #     json.dump(locations.json(), file)
    return locations.json()


locs = GetLocationsByZip(token, '48085', 2, 4)
print(locs)