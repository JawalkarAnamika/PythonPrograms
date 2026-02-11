n=int(input("enter the number:"))
i=2
flag=True
while i<n:
    if n%i==0:
        flag=False
    i=i+1
if flag: 
    print("it is Prime")   
else:
    print("it is not prime")    
