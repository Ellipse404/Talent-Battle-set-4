def Non_Repeating(Array, Size):

    print("Non-Repeating Numbers Are : ")
    hash_table = {}
    for x in range(Size):
        if (Array[x] not in hash_table):
            hash_table[Array[x]] = 0
        hash_table[Array[x]] += 1
#  print(hash_table)
    for y in hash_table:
        if (hash_table[y] == 1) :
            print(y, end = " , ")

li = list(map(int, input("Enter The Number of Array seperated by comma (,) : ").split(',')))
Non_Repeating(li, len(li))
