A=[98,100,34,10,500,78,200]

def bubbleSort(A):
    n=len(A)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]


bubbleSort(A)


# for i in range(0,len(A)):
#     print(A[i])

print(A)
