price = [34.34,367.19,22,21,88.89,100]

sum=0

for i in range(0,len(price)):
    sum+=price[i]

average_price = sum/len(price)

print("Average price is ",average_price)

for i in range(0,len(price)):
    if type(price[i]) is int:
        print("Current price is ",type(price[i])," type")
    else:
        print(price[i])


