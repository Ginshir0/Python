from art import logo
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    user_cards = []
    computer_cards = []
    game_over = False
    user_score = 0
    computer_score = 0


    for user_card in range(2):
        user_cards.append(cards[random.randint(1, 13)-1])
        user_score += user_cards[-1]
    for computer_card in range(2):
        computer_cards.append(cards[random.randint(1, 13)-1])
        computer_score += computer_cards[-1]
        
    print(logo)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score != 21:
        while not game_over:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get_card == "y" and not game_over:
                user_cards.append(cards[random.randint(1, 13) - 1])
                user_score += user_cards[-1]
                print(f"\nYour cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            if sum(user_cards) > 21:
                game_over = True
            if get_card == "n" or game_over:
                while computer_score < 17:
                    computer_cards.append(cards[random.randint(1, 13) - 1])
                    computer_score += computer_cards[-1]
                print(f"\nYour final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                game_over = True
        if user_score > 21:
            print("You went over. You lose 😭")
        elif computer_score > 21:
            print("Opponent went over. You win 😁")
        elif user_score == computer_score:
            print("Draw 🙃")
        elif user_score > computer_score:
            print("You win 😃")
        elif user_score < computer_score:
            print("You lose 😤")
    
        replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if replay == "y":
            blackjack()
    else:
        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Win with a Blackjack 😎")
        replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if replay == "y":
            blackjack()
            
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == "y":
    blackjack()