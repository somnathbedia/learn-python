A = [45,78,100,150,170,180,200]

def binarySearch(A,start,end,key):
    if start<end:
        mid=(start+end)//2
        if A[mid] == key:
            return mid
        elif key > A[mid]:
            return binarySearch(A,mid+1,end,key)
        elif key < A[mid]:
            return binarySearch(A,start,mid-1,key)
        else:
            return -1


key = 180

index = binarySearch(A,0,len(A)-1,key)

print(index)