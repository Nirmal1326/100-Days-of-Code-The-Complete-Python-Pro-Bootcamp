import art

# Calculation function
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

# User interaction
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    print(art.logo)
    calci_continue = True
    num1 = float(input("What is the first number?: "))

    while calci_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            calci_continue = False
            print("\n" * 20)
            calculator()

calculator()