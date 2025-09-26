# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)


def bidding_result(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The Winner of this auctions is {winner} with bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your good name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    continue_bid = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if continue_bid == "no":
        continue_bidding = False
        bidding_result(bids)
    elif continue_bid == "yes":
        print("\n" * 20)
    else:
        print("Bidding crash because of typeO")
        continue_bidding = False