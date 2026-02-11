#display number in words
x=int(input("Enter the number:"))
div=x
sum=0
while div>0:
    rem=div%10
    div=div//10
    sum=sum*10+rem
print("sum=",sum)
while sum>0:
    rem=sum%10
    sum=sum//10
    if rem==0:
        print("zero")
    elif rem==1:
        print("One")
    elif rem==2:
        print("Two")        
    elif rem==3:
        print("Three")        
    elif rem==4:
        print("Four")        
    elif rem==5:
        print("five")        
    elif rem==6:
        print("six")        
    elif rem==7:
        print("Seven")        
    elif rem==8:
        print("Eight")        
    elif rem==9:
        print("Nine")        

