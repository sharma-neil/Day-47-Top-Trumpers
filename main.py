import os, time, random

trumps = {}

#using default values from solution to get started with some
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

def create_card():
  while True:
    build = input("Do you want to build a card: (y/n)")
    if build == "y":
        name = input("Name: ")
        intelligence = int(input("Intelligence: "))
        speed = int(input("Speed: "))
        guile = int(input("Guile: "))
        baldness = int(input("Baldness Level: "))
        trumps[name] = {"Intelligence": intelligence, "Speed": speed, "Guile": guile, "Baldness Level": baldness}
    else:
        print("Very well! Let's continue\n")
        break


def user_choices():
    for key in trumps:
        print(key)
    print("")
    card_choice = input("Choose your card: ")
    while card_choice not in trumps.keys():
        card_choice = input("Choose your card: ")
        print("")
    card_key = trumps[card_choice]   
    return card_choice, card_key

def user_stat_choice(card_key):
    for key in card_key:
        print(key)
    print("")
    statchoice = input("Choose a stat to battle: ")
    while statchoice not in card_key:
        statchoice = input("Choose a stat to battle: ")  
        print("")
    return statchoice

while True:
    
    q_1_or_2 = input("Do you want to play 1 or 2 player? (1/2) or enter any other key to exit: ")
    print("")
    
    if q_1_or_2 == "1":
        create_card()
        
        p1_choice, p1_key = user_choices()
        p1_stat = user_stat_choice(p1_key)
        comp_choice = random.choice(list(trumps.keys()))

        p1_stat_value = trumps[p1_choice][p1_stat]
        comp_stat_value = trumps[comp_choice][p1_stat]
        
        print(f"\n{p1_choice} has a {p1_stat} of {p1_stat_value}")
        print(f"{comp_choice} has a {p1_stat} of {comp_stat_value}\n")
        
        if p1_stat_value > comp_stat_value:
            print(f"Player 1: {p1_choice} wins")
        elif comp_stat_value > p1_stat_value:
            print(f"Computer: {comp_choice} wins")
        else:
            print(f"It's a tie!")
    elif q_1_or_2 == "2":
        q_build_card = ""
        create_card(q_build_card)
        
        p1_choice, p1_key = user_choices()
        p2_choice, p2_key = user_choices()
        stat = user_stat_choice(p1_key)

        p1_stat_value = trumps[p1_choice][stat]
        p2_stat_value = trumps[p2_choice][stat]
        
        print(f"\n{p1_choice} has a {stat} of {p1_stat_value}")
        print(f"{p2_choice} has a {stat} of {p2_stat_value}\n")
        
        if p1_stat_value > p2_stat_value:
            print(f"Player 1: {p1_choice} wins")
        elif p2_stat_value > p1_stat_value:
            print(f"Player 2: {p2_stat_value} wins")
        else:
            print(f"It's a tie!")
    else:
        exit()
