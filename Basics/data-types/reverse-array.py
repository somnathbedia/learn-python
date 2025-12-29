list = [67,78,54,23,98,100]

def reverse(list):
    i=0
    last=len(list)-1
    while i <= last:
        temp = list[i]
        list[i]=list[last]
        list[last]=temp
        i+=1
        last-=1

reverse(list)

print(list)


def reverse_pythonic_way(list):
    i=0
    last=len(list)-1
    while i<=last:
        list[i],list[last]=list[last],list[i]
        i+=1
        last-=1

reverse_pythonic_way(list)
print(list)
