amount =int(input("plz enter the amount for withdraw"))
note_100 = amount//100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10
print("100:",note_100)
print("50:",note_50)
print("10:",note_10)


