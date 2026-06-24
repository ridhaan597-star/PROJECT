try:
    a = int(input("enter a number: "))
    print(a**2)
except:
    print("plz enter only numbers ")
print()
try:
    a,b =eval(input("enter 2 numbers: "))
    c=(a/b)
    print(c)
except ZeroDivisionError:
    print(" cannot divede by 0")
except SyntaxError:
    print("',' is missing")
except:
    print ("Wrong input")
else:
    print ("No exceptins")
finally:
    print ("This will execute no matter what")
print()
    