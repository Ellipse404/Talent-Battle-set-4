arr = list(map(int, input("Enter the Array Elements Seperated by comma(',') :").strip().split(',')))[:]

# Code - 1 :

x = len(arr)-1
arr1 = []
for _ in range(len(arr)):    
    arr1.append(arr[x])    
    x-=1
print(arr1)

# Code - 2 :

print(arr[len(arr)-1::-1])
