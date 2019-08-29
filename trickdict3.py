# Hey this is new file for python dict
# #building a dictionary incrementally
# person = {}
# person['Name'] = 'Jason'
# person['lname']= 'Bourne'
# person['age']= 36
# person['spouse'] = 'Anna'
# person['childrn']= ['Matt','Annie']
# person['pets'] ={'dog':'Germanshepherd','cat':'bree'}
# print(person)
#
# # How to use Get method in nested dictionary
# a = person.get('pets').get('ak','not exist')
# print(a)
#
# # a tuple can also used to a dictionary key
# a_dict = {(1,1):'Mukesh',(2,2): 'vaibhav'}
# print(a_dict)
# print(a_dict[(1,1)])
#
# # A list should not be a key in dictionary
#
# b_dict = {[1,2]:'mukesh'}
# print(b_dict)
# note U should pass a hashable object as key (hashable ---> immutable)
a = (1,2)
print(type(a))
print(hash(a))

b = 'mukesh'
print(hash(b))

# list object is not hashbale
c = [1,'m']
print(hash(c))