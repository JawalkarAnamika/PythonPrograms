n=int(input("Enter the number:"))
sum=0
div=n
while div>0:
    rem=div%10
    div=div//10
    sum=sum*10+rem
while sum>0:
    rem=sum%10
    sum=sum//10
    if rem==0:
      print("Zero")
    elif rem==1:
      print("One")
    elif rem==2:
      print("Two")
    elif rem==3:
      print("Three")
    elif rem==4:
      print("Four")
    elif rem==5:
      print("Five")
    elif rem==6:
      print("Six")
    elif rem==7:
      print("Seven")
    elif rem==8:
      print("Eight")
    elif rem==9:
     print("Nine")

