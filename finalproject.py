n = input("Woud you like to play blackjack today, my good sir?")

#starting the game off by being polite
#if someone doesn't give one of the responses it will hoppefully make fun of them until they respond normally.

if n == "Yes":
    print("Excellent, please take a seat. Prepare to get smacked")
elif n == "yes":
    print("Excellent, please take a seat. Prepare to get smacked.")
elif n == "yea":
    print("Excellent, please take a seat. Prepare to get smacked.")
elif n == "no":
    print("Well then why are even in my casino?")
elif n == "nah":
    print("Well then why are even in my casino?")
else:
    print("What are you even saying?")

#I have a lot of answers so that every response hopefully triggers something
#It always ends up with you playing, though. Even if the user inputs "no" as a response to both questions cards will be dealt.

m = input("Hate to break it to you sir, but there is no gambling here, due to the UCVTS student handbook. Are you ready to play?")

#Just in case anyone was wondering if there is money involved

if m == "Yes":
    print("Excellent I will deal your cards.")
elif m == "yes":
    print("Excellent I will deal your cards.")
elif m == "yea":
    print("Excellent I will deal your cards.")
elif m == "No":
    print("I don't really care here are your cards.")
elif m == "no":
    print("I don't really care here are your cards.")
else:
    print("These annoying responses are really getting on my nerves.")

#no matter what the game will be played

#a while loop was created for the lists of faces, cards, and suits

while True:
    import random

    faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    faces_string = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    #this list is naming all the numbers and faces of cards

    suits = [1, 2, 3, 4]

    suits_string = ["Spades", "Hearts", "Clubs", "Diamonds"]

    #this list gives all the types of cards

#I defined a function to print the cards the player or dealer is dealt
#This function will give the face and suit of every card

    def create_cards():
        cards = []
        for face in range(len(faces)):
            for suit in range(len(suits)):
                cards.append([suits[suit], faces[face],"%s of %s" % (faces_string[face], suits_string[suit])])
        return cards

#This function is to play with the value of the ace so it benefits the player the most
#At first it counts the ace as an 11, but if you go over 21 it will count the ace as a 1

    def score_hand(hand):
        score = 0
        aces = 0
        for card in hand:
            if card[1] == 1:
                score += 11
                aces += 1
            else:
                score += card[1]

        while score > 21 and aces > 0:
            score -= 10
        return score

#this function will tell you what cards you were dealt and there values added together

    def display_hand(hand):
        out = ""
        for card in hand:
            out += card[-1] + '\n'

        out += "-------------\n"
        out += "Score: %s" % score_hand(hand)
        return out

#defining a function to take the top card

    def take_top_card():
        c = cards[0]
        cards.pop(0)
        return c

#this function will adjust the value from the other card you get
#this uses the take top card function to get a new card and add the value from that card to your hand

    def create_opening_hand():
        hand = []
        hand.append(take_top_card())
        hand.append(take_top_card())
        return hand

    cards = create_cards()

    random.shuffle(cards)

    hand = create_opening_hand()

    #created a while loop

    while True:
        #this will print your score
        print(display_hand(hand))
        #if your score is greater than 21 it will print "you busted"
        if score_hand(hand) > 21:
            print("You busted!")
            exit()
        #this allows there to be an option of hit or stay
        #if you hit then you get another card
        #if you stick you keep the same cards and value you have now
        print("\nHit: 1\nStay: 2")
        hs = int(input("Enter option: "))
        print("\n")
        if hs == 1:
            hand.append(take_top_card())
        else:
            break


#this set of lines will deal with the automatic hands for the dealer

    dealer = create_opening_hand()
    while True:
        #if the dealer's score is lower than 17 the dealer will hit
        if score_hand(dealer) < 17:
            dealer.append(take_top_card())
            #if the score of the dealer is more than 21 it will print he busted and you will win.
            if score_hand(dealer) > 21:
                print("Dealer Busted. You won!")
                break
        else:
            break

#this will print the dealer's cards and respective value

    print('\n')
    print("Dealer's hand:")
    print(display_hand(dealer))

#this will print your hand with the value from the cards

    print('\n')
    print("Your hand:")
    print(display_hand(hand))

#this will just compare your score and the dealer's
#it will print the results if you win, lose, or tie

    if score_hand(hand) > score_hand(dealer):
        print("You won!")
    elif score_hand(hand) == score_hand(dealer):
        print("You tied... and tie goes to the dealer")
    else:
        print("You lost!")

#this code will continue to run until you bust in a game
#and that's a good game of blackjack