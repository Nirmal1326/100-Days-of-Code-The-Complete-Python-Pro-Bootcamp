# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with_name(name = "Nirmal", location = "Koomapatti")


def calculate_love_score(name1, name2):
    love = 0
    true = 0
    pair = (name1 + name2).upper()
    for count in pair.upper():
        if count in "TRUE":
            true += 1

    for count in pair.upper() :
        if count in "LOVE":
            love += 1

    print(f"{true}{love}")

calculate_love_score("Kanye West", "Kim Kardashian")