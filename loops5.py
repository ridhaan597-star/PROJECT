lower = int(input("enter the 1 number: "))
upper = int(input("enter the 2 number: "))
count = 1 
print ("range: ",lower,upper)
for num in range (lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(f"{count})  {num}")
            count += 1

