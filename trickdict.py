# sorting a dict Key
a_dict = {'banana':500,'apple':200,'grape':250}
new_dict = {k : a_dict[k]  for k in sorted(a_dict)}
print(new_dict)
