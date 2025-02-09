'''
Authorized
Token URL: https://api.kroger.com/v1/connect/oauth2/token
Flow: clientCredentials
'''


import requests
import json
from datetime import datetime

# Get the product
def search_products(token: str, term: str, productId: str = "", locationId="01800757", brand: str = "Kroger", fulfillment: str = "ais", limit: str = "5"):
    """
    term: string (query)
        A search term to filter product results. As an example, you could
        input milk, bread, or salt. 

        Note - Search terms are limited to a maximum of 8 words. Each new
        space in the search term denotes a new word.

    token: string
    locationId: string (query)
        The locationId of the location. When using this filter, only products available at that location are returned.
    productId: string (query)
        The productId of the products(s) to return. For more than one item, the list must be comma-separated. When used, all other query parameters are ignored.
    brand: string (query)
        The brand name of the products to return. When using this filter, only products by that brand are returned. Brand names are case-sensitive, and lists must be pipe-separated.
    fulfillment: string (query)
        'The available fulfillment types of the product(s) to return. 
        Fulfillment types are case-sensitive, and lists must be 
        comma-separated. Must be one or more of the follow types:
        ais - Available In Store
        csp - Curbside Pickup
        dth - Delivery To Home
        `sth` - Ship To Home'
    start: integer (query)
        The number of products to skip.
    limit: integer (query)
        The number of products to return.

    example usage:
    
        from get_products import search_products
        from get_token import get_token

        token = get_token('product.compact')
        print(token)
        search_products(token= f"bearer {token}",
                        term = "bread", 
                        # location_id = "01800757", 
                        # productId = "", 
                        brand = "private selection", 
                        # fulfillment = "", 
                        limit = "20") 



    """

    term        = term if term == "" else f"&filter.term={term}"
    locationId  = locationId if locationId == "" else f"&filter.locationId={locationId}"
    productId   = productId if productId == "" else f"&filter.productId={productId}"
    brand       = brand if brand == "" else f"&filter.brand={brand}"
    fulfillment = fulfillment if fulfillment == "" else f"&filter.fulfillment={fulfillment}"
    limit       = limit if limit == "" else f"&filter.limit={limit}"
    url = f"https://api.kroger.com/v1/products?{term}{locationId}{productId}{brand}{fulfillment}{limit}".replace(" ", "%20")
    headers = {
        'accept': 'application/json',
        'Authorization': f'{token}'
    }
    products = requests.get(url, headers=headers)
    
    # with open("./DataLake/Products/products_{}.json".format(str(datetime.now())), "w") as file:
    #     json.dump(products.json(), file)
    
    return products.json()
    
def product_details(token="", productid="0005200032866", locationid="01800757"):
    url = f'https://api.kroger.com/v1/products/{productid}?filter.locationId={locationid}'
    headers = {'accept':'application/json','Authorization': f'Bearer {token}'}
    response = requests.get(url=url, headers=headers)
    return response.json()
