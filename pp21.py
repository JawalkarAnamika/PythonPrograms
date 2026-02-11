num=int(input("Enter the number"))
sum=0
div=num
while div>0:
    rem=div%10
    div=div//10
    sum=sum+rem**3
if sum==num:
    print("The number",num,"is Armstrong")
else:
    print("The number",num,"is not Armstrong")