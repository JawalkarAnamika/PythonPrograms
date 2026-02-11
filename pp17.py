num=int(input("enter the numbers"))
i=1
even=0
odd=0
while i<=num:
    x=int(input("Enter the number:"))
    if(x%2==0):
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("the even number is:",even)
print("the odd number is:",odd)
