a = [['молоток', 300], ['телевизор', 1000]]
b = [{'name': 'молоток', 'price': 300}, {'name': 'телевизор', 'price': 1000}]

# def get_price(product):
#     return product[1]
#
# a.sort(key=get_price, reverse=True)
a.sort(key=lambda product: product[1])
print(a)

b.sort(key=lambda product: product['price'])
print(b)
