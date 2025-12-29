# Tuples is an immutable list 
# Tuples object does not support item assignment

# Characterstics
# 1. Ordered (1,2,3,4) != (4,3,2,1)
# 2. Unchangeable
# 3. Allow duplicate

t1 = (1,2,3,4,1,4)

print(t1)

#create tuple using single element

# t2 = (1,)
# print(t2)

t3 = ("Hello",)
# print(t3)

#using type conversion

t4 = tuple("Hello")
print(t4)

# t5 = tuple(2) 'int' object is not iterable
# print(t5)