def QuickSorty(A):
    if len(A)<=1:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        more = [i for i in A[1:] if i > pivot]
        return QuickSorty(less) + [pivot] + QuickSorty(more)
A = [33,37,15,10,6,35,57]
ans = QuickSorty(A)
print(ans)
