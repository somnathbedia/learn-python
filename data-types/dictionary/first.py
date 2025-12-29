# Dictionaries are mutable
# Keys should be immutable
# duplicate key are not alowed
# The values in dictionary items can be of any data type but keys should be immutable:
# 1D Dic 
d1 = {'name':"Somnath",'Age':22,'Gender':"Male"}

print(d1)

# 2D Dic -> Dictionary inside dictionary -> JSON

d2 = {'name':"Harihar",'college':'SBU','sem':2,'Subjects':{
    'DSA':80,
    'Maths':100,
    'english':88
}}


# Dictionary using dict function 

# tuple inside list (IMP)
d4 =  dict( [('name','somnath'),('age',22),(3,3)] )

# print(d4)

# Mutable items as keys are not allowed 
# List is not allowed as key in dictionary




# Accessing items

my_dict = {'name':'bunny','Age':22}

# print(my_dict['name'])
# print(my_dict.get('Age'))

# Adding new key value pair 
my_dict['gender'] = 'Male'

# print(my_dict)

# Remove key value 

d5 = {'name':'Honey Singh','Profession':'Singer','gender':'Male','weight':80}

# Popping specific value 
# d5.pop('weight')


# removing last items 
# d5.popitem()

del d5['Profession']
# print(d5)

# membership operators

d6 = {'userId':'somnath.ig.swd','email':'somnath@gmail.com','address':{
    'village':'HRBR',
    'pin':829110,
    'PO':'sondimra'
}}

# Kya address key dictionary mein hai
# print('address' in d6)

d7 = {'name':'Nitish','gender':'Male','age':32}

# for i in d7:
#     print(i, d7[i])

d8 = d7.copy()

print(d8)




