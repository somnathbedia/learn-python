# {key:value for vars in iterable}

distances = {'delhi':1000,'mumbai':2000,'chennai':1100}

print(distances.items())

newDis = {key:value*0.1 for (key,value) in distances.items()}

# print(newDis)

# zip()

print(zip(distances))

