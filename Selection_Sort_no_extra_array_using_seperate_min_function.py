def mini_fun(a):
    mini = a[0]
    ind = 0
    for i in range(len(a)): #do 1,len(a) to reduce 1 iteration
        if a[i]<mini:
            mini = a[i]
            ind = i
    return ind

B = []
def SelectionSort(A):
    for i in range(len(A)):
        ind = mini_fun(A[i:])
        print(A[ind+i])
        A[ind+i],A[i] = A[i],A[ind+i]
        print(A)
A = [29,10,14,5,37]
SelectionSort(A)
print(A)
