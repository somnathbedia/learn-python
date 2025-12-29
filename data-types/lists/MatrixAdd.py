A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[10,11,12],[13,14,15],[16,17,18]]

#  Assignment of elements using list comprehension
C = [[0 for i in range(0,3)] for i in range(3)]


for i in range(0,3):
    for j in range(0,3):
        C[i][j]=A[i][j]+B[i][j]

# print(C)

# C.append(7)



# C.sort()

# print(C)

D = [345,6,23,11,4,1,100,12]

# D.sort() -> [1, 4, 6, 11, 12, 23, 100, 345]

print(D)

