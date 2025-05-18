print("Welcome to Python Pizza Deliveries!")
bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza
else:
    print("You have chosen an invalid size.")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    if size == "M" or size == "L":
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")


