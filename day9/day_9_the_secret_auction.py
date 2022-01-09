from typing import Dict, List
from replit import clear

logo = '''
         ___________
         \         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-'
          )"""""""(
         /_________\\
       .-------------.
      /_______________\\
'''


def find_highest_bidder(auction_bids_dict):
    highest_bid_amount = 0
    highest_bid_name = ''

    for bidder in auction_bids_dict:
        if auction_bids_dict[bidder] > highest_bid_amount:
            highest_bid_amount = auction_bids_dict[bidder]
            highest_bid_name = bidder

    print(
        f"\nCongratulations!!!\nThe winner is {highest_bid_name} with a "
        f"bid of ${highest_bid_amount}."
    )


should_continue = True
auction_bids: Dict = {}
clear()
print(logo)
print('Welcome to the secret auction program!!!')

while should_continue:
    # clear() # Uncomment here to clean the display before pass
    #           to the next bidder

    name = input("\nWhat is your name?: ")
    bid_value = int(input("What's your bid? $"))

    auction_bids[name] = bid_value

    should_continue_input = input(
        "\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue_input == 'no':
        should_continue = False
        find_highest_bidder(auction_bids)
