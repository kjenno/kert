import time
import random

elf_hp = 25
kerst_hp = 50
hero_hp =30
current_hp1 = elf_hp
current_hp2 = kerst_hp
strength = 5
ac = 15
hp = 25
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

def damage_elf(elf_hp, dmg):
    current_hp1 = elf_hp - dmg
    return current_hp1

def damage_kerst(kerst_hp, dmg):
    current_hp2 = kerst_hp - dmg
    return current_hp2



print("It’s a late Christmas night, you’re downstairs in front of the television, you think it’s time to go to bed so you head upstairs and go to sleep.")
time.sleep(6)
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
            inp = input(r"you decide to fight what will you do?:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    elf_hp = damage_elf(elf_hp, damage_done)
                    current_hp1 = damage_elf(current_hp1, damage_done)
                else:
                    print("You missed!")
            if(inp == "dodge"):
                print("you dodged the elf's attack")
            if(inp == "run"):
                print("you ran away")
        print("You have beaten the elves!")
    time.sleep(3)
    print("You see the big glowing Christmas tree and think it’s time to take it home")
    time.sleep(3)
    print("Ho ho ho looks like someone is trying to take our Christmas tree home.")
    time.sleep(3)
    print("Santa comes down to attack you and you start to fight")
    while current_hp2 > 0:
            inp = input(r" santa has appeared what will you do?:  ")
            if(inp == "attack"):
                if(roll_to_hit(ac)):
                    damage_done = roll_4_dmg(strength)
                    current_hp2 = damage_kerst(current_hp2, damage_done)
                else:
                    print("You missed!")
            if(inp == "dodge"):
                print("you dodged santa's attack")
            if(inp == "run"):
                print("you ran away")
    print("You beat santa!")

