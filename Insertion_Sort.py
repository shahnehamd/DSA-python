A = [15,41,35,14,31,11]
for i in range(1,len(A)):
    j=i
    while j>0 and A[j]<A[j-1]:
        A[j],A[j-1] = A[j-1],A[j]
        j = j-1
print(A)
