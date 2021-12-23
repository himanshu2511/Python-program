item=int(input("Enter the number of item you purchase: "))
a=0
for i in range(item):
    item_list=int(input("Enter the amount of item: "))
    a=a+item_list
print(a)
if a>=8000:
    discount=a*(30/100)
    balance=a-discount
    print("thank you for Coming your bill with 30% discount: ",balance)
else:
    print("thank you for Coming your bill",a)
