n=int(input("Enter the numbers"))
list1=[]
list2=[]
max=0
for i in range(0,n):
    x=int(input("Enter the element of list:"))
    list1.append(x)
print(list1)
for k in list1:
    if k not in list2:
        list2.append(k)
print(list2)
