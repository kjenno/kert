import random

class Player:
    hp = 100
    ac = 15
    name = ""

    def setName(name):
        name = name

    def setHp(number):
        hp = hp - number

    def roll_to_hit(ac):
        hit = random.randint(1, 20)
        if hit <= ac:
            return True
        return False

    def roll_4_dmg(strength):
        dmg = random.randint(1, 10) + strength
        print(f"You hit and did {dmg} damage.")
        return dmg

    def damage(monster_hp, dmg):
        current_hp = monster_hp - dmg
        return current_hp


