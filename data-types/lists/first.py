my_list=[True,'Hello',1,10.6]

populaton=[]

current_population=1000
expected_population=0
number_of_years=3

for i in range(1,number_of_years+1):
    current_population=current_population+(current_population*0.1)
    populaton.append(current_population)

expected_population=populaton[-1]

print(expected_population)
