# Adding some new tricks
# dlete a key through iteration
fruits = {'apple':500,'orange':200,'dates':150}

# make dictionary as list object
for key in list(fruits.keys()):
    if key == 'apple':

        del fruits[key]
print(fruits)

# if we directly use .keys() and delete it will raise an error
# because dict.keys() returns a view object which yeilds keys on demand at a time

# lts check
for key in fruits.keys():
    if key == 'orange':
        del fruits[key]

# note ---> its technical point

# real world example
#Turning keys into values
capitals = {'uk':'london','germany':'berlin','australia':'melbourne','netherlands':'amsterdam'}
new_value = {}
for key,value in capitals.items():
    new_value[value] = key
print(capitals)
print(new_value)

# trying to filtering the values through if conditions
test = {'one':1,'two':2,'three':3,'four':4}
new_value1 = {}
for key ,value in test.items():
    if value ==3:
        new_value[key]= value
print(new_value)


