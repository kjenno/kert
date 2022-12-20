import time
import random


elf_hp = 25
kerst_hp = 50
sneeuw_hp = 50
kerst_hp2 = 50
sneeuwpop_hp = 15
reindeer_hp = 100
sneeuwman_hp = 15
hero_hp = 100

current_hp1 = elf_hp
current_hp2 = kerst_hp
current_hp3 = sneeuw_hp
current_hp4 = kerst_hp2
current_hp5 = sneeuwpop_hp
current_hp6 = reindeer_hp
current_hp7 = sneeuwman_hp
current_hp8 = hero_hp
healing = 25
strength = 5
ac = 15

combat = True

dmg = 0
hit = False

def roll_to_hit(ac):
    hit = random.randint(1, 20)
    if hit <= ac:
        return True
    return False

def roll_4_dmg(strength):
    dmg = random.randint(1, 10) + strength
    print(f"You hit and did {dmg} damage.")
    return dmg

def roll_4_dmgh(strength):
    dmgh = random.randint(1, 10) + 2
    print(f"You got hit and took {dmgh} damage.")
    return dmgh

def damage_elf(elf_hp, dmg):
    current_hp1 = elf_hp - dmg
    return current_hp1

def damage_kerst(kerst_hp, dmg):
    current_hp2 = kerst_hp - dmg
    return current_hp2

def damage_sneeuw(sneeuw_hp, dmg):
    current_hp3 = sneeuw_hp - dmg
    return current_hp3

def damage_kerst2(kerst2_hp, dmg):
    current_hp4 = kerst2_hp - dmg
    return current_hp4

def damage_sneeuwpop(sneeuwpop_hp, dmg):
    current_hp5 = sneeuwpop_hp - dmg
    return current_hp5

def damage_reindeer(reindeer_hp, dmg):
    current_hp6 = reindeer_hp - dmg
    return current_hp6

def damage_sneeuwman(sneeuwman_hp, dmg):
    current_hp7 = sneeuwman_hp - dmg
    return current_hp7

def damage_hero(hero_hp, dmgh):
    current_hp8 = hero_hp - dmgh
    return current_hp8

def heal(current_hp8, healing, hero_hp):
    if current_hp8 < hero_hp:
        if current_hp8 <= hero_hp - healing:
            current_hp8 = current_hp8 + healing
            print("you healed and got your hp up to",current_hp8)
            return current_hp8
        if current_hp8 > hero_hp - healing:
            current_hp8 =  hero_hp
            print("you healed and got your hp up to",current_hp8)
            return current_hp8
    if current_hp8 == hero_hp:
        print("you already have full hp")
def game_over():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀  """)
    exit()

def hp_check(current_hp8):
    if current_hp8 <= 0:
        game_over()
    else:
        return



print("It’s a late Christmas night, you’re downstairs in front of the television, you think it’s time to go to bed so you head upstairs and go to sleep.")
time.sleep(4)
print("Suddenly you hear a loud knock on the door, you look through the window but you can’t recognize the person in front of the door.")
time.sleep(3)
print("[ Do you open the door ] [open] or  [ Do you go to sleep? ] [sleep]")
option1 = input()
if option1 == ("sleep"):
    print("It didn’t even feel like you went to sleep, but you’re definitely not in your bed anymore you’re in a playground and it’s snowy. ")
    time.sleep(6)
    print("You see a reindeer who asks for your help, the big Christmas tree has been stolen by the elves, you have to find someone who knows about where the Christmas tree went")
    time.sleep(6)
    print("After searching you find a snowman he tells you that the Christmas tree has been taken to the factory to burn it.")
    time.sleep(6)
    print("There are two elf guards waiting for you at the gate of the factory.")
    time.sleep(3)
    print("[Try to talk it out] [talk] or [Fight your way in] [fight]")
    option2 = input()
    if option2 == ("talk"):
        print("You talk it out and due to your charisma you managed to get in without harming anyone")
    if option2 == ("fight"):
        while current_hp1 > 0:
            inp = input(r"you decide to fight what will you do?[attack][heal][run]:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    current_hp1 = damage_elf(current_hp1, damage_done)
                else:
                    print("You missed!")
                damage_doneh = roll_4_dmgh(10)
                current_hp8 = damage_hero(current_hp8, damage_doneh)
                hp_check(current_hp8)
                time.sleep(1)
                print("you have",current_hp8, "hp left")
                time.sleep(1)
            if(inp == "heal"):
                current_hp8 = heal(current_hp8, healing, hero_hp)
            if(inp == "run"):
                game_over()
            else:
                print("wrong input")
        print("You have beaten the elves!")
    time.sleep(3)
    print("You see the big glowing Christmas tree and think it’s time to take it home")
    time.sleep(3)
    print("Ho ho ho looks like someone is trying to take our Christmas tree home.")
    time.sleep(3)
    print("Santa comes down to attack you and you start to fight")
    while current_hp2 > 0:
            inp = input(r" santa has appeared what will you do?[attack][heal][run]:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    current_hp2 = damage_kerst(current_hp2, damage_done)
                else:
                    print("You missed!")
                damage_doneh = roll_4_dmgh(10)
                current_hp8 = damage_hero(current_hp8, damage_doneh)
                hp_check(current_hp8)
                time.sleep(1)
                print("you have",current_hp8, "hp left")
                time.sleep(1)
            if(inp == "heal"):
                current_hp8 = heal(current_hp8, healing, hero_hp)
            if(inp == "run"):
                print("you ran away")
                game_over()
    print("You beat santa!")
    time.sleep(2)
    print("you take the Christmas tree home but, you wake up, this time for real. You’re home and it doesn’t feel like a dream anymore")
if option1 == ("open"):
    print("you open the door")
    time.sleep(1)
    print("he tells you Santa’s snowmen have gone rogue against him and he needs your help!")
    time.sleep(4)
    print("You follow the elf to a big forest with huge trees but a huge snowstorm makes you lose the small elf")
    time.sleep(4)
    print("Now you’re all alone but you feel that someone is behind you, so you say : “He’s right behind me isn’t he.”")
    time.sleep(5)
    print("You gulp and slowly turn your head")
    time.sleep(1)
    print(" It’s the snowman captain.")
    while current_hp3 > 0:
            inp = input(r" the snowman captain has appeared what will you do?[attack][heal][run]:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    current_hp3 = damage_sneeuw(current_hp3, damage_done)
                else:
                    print("You missed!")
                damage_doneh = roll_4_dmgh(10)
                current_hp8 = damage_hero(current_hp8, damage_doneh)
                hp_check(current_hp8)
                time.sleep(1)
                print("you have",current_hp8, "hp left")
                time.sleep(1)
            if(inp == "heal"):
                current_hp8 = heal(current_hp8, healing, hero_hp)
            if(inp == "run"):
                print("you ran away")
                game_over()
    print("You beat the snowman captain!")
    time.sleep(2)
    print("the snowstorm stops")
    time.sleep(2)
    print("you see black smoke coming from the distance so you choose to follow it.")
    time.sleep(3)
    print("While on your way there you see a man with a cloak covering his whole face and a candy cane walking stick.")
    time.sleep(4)
    print("You ask him if he caused the smoke and he takes off his cloak, it’s the fired Santa,")
    time.sleep(5)
    print("he has been fired from the factory a long time ago and is looking for revenge.")
    time.sleep(5)
    option3 = input("what will you do[talk] [ attack]")
    if option3 == ("talk"):
        print("You talk it out, luckily you have worked on your charisma and he accepts your offer to let you go help Santa at the factory you continue.")
    if option3 == ("attack"):
        while current_hp4 > 0:
            inp = input(r" santa got mad what will you do?[attack][heal][run]:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    current_hp4 = damage_kerst2(current_hp4, damage_done)
                else:
                    print("You missed!")
                damage_doneh = roll_4_dmgh(10)
                current_hp8 = damage_hero(current_hp8, damage_doneh)
                hp_check(current_hp8)
                time.sleep(1)
                print("you have",current_hp8, "hp left")
                time.sleep(1)
            if(inp == "heal"):
                current_hp8 = heal(current_hp8, healing, hero_hp)
            if(inp == "run"):
                print("you ran away")
                game_over()
        print("You beat santa and continue")
        time.sleep(2)
        print("You reach Santa’s factory there is fire everywhere, there are 10 snowman guards ready to hold you back.")
        option4 = input("what will you do[fight][go home]")
        if option4 ==("fight"):
            while current_hp5 > 0:
                inp = input(r" the guards got mad what will you do?[attack][heal][run]:  ")
                if(inp == "attack"):
                    if(roll_to_hit(ac)):
                        damage_done = roll_4_dmg(strength)
                        current_hp5 = damage_sneeuwpop(current_hp5, damage_done)
                    else:
                        print("You missed!")
                    damage_doneh = roll_4_dmgh(10)
                    current_hp8 = damage_hero(current_hp8, damage_doneh)
                    hp_check(current_hp8)
                    time.sleep(1)
                    print("you have",current_hp8, "hp left")
                    time.sleep(1)
                if(inp == "heal"):
                    current_hp8 = heal(current_hp8, healing, hero_hp)
                if(inp == "run"):
                    print("you ran away")
                    game_over()
            print("You beat the guards and continue")
            time.sleep(3)
            print("you get to Santa’s office and find out he is being held hostage by one of his reindeers")
            time.sleep(2)
            print(" your only option is to fight the reindeer.")
            time.sleep(3)
            while current_hp6 > 0:
                inp = input(r" what will you do?[attack][heal][run]:  ")
                if(inp == "attack"):
                    if(roll_to_hit(ac)):
                        damage_done = roll_4_dmg(strength)
                        current_hp6 = damage_reindeer(current_hp6, damage_done)
                    else:
                        print("You missed!")
                    damage_doneh = roll_4_dmgh(10)
                    current_hp8 = damage_hero(current_hp8, damage_doneh)
                    hp_check(current_hp8)
                    time.sleep(1)
                    print("you have",current_hp8, "hp left")
                    time.sleep(1)
                if(inp == "heal"):
                    current_hp8 = heal(current_hp8, healing, hero_hp)
                if(inp == "run"):
                    print("you ran away")
                    game_over()
            print("You beat the reindeer and continue")
            time.sleep(2)
            print("you get to Santa and save him, you saved Christmas! But then. You wake up and realise everything was a dream.")
        if option4 == ("Go home"):
            print("you go home")
            print("you find some snowman along the way and find ")
            while current_hp7 > 0:
                inp = input(r" what will you do?[attack][heal][run]:  ")
                if(inp == "attack"):
                    if(roll_to_hit(ac)):
                        damage_done = roll_4_dmg(strength)
                        current_hp7 = damage_sneeuwman(current_hp7, damage_done)
                    else:
                        print("You missed!")
                    damage_doneh = roll_4_dmgh(10)
                    current_hp8 = damage_hero(current_hp8, damage_doneh)
                    hp_check(current_hp8)
                    time.sleep(1)
                    print("you have",current_hp8, "hp left")
                    time.sleep(1)
                if(inp == "heal"):
                    current_hp8 = heal(current_hp8, healing, hero_hp)
                if(inp == "run"):
                    print("you ran away")
                    game_over()
            print("You beat the snowman's and go home")

