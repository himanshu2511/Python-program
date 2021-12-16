
print("1. Area of reactangle : ")
print("2. Area of square : ")
print("3. Area of circle : ")

choice=int(input("CHOICE NO. : "))
if choice==1:
    a=int(input("Lenth : "))
    b=int(input("Breath : "))
    reactangle=(a*b)
    print("Area of reactangle : ",reactangle)

elif choice==2:
    c=int(input("Circle"))
    circle=c*c
    print("Area of circle : ",circle)
elif choice==3:
    d=int(input("Radius"))
    radius=(3.14*d**2)
    print("Area of cirlce : ",radius)
