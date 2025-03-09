import random
import time
import sys

bust = True
Found = True
card_keys = []
card_values = []
dealer_total = 0
players_total = 0
money = 50

def loading_animation(): #Loading animations for the dealer
    for _ in range(2):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r🎲- Dealer is drawing his cards{dots} ")
            sys.stdout.flush()
            time.sleep(0.5)

def cards(): #cards dictionary/list
    global card_keys
    global card_values

    cards = {
        "Ace": 11,
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2,
        "One": 1
    }

    card_keys = list(cards.keys())
    card_values = list(cards.values())

def game(): #blackjack game logic
    global player_total
    global dealer_total
    global bust
    global money

    Found = True
    bust = True
    player_total = 0
    dealer_total = 0

    draw1 = random.randint(0, 12) #dealers first draw
    draw2 = random.randint(0, 12) #players first draw
    draw3 = random.randint(0, 12) #players second draw
    draw4 = random.randint(0, 12) #players hits
    draw5 = random.randint(0, 12) #dealers hits

    print("♥️ Welcome to BlackJack!🃏") #intro 
    print("")
    loading_animation()
#Dealer drawing
    print("")
    print(f"The Dealer drew:", card_keys[draw1])
    dealer_total += card_values[draw1]
    print("🃏 Dealers total:", dealer_total,"🃏")
    print("------------------------------------------------")

    print(f"You bet $10. Your current money is ${money}")
    print("You drew:", card_keys[draw2], "and", card_keys[draw3])
    player_total = int(card_values[draw2]) + int(card_values[draw3])

    print(f"Your current total:", player_total)
    while Found:
        #hit or stand
        anwser = input("Would you like to Hit or Stand?(H/S): ").capitalize()
        if anwser == "H":
            draw4 = random.choice(card_values) #drawing random cards

            print("You drew:", card_values[draw4])
            player_total = player_total + int(card_values[draw4])

            if player_total == 21:
                print("Congratulations! You hit 21! 🎊")
                anwser = "S" #automatically stands for the player

            elif player_total < 21:
                 print("Your current total:", player_total)

            else:
                print("You bust!")
                print("Your current total was:", player_total)
                Found = False
                bust = False
            
        elif anwser == "S":

            print("Your current total is:", player_total)
            print("------------------------------------------------")

            while dealer_total < player_total and dealer_total < 21: #dealers hitting logic
                loading_animation()
                draw5 = random.choice(card_values)

                print("The Dealer drew:", card_keys[draw5])
                dealer_total += card_values[draw5]
                print("🃏 Dealers total:", dealer_total,"🃏")
                print("------------------------------------------------")
                if dealer_total < player_total or dealer_total < 21:
                    Found = False

        else:
            print("Please input H for Hit or, S for Stand")

#winning function
def winner():
    global dealer_total, player_total, bust
    global money

    if dealer_total == player_total:
        print("It's a draw! You won 0$")
    elif not bust:  # Player bust
        print("The Dealer wins. You lost -10$.")
    elif dealer_total > 21:
        print("You win! The Dealer busts. You won +10$")
        money += 10
    elif dealer_total > player_total:
        print("The Dealer wins. You lost.")
    else:
        print("You win! You won 10$")
        money += 10

while Found:
    cards()
    if money == 0:
        print("If your a brokie, just says so! You don't have enough to bet")
        exit()
    elif money != 0:
        money -= 10
    game()
    winner()
    anwser = input("Would you like to play again?(Y/N) ").capitalize()
    if anwser == "N":
        print(f"Thank you for playing! Your total currency was: ${money}")
        Found = False
    elif anwser == "Y":
        Found = True
    else:
        print("Your input is wrong, press Y for yes, N for No")