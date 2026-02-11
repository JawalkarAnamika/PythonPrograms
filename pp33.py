def palindrom(num):
    i=0
    sum=0
    div=num
    while div>0:
        rem=div%10
        div=div//10
        sum=sum*10+rem
    if(sum==num):
        return True
    else:
        return False
num1=int(input("Enter a number:"))
if(palindrom(num1)):
    print("number is palindrom")
else:
    print("Number is not palindrom")