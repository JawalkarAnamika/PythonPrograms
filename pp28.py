n=int(input("Enter the numbers"))
list=[]
max=0
for i in range(0,n):
    x=int(input("Enter the elenent of list:"))
    list.append(x)
print(list)
for i in list:
    if max<i:
        max=i
print(max)