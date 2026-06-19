n = int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() 




rows = int(input("enter a number: "))
n = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n = n+1
    print()

