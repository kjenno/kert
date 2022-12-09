import random

monster_hp = 25
strength = 5
ac = 15
hp = 25
combat = True
current_hp = monster_hp
dmg = 0
hit = False

def roll_to_hit(ac):
    hit = random.randint(1, 20)
    if hit >= ac:
        return True
    return False


def roll_4_dmg(strength):
    dmg = random.randint(1, 10) + strength
    print(f"You hit and did {dmg} damage.")
    return dmg

def damage(monster_hp, dmg):
    current_hp = monster_hp - dmg
    return current_hp

while current_hp > 0:
    inp = input(r" santa has appeared what will you do? ")
    if(inp == "attack"):
        if(roll_to_hit(ac)):
            damage_done = roll_4_dmg(strength)
            current_hp = damage(current_hp, damage_done)
        else:
            print("You missed!")
    if(inp == "dodge"):
        print("you dodged santa's attack")
    if(inp == "run"):
        print("you ran away")
print("You have slain santa!")