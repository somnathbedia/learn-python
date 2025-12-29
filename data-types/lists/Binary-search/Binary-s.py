A = [2,3,4,6,8,10,12,18]

target = int(input('Enter Target element'))

def binary_search(A,target,n):
    start = 0
    end=n-1

    while (start <= end):
        mid = start + (end-start)//2

        if(A[mid]==target):
            return mid
        elif (A[mid] > target):
            end=mid-1
        else:
            start=mid+1
    
    return -1

index = binary_search(A,target,len(A))

print(index)
