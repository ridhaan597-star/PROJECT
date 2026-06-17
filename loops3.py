n = int(input("enter the numbers of terms: "))
sum=0
i=1
while i<=n:
    sum=i+sum
    i=i+1
print(sum)


num = int(input("enter the numbers of terms: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=digit**3+sum
    temp=temp//10
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")