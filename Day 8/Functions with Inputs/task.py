def greet():
    print("Who are you ?")
    print("I'm Lucifer")
    print("The Devil 😈!!!!\nExactly!!!!!")
greet()

def greet_with_name(name):
    print("Who are you ?")
    print(f"I'm {name}")
    print("The Devil 😈!!!!\nExactly!!!!!")

greet_with_name("Nirmal")


def life_in_weeks(age):
    if age < 0 or age > 90:
        print("Please enter a valid age between 0 and 90.")
        return

    total_weeks = 90 * 52
    weeks_done = age * 52
    weeks_left = total_weeks - weeks_done
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(int(input("What is your age? ")))