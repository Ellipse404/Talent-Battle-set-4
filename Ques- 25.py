 #  Q: Find the repeating  elements in an Array : #
            
def Repeating_Numbers(arr, size):

    print("Reapeatiung Numbers Are : ")
    hash_table = {}
    for x in range(size):
        if arr[x] not in hash_table :
            hash_table[arr[x]] = 0

        hash_table[arr[x]] += 1

    for y in hash_table:
        if (hash_table[y] > 1):
            print(y, end = ' ')

li  = list(map(int, input("Enter The Numbers In Array seperated by Commaa(,)").split(',')))
Repeating_Numbers(li, len(li))
