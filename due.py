def calculate_change(bill, paid):
    return paid - bill

bill = float(input("Enter bill amount: "))
paid = float(input("Enter amount paid: "))

print("Change =", calculate_change(bill, paid))