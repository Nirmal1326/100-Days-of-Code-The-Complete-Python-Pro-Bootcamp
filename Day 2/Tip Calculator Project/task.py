print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
print(tip_percent)
total_tip_amount = 100 * tip_percent
print(total_tip_amount)
total_bill = bill + total_tip_amount
print(total_bill)
bill_per_person = total_bill / people
print(bill_per_person)
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")