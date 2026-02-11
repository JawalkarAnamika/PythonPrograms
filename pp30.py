n=int(input("Enter a number"))
div=n
mylist=[]
i=0
while div>0:
    rem=div%2
    div=div//2
    mylist.append(rem)
    i=i+1
mylist.reverse()
print("The binary number is:",mylist)
