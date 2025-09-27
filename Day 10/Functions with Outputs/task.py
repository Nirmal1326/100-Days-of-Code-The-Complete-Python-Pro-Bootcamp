def format_name(first, last):
    formated_fist = first.title()
    formated_last = last.title()
    return f"{formated_fist} {formated_last}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

print(format_name(f_name, l_name))

def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)
