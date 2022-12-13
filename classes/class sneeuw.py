import random

class attack():
    sneeuw_hp = 50
    current_hp = sneeuw_hp
    ac = 15
    strength = 5
    def roll_to_hit(ac):
        hit = random.randint(1, 20)
        if hit <= ac:
            return True
        return False
    def roll_4_dmg(strength):
        dmg = random.randint(1, 10) + strength
            print(f"You hit and did {dmg} damage.")
            return dmg
        def damage(sneeuw_hp, dmg):
            current_hp = sneeuw_hp - dmg
            return current_hp
        def V_sneeuwpop(current_hp5, strength, ac, roll_to_hit, roll_4_dmg, damage_sneeuwpop):
            while current_hp5 > 0:
                inp = input(r"the guards hold you down what do you do?:  ")
                    if(inp == "attack"):
                        if(roll_to_hit(ac)):
                            damage_done = roll_4_dmg(strength)
                            current_hp5 = damage_sneeuwpop(current_hp5, damage_done)
                            else:
                                print("You missed!")
                    if(inp == "dodge"):
                        print("you dodged the attack")
                    if(inp == "run"):
                        print("you ran away")
            print("You beat the guards and continue")

attack