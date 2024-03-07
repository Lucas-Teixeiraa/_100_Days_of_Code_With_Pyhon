print("Welcome to the tip calculator!")
print("------------------------------")
totalBill = float(input("What was the total bill?"))
percentPay = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
numberPeople = int(input("How many people to split the bill?"))
billResult = 0.0
if numberPeople == 5:
    percentPay = float(15 / 100)
    billResult = (totalBill - (percentPay * totalBill)) / numberPeople
    print("Each person should pay: %.2f" % billResult)
else:
    billResult = (totalBill - ((percentPay/100) * totalBill)) / numberPeople
    print("Each person should pay: $%.2f" % billResult)
