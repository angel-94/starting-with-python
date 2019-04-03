
dict_one = {
	"book": "Uno",
}

dict_cart = {
	"name_product": "Book",
	"quantity": 23,
	"price": 123.9213
}

'''
Al this values are a dictionary
'''

print(type(dict_cart))
# print(dir(dict_cart))

print(dict_cart.keys())
print(dict_cart.items())

dict_cart.pop('price')
print(dict_cart)
