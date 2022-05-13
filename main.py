# Name: Xander Russell
# Performance Task: Attack on Nakereth
# Date: 2/17/21
        
# Main Code

import random
import combat
import variables

playing = True
while playing:

  #roomsList = [""]
  monsterList = ["Zombie", "Zombie", "Ghost", "Imp"]
  cardList = ["Strike", "Strike", "Strike", "Strike", "Bash", "Bash", "Guard", "Guard", "Guard","Guard"]
  cardListBackup = ["Strike", "Strike", "Strike", "Strike", "Bash", "Bash", "Guard", "Guard", "Guard","Guard"]

  random.shuffle(monsterList);
  #random.shuffle(cardList);

  success = ""
  continuePrompt = True

  print("Welcome, fool, to the dead city of Nakereth.\nSeek you the treasure found in the center? Then you must work your way in from the edge.\nYour first stop: the Calithian Outskirts.\n")

  # Fight loop: chooses enemy, runs combat function, and depending on what occurs, either runs game over state or adds new card. Removes the enemy from the list as well. Then repeat.
  for i in range(5):

    if i != 4:
      enemy = random.choice(monsterList)
      print("\nAn enemy approaches you! Now you fight against a " + enemy + "!")
    else:
      print("\n\nAs you arrive at the gate to the next ring of Nakereth, one of the ominous statues nearby begins to move. Suddenly, it jumps down from it plinth, and begins to attack. Succeed against the boss, Golem, and proceed!")
      enemy = "Golem"

    success = combat.combat(enemy, cardList, cardListBackup)

    if success == "Failure":
      tryAgain = ""
      tryAgain = input("\n\nGame Over! Would you like to try again? (y/n) ")
      if tryAgain == "y":
        variables.health = 30;
        print("\n\n\n")
        break
      else:
        print("\n\nThank you for playing!")
        continuePrompt = False
        break
    else:
      print("As the fight ends, your health is " + str(variables.health) + ".")

    if enemy == "Zombie":
      cardList.append("Leeching Claw")
      cardListBackup.append("Leeching Claw")
      print("You have gained the Leeching Claw ability.")
    if enemy == "Golem":
      cardList.append("Manipulate Elements")
      cardListBackup.append("Manipulate Elements")
      print("You have gained the Manipulate ability.")
    if enemy == "Ghost":
      cardList.append("Spectral Leech")
      cardListBackup.append("Spectral Leech")
      print("You have gained the Spectral Leech ability.")
    if enemy == "Imp":
      cardList.append("Quick Attack")
      cardListBackup.append("Quick Attack")
      print("You have gained the Quick Attack ability.")

    if enemy != "Golem":
      monsterList.remove(enemy)

         
  if variables.health >= 1:
    print("Congratulations! Thank you for playing the demo, it's very likely this will get expanded upon :D")
    playing = False
    break

  if continuePrompt:
    continue
  else:
    #print("Thank you for trying my demo!")
    playing = False
    break