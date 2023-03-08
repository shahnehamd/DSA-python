def bubbleSort(arr,arr2):
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

arr = [156,141,35,94,61,111]
arr2 = ['R','S','A','B','P','Z']

n = len(arr)
bubbleSort(arr,arr2)
op = dict(zip(arr2,arr))
print(op)
