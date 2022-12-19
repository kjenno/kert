points = 10
charisma = 0
attack = 0
luck = 0

def cotrolle(amountofpoints, points):
   if amountofpoints >= points:
      return False

while True:
 print("To what would you like to add a skill point?")
 print("[charisma] [attack] [luck]")
 print("------------------------------")
 choice = input("")

 if choice == ("charisma"):
    print("How many points would you like to add to", choice, "you have a total of", points, "points.")
    print("------------------------------")
    amountofpoints = int(input(""))
    charisma = amountofpoints + charisma
    print("You have",charisma,"charisma points.")
    points = points - amountofpoints
    print("You have",points,"points left.")

 if choice == ("attack"):
    print("How many points would you like to add to", choice, "you have a total of", points, "points.")
    print("------------------------------")
    amountofpoints = int(input(""))
    attack = amountofpoints + attack
    print("You have",attack,"attack points.")
    points = points - amountofpoints
    print("You have",points,"points left.")
    
 if choice == ("luck"):
    print("How many points would you like to add to", choice, "you have a total of", points, "points.")
    print("------------------------------")
    amountofpoints = int(input(""))
    luck = amountofpoints + luck
    print("You have",luck,"luck points.")
    points = points - amountofpoints
    print("You have",points,"points left.")

 if points <= 0:
   print("Your skills")
   print("------------------------------")
   print("Charisma :", charisma)
   print("Attack :", attack)
   print("Luck :", luck)
   break




