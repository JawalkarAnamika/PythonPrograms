n=int(input("Enter the number:"))
div=n
sum=0
while div>0:
    rem=div%10
    div=div//10
    sum=sum*10+rem
print("The reverse number is:",sum)