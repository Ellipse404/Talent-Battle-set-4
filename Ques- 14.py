arr = list(map(int, input("Enter the Array Elements Seperated by comma(',') :").strip().split(',')))[:]
# Code -1 : [ with changing the array ]
arr.remove(max(arr))
print(max(arr))

# Code -2 : [without changing the array ]

arr1 = sorted(arr)
print(arr1[-2])

# Code -2.1 :
arr2 = sorted(arr)
x = 2
for _ in range(len(arr2)):
    if max(arr) == arr2[-x]:
        x += 1
    else:
        print(arr2[-x])
