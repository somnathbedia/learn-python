import math

num=int(input("Enter number to find factors "))

for i in range(1,num+1):
    if num%i == 0:
        print("Factors: ",i)

# for i in range(1,int(math.sqrt(num))):
#     if num%i == 0:
#         print(i)
#         if i != math.sqrt(num):
#             print(num//i)

factors_list=[]
i=1
while i <= int(math.sqrt(num)):
    if num%i == 0:
        factors_list.append(i)
        if i != int(math.sqrt(num)):
            factors_list.append(num//i)
    i+=1

print(factors_list)