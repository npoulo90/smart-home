from get_products import product_details, search_products
from get_token import get_token

token = get_token('product.compact')
# print(token)
product = product_details(token=token, productid='0005200032866', locationid='01800757')
# product = search_products(token=token, term='bread', brand='private selection', limit='20')

print(product)