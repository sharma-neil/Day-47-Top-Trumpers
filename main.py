import os, time, random

trumps = {}

#using default values from solution to get started with some
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

def create_card(build):
  while build != "y" and build != "n":
    build = input(f"Do you want to build your own card? (y/n) ")
    if build == "y":
      name = input("Name: ")
      intelligence = int(input("Intelligence: "))
      speed = int(input("Speed: "))
      guile = int(input("Guile: "))
      baldness = int(input("Baldness Level: "))

      trumps[name] = {"Intelligence": intelligence, "Speed": speed, "Guile": guile, "Baldness Level": baldness}
    else:
      print("Very Well! Let's get started!\n")

def user_choices():
    for key in trumps:
        print(key)
    card_choice = input("Choose your card: ")
    while card_choice not in trumps.keys():
        card_choice = input("Choose your card: ")
    card_key = trumps[card_choice]
    
    return card_choice, card_key

def user_stat_choice(card_key):
    for key in card_key:
        print(key)
    statchoice = input("Choose a stat to battle: ")
    while statchoice not in card_key:
        statchoice = input("Choosea a stat to battle: ")
    
    return statchoice

while True:
    q_build_card = ""
    create_card(q_build_card)
    
    q_1_or_2 = int(input("Do you want to play 1 or 2 player? (1/2) > "))
    while q_1_or_2 != 1 and q_1_or_2 != 2:
        q_1_or_2 = int(input("Do you want to play 1 or 2 player? (1/2) > "))
    
    if q_1_or_2 == 1:
        p1_choice, p1_key = user_choices()
        p1_stat = user_stat_choice(p1_key)
        comp_choice = random.choice(list(trumps.keys()))

        print(f"{p1_choice} has a {p1_stat} of {trumps[p1_choice][p1_stat]}")
        print(f"{comp_choice} has a {p1_stat} of {trumps[comp_choice][p1_stat]}")
