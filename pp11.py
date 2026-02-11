m1=int(input("Enter the marks of first subject:"))
m2=int(input("Enter the marks of second subject:"))
m3=int(input("Enter the marks of third subject:"))
per=(m1+m2+m3)/3
if(per<40):
    print("Fail")
elif(per<40 and per>50):
    print("You pass with C grade")
elif(per<50 and per>55):
    print("You pass with B grade")
elif(per<55 and per>60):
    print("You pass with B+ grade")
elif(per>60):
    print("You pass with A grade")

