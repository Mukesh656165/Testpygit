# Some new tricks to avoid error
# film = {'jimmy':'jack','neesham':'ryder','array':'james'}
#
# print('jimmy' in film)
# print('jack' in film)
#
# print('torronto' in film)
# print(film['jack'])
#
# # To avoid this error we can use
# a = 'torronto' in film and film['torronto']
#
# print(a)
# This is called trick

# Recap to the Built in methods in python dictionary
# My_dict = {'amit':12000,'Sathis':15000,'Adasrs':12000,'Latanjalli':12500,'Vaibhav':18000}
# print(My_dict)

# Clear() method
# My_dict.clear()
# print(My_dict)

# returning None
# a = My_dict.clear()
# print(a)
# get()  A convinient way to get value in dictionary
# a = My_dict.get('amit')
# print(a)
# b = My_dict.get('Mukesh')
# print(b)
# If key is not present then Default value
# c = My_dict.get('jackson','Item is not avialbale')
# print(c)

# Get() used in nested dictionary
# my_dict = {'fname':'Mukesh','lname':'singh','age':26,'mobile':{1:'Samsung',2:'Vivo'}}
# print(my_dict)
# a = my_dict['mobile']
# print(a)
# b = my_dict['mobile'][1]
# print(b)
# c = my_dict.get('mobile').get('1','not')
# print(c)
# If a key is not avialable in the dictionary

# d = my_dict.get('mobile').get('iphone','This item is not exist in the dict')
# print(d)
# items() returns---> list of tuple<--- of items
# my_dict ={'vivo':15500,'iphone':50000,'google_pixel':100000}
# print(my_dict)
# a = my_dict.items()
# print(a)
# b = list(my_dict.items())
# print(b)
# d = list(my_dict.items())[0]
# print 1st key-->value
# print(d)
# to access 1st key in dict
# e = list(my_dict.items())[0][0]
# print(e)
# to print 2nd key--value 1st key
# f = list(my_dict.items())[1][0]
# print(f)

# items() method in dict it returns list of values
# d = {'mukesh':'python dev','vaibhav':'ps'}
# a = d.keys()
# # print(a)
# print(d.keys())
# # although it returns as list so make it as list abnormally
# b = list(d.keys())
# print(b)

# values() --->returns all values as list
# d = {'mukesh':'python dev','vaibhav':'ps'}
# a = d.values()
# print(a)
# print(d.values())
# b = list(d.values())
# print(b)
# print(id(b)) # it is also refercing diffrent dict object
# # any duplicate value in dict return as many time it occur
# a = {'mk':10,'vak':10,'rk':10}
# b = list(a.values())
# print(b)
# print(id(b))# it is reffrencing diffrent dict object

# tech point--> items(),keys(),values()actully it returns somthing called  view objct for pratically
# we can think it return list of dictionary

# pop() method remove key from dict if it present and return its value
# d = {'ak':1000,'bk':20,'ck':5000}
# a = d.pop('ck')
# print(a)
# print(d)
# key error exception if key is not present
# c = d.pop('rk')
# print(c)
# if key is not present then use default value
# b = d.pop('rk','not in dict')
# print(b)

# popitem() # to remove random key value pair in the dict
# a = {'python':5,'java':4,'java_script':4.5}
# b = a.popitem()
# print(b)
# print(a)
# c = a.popitem()
# print(c)
# print(a)

# # exception if dict is empty{}
# d = {}
# a = d.popitem()
# print(a)

# Update() method
d = {'mk':1000,'rk':5000,'ab':2000}
d1 = {'ak':3000,'ck':500}
a = d.update(d1)
print(a) # none is op
d.update(d1)
print(d)
d1.update(d)
print(d1)
# if similar key then override
d2 = {'mk':200,'jk':2000}
d.update(d2)
print(d)
# we may update to as list of tuple
print('------>*--------->')
d3 = [('mk',320),('jk',520)]
d.update(d3)
print(d)

# we can specified values by kwargs
print('------->*------>')
d5 = {'a':360,'b':365,'c':520}
print(d5)
d5.update(b=200,c=386)
print(d5)
print('---->***------>')
# to print 30
x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]
print(x)
print(x[1])
print(x[1]['foo'])
print(str(x[1]['foo']))
a = ['a',{'f':0}]
print(len(a))
print(a[0])
print(a[1])
print('----->---->')
print(a[1]['f'])

x = ['a','b',{'foo':1,'bar':{'x':10,'y':20,'z':30},'baz':3},'c','d']
print(len(b))
print(x[2]['bar']['z'])
print(x[2])
print(x[2]['bar'])
print(x[2]['bar']['z'])
v = {'a':100,'b':200}
v.pop(200)
print(v)

# to create dict with existing dict
d1 = dict(d2)


