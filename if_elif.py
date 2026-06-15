a = input("Do u have a medical cause?").upper()
if (a=="YES"):
    print ("allowede")
else:
    b = int(input("attendense ?"))
    if (b>=75):
        print("allowed")
    else:
        print("not allowed")
