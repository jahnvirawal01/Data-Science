"""
                            HOUSIE

            12 tickets:

            85 65 12 5 48 62 14 8 1 74 66 15

            player 1:                       player 2:

            12 48 62 8 1 74                 85 65 5 14 66 15

1) generate 12 randon unique tickets between 1-100
2) divide 6-6 unique random tickets
3) start your game - it will give one random number e.g., 8
"""

import random
tickets = 12 * [0]
tickets1 = 12 * [0]
player1 = 6 * [0]
player2 = 6 * [0]

i = j = k =0
while i<12:
    tickets[i] = random.randint(1, 100)
    i+=1

print("The total tickets are:", *tickets[:12])

print()

tickets1 = tickets.copy()

while j<6:
    player1[j] = random.choice(tickets)
    tickets.remove(player1[j])
    j+=1
    
while k<6:
    player2[k] = random.choice(tickets)
    tickets.remove(player2[k])
    k+=1

print(f"The card for player 1 is:", *player1[:6])
print(f"The card for player 2 is:", *player2[:6])

print()

print("Let the game begin!!!")
print(input())

for i in range(13):
    choice = random.choice(tickets1)
    tickets1.remove(choice)
    print(input())
    print(f"The number is: {choice}")
    if choice in player1:
        player1.remove(choice)
        print(f"Now the card for player 1 is:", *player1)
        print(f"Now the card for player 2 is:", *player2)
        print()
    else:
        player2.remove(choice)
        print(f"Now the card for player 1 is:", *player1)
        print(f"Now the card for player 2 is:", *player2)
        print()
    
    if len(player1) == 0:
        print("Player 1 won!")
        break
    
    elif len(player2) == 0:
        print("Player 2 won!")
        break
