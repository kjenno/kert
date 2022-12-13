from speler import Player
from spelverloop import Spelverloop

speler = Player()
elf = Player()
kerst1 = Player()
sneeuw = Player()
kerst2 = Player()
sneeuwpop = Player()
spelverloop = Spelverloop()

speler.setName("The Boss")
elf.setName("The Boss")
kerst1.setName("The Boss")
sneeuw.setName("The Boss")
kerst2.setName("The Boss")
sneeuwpop.setName("The Boss")

speler.setHp(100)
elf.setHp(100)
kerst1.setHp(100)
sneeuw.setHp(100)
kerst2.setHp(100)
sneeuwpop.setHp(100)

beurt = Spelverloop.beurt

while(True):
    if(beurt ==  1):
        attack = speler.roll_to_hit()
        if(attack):
            damage = speler.roll_4_dmg()
            match spelverloop.status:
                case 1: elf.damage(damage)
                case 2: kerst1.damage(damage)
                case 3: sneeuw.damage(damage)
                case 4: kerst2.damage(damage)
                case 5: sneeuwpop.damage(damage)
                case 6: exit()
            spelverloop.setBeurt()
    else:
         attack = speler.roll_to_hit()
         speler.damage(damage)
         spelverloop.setBeurt()

