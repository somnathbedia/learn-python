A = [
    [1,2,3],
    [4,5,6]
]

B=[
    [8,9,10],
    [11,12,13]
]

def sumMatrix():
    rows = len(A)
    cols = len(A[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            result[i][j]=A[i][j]+B[i][j]
    return result

# ans=sumMatrix()

result = [[0 for _ in range(4)] for _ in range(4)]
        # [0,0,0,0]*4

        
print(result)

