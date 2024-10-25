players = {}
bidder_name = ""
bidder_value = 0
next_bidder = "yes"

def bid_function(name, value):
    name = input("Insert your name: ")
    value = input("Insert your bid: €")
    players[name] = value

while next_bidder == "yes" or next_bidder == "y":
    bid_function(bidder_name, bidder_value)
    next_bidder = input("Is there another bidder? If so, type yes. If not, type no.\n").lower()
    if next_bidder == "yes" or next_bidder == "y":
        print("\n" * 100)

max_value = 0
winner = ""
for bid in players:
    x = int(players[bid])
    if x > max_value:
        max_value = x
        winner = bid

print(f"{winner} has the highest bid: {max_value}€")
print(players)