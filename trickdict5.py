# new dict for iterating and dict comprehensions
# from typing import Tuple

a_dict = {'apple':'fruit','dog':'pets','car':'vehicle','twitter':'social network'}
# to know the methods whtever dictionary holds
print(dir(a_dict),end='--->')

# using for loop to access the keys
for key in a_dict:
    print(key)
# simple trick to access keys and values --->with indexing oprator[]

for key in a_dict:
    print(key,'---->' ,a_dict[key])

# iterating over .items() and it will return a tuple object
d_items = a_dict.items()
print(d_items) # here it will return  view of items
# lets itreate
# items: Tuple[str, str]
for items in a_dict.items():
    print(items)
# here we can know  the view return by items() method
# its really a tuple object

for items in a_dict.items():
    print(items)
    print(type(items))

# once you know this then we will use tuple unpacking to iterate through keys and values
# lts take a look on tuple unpacking
for key,value in a_dict.items():
    print(key, '--->', value)
# in this way we have more control in this dictionary
# here key will hold the keys and value will hold the values every time iteration

# iterating through .keys()
a_keys = a_dict.keys()
print(a_keys)
# lts iterate overs
for key in a_dict.keys():
    print(key)

# iterating through .values()
d_value= a_dict.values()
print(d_value)

# iterate
for value in a_dict.values():
    print(value)
# here we can also test member ships
print('----->*------>')
a = 'apple' in a_dict.values()
print(a)
f = 'fruit' in a_dict.values()
print(f)


