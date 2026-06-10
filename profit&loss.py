sp = int(input("enter your selling  price: "))
cp = int(input("enter your cost price: "))
x =sp-cp
if x > 0:
    print("profit: ",x)
else :
    print("loss: ",abs(x))
