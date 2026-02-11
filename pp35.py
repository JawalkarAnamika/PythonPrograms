def readlist(list1):
    n=int(input("Enter the number"))
    for i in range(0,n):
        x=int(input("Enter the element of list"))
        list1.append(x)
def displaylist(list1):
    print(list1)
def maxmin(list1):
    max=0
    for x in list1:
        if max<x:
            max=x
    min=list1[0]
    for z in list1:
        if min>z:
            min=z
    return max,min
list1=[]
readlist(list1)
displaylist(list1)
max,min=maxmin(list1)
max=print("the maximum number is:",max)
min=print("the minimum number is:",min)


