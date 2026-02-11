income=int(input("enter the Income:"))
if(income<1200000):
    print("No Tax")
elif(income>1200000 and income<1500000):
    tax=income*10/100
elif(income>1500000 and income<2000000):
    tax=income*20/100
elif(income>2000000):
    tax=income*30/100
print("Your Income is:",income,"And Tax is",tax)    
       
