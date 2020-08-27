arr1 = list(map(int, input("Enter The Elements Seperated by Comma(,): ").strip().split(',')))[:]
arr2 = list(map(int, input("Enter The Elements Seperated by Comma(,): ").strip().split(',')))[:]
def Disjoint(Array1, Array2):
    x = []
    for x in range(len(Array1)):
        if (Array1[x] in Array2):
            x.append(Array[x])
            print("Not Disjoint ..", (i for i in x), "is common in two Arrays")
        else:
            print("It's Disjoint")
Disjoint(arr1, arr2)
            
