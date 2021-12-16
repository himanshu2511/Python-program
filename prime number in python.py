a=int(input("Enter a number : "))
k=0
if (a==0) or (a==1):
    k=1
else:
    i=2
    
    while(i<a):
        if a%i==0:
            k=k+1
        i=i+1
if k==0:
    print("prime")
else:
    print("not prime")
