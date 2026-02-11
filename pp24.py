#without using thirs variable
"""print("Before Swapping:")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
a=a+b
b=a-b
a=a-b
print("after Swapping:")
print(a)
print(b)"""
#Using third variable:
print("Before Swapping:")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
temp=a
a=b
b=temp
print("after Swapping:")
print(a)
print(b) 
    
