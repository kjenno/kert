class Spelverloop:
    beurt = 1
    status = 1

    def setBeurt():
        if(beurt == 1):
            beurt = 2
        else:
            beurt = 1

    def statusPlus():
        status = status + 1
