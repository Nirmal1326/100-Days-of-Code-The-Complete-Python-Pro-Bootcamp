year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# elif year > 1994: # Before debugging
elif year >= 1994: # After debugging
    print("You are a Gen Z.")
