# Q : Find All the Distinct Elements in an Array :

try:
    arr = list(map(int, input("Enter The Elements Seperated by Comma(,): ").strip().split(',')))[:]

    def Distinct(Array):

        print("Distinct Array : ")

        #  Code -1 :
        hash_table = {}
        for x in range(len(Array)):
            if Array[x] not in hash_table:
                hash_table[Array[x]] = 0
            hash_table[Array[x]] += 1
        for y in hash_table:
            print(y, end = ' ')
        print('\n')
            
        # Code -2 :
        table = []
        for i in Array:
            if i not in table:
                table.append(i)
        for j in table:
            print(j, end = ' ')
            
        # Number of Occurance [unneccessary code]:
        print("\nNumber Of Occurance in the Array : ")
        for z in hash_table:
            print('\n',z," Occurs :",hash_table[z]," times.")
        
    Distinct(arr)
except:
    print("Check Your Input !! It may Wrong .. It can contain only Integers ..")
