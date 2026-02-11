x=int(input("Enter the term of fibonacci:"))
a=0
b=1
i=3
print(a)
print(b)
while i<=x:
    fib=a+b
    print(fib) 
    a=b
    b=fib
    i=i+1