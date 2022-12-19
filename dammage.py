import time
import random

elf_hp = 250
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
strength = 5
healing = 25
ac = 0

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
    dmgh = random.randint(1, 10) + 10
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
def hp_check(current_hp8):
    if current_hp8 <= 0:
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
    else:
        return

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









while current_hp1 > 0:
    inp = input(r"you decide to fight what will you do?[attack][heal][run]  ")
    if(inp == "attack"):
        if(roll_to_hit(ac)):
            damage_done = roll_4_dmg(strength)
            current_hp1 = damage_elf(current_hp1, damage_done)
        else:
            print("You missed!")
        time.sleep(1)
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
print("You have beaten the elves!")






