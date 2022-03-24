# ***** Dictionaries

# Dictionaries cannot be sorted and they do not retain an order

# Dictionaries can store multiple data types at the same time
my_dict = {
    "key1": "value",
    "key2": 123,
    "key3": [1, 2, 3],
    "key4": {"innerDict": 100},
}
print(my_dict["key2"])
print(my_dict["key3"][1])
print(my_dict["key4"]["innerDict"])

prices = {
    "apple": 2.99,
    "oranges": 1.99,
    "milk": 5.80,
}

print(prices["apple"])

# To add entries to a dictionary just put the key in brackets and assign it a value
prices["bread"] = 3.50
print(prices)

# To edit an existing entry, just call the key in brackets and assign a new value
prices["apple"] = 1.50
print(prices)

# .keys() will return all the keys of a dictionary
price_keys = prices.keys()
print(price_keys)

# .values() will return all the values of a dictionary *** DOES NOT RETURN A LIST
price_vals = prices.values()
print(price_vals)

# .items() will return all the key/value pairs of a dictionary *** DOES NOT RETURN A LIST
price_items = prices.items()
print(price_items)
