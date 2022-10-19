    # 9.1

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] <= 100:
        student_grades[key] = "Outstanding"

print(student_grades)

    # 9.2

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_visited,times_visited,cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

    # 9.3 - Challenge - Auction Bid

from replit import clear
from logo2 import logo

auction = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_price = bidding_record[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    bidder_name = input("What's your name? ")
    bid_ammount = float(input("Put your bid here: $"))
    auction[bidder_name] = bid_ammount
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(auction)
    elif should_continue == "yes":
        clear()