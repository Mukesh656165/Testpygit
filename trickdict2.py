# Welcome to dictionary tricks 2

# how to remove items using pop method

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# while True:
#     try:
#         print(f'Dictionary length: {len(a_dict)}')
#         item = a_dict.popitem()
#         # Do something with item here...
#         print(f'{item} removed')
#     except KeyError:
#         print('The dictionary has no item now...')
#         break

# to iterate both the dictionary
from collections import ChainMap
a_dict = {'fruit':'apple','fruit2':'mango'}
b_dict = {'price':180,'price2':190}

chained_dict = ChainMap(a_dict,b_dict)

print(chained_dict)
print(type(chained_dict))

# To access keys in the dictionary
for key in chained_dict.keys():
    print(key,'--->',chained_dict[key])

print('*--------->*------------>')
# another way to access keys and values in chainmap object
for key,value in chained_dict.items():
    print(key,'----->',value)