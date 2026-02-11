def sumdigit(num):
    i=0
    sum=0
    div=num
    while div>0:
        rem=div%10
        div=div//10
        sum=sum+rem
    print(sum)
num=int(input("Enter a number:"))
sumdigit(num)