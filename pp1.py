x=int(input("Enter the number:"))
div=x
sum=0
while div>0:
    rem=div%10
    div=div//10
    sum=sum+rem**3
if(sum==x):
    print("it is armstrong")
else:
    print("it is not armstrong")    