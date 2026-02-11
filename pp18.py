n=int(input("Enter the number "))
div=n
sum=0
while div>0:
    rem=div%10
    div=div//10
    sum=sum+rem
print("The sum of digits is:",sum)
