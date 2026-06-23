def cube(n):
    return(n**3)
def by_3(n):
    if n%3==0:
        return cube(n)
    else:
        return False
print(by_3(7))   
print()
def factorial(x):
   '''this is a function that calculates factorial '''
   if x==0 or x==1:
       return(1)
   else:
       return(x*factorial(x-1))
print(factorial(3))
print(factorial.__doc__)