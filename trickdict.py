# sorting a dict Key
a_dict = {'banana':500,'apple':200,'grape':250}
# new_dict = {k : a_dict[k]  for k in sorted(a_dict)}
# print(new_dict)

# sum of values
total_incm = 0.00
for value in a_dict.values():
    total_incm += value
print(total_incm)

# sorted by Keys
for key in sorted(a_dict):
    print(key,'--->',a_dict[key])
# Sorted of only values
for value in sorted(a_dict.values()):
    print(value)

# sorted with values and key
def by_value(item):
    return item[1]
for k, v in sorted(a_dict.items(), key=by_value):
    print(k, '->', v)

#change the key into values and then sorted as changes value as key
a_dict = {1:'jason',2:'james',3:'audit'}
new_dict = {}
for key,value in a_dict.items():
    new_dict[value]= key
print(new_dict)
for key in sorted(new_dict):
    print(key,'-->',new_dict[key])
