n=int(input("Enter the number:"))
div=n
sum=0
while div>0:
    rem=div%10
    div=div//10
    sum=sum*10+rem
if sum==n:
    print("The number",n,"is palindrom")
else:
    print("The number",n,"is not palindrom")

