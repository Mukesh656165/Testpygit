# dict comprehension tricks and usage
# using of zip functions
country =['australia','usa','india','spain','france']
city = ['melbourne','new york','new delhi','madrid','paris']
capitals = {key:value  for key,value in zip(country,city)}
print(capitals)

# turning keys into values through dict comprehenssion
a_dict = {'one':1,'two':2,'three':3}
new_dict = {value : key for key,value in a_dict.items()}
print(new_dict)
print(a_dict)

# filtering in the dict through comprehension
m_dict = {key : value for key, value in a_dict.items() if a_dict[key] == 3}
print(m_dict)

#  sum of values through comprehension
income = {'apple':150,'orange':180,'grape':120}
total = sum([value for value in income.values()])
print(total)
print(type(total))

# if u worked in large dict the its better to do same thing generator object
total1 = sum(value for value in income.values()) # its generator object bcz removing of square bracket
print(type(sum(value for value in income.values())))
print(total1)
print(type(total1))

# note genertor object is memory efficient and it is not storing in  the whole list in memory
# it yeilds  element on demand

# one simple way to solve this problem
print('------*-----')
total2 = sum(income.values())
print(total2)

# removing specific items through comprehension
d_dict = {'mk':'spcl',"pk":'orange','sk':'chiken'}
new_dict = {key : value for key,value in d_dict.items() - {'orange'}}
new_dict1 = {key : d_dict[key] for key in d_dict.keys() - {'orange'}} # its is one trick to remove
print(new_dict1)

print(new_dict)
