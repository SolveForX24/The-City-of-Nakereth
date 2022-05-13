import random
import variables

# Randomly generate whether or not to send True or False
def stunChance():
    chance = random.randrange(1, 3);
    if chance == 1:
        return True
    else:
        return False
  
# Main combat function
def combat(monster, cardListToChoose, cardListBackup):
    
    # Establish important variables.
    monsterHealth = 0
    monsterHealthMax = 0
    monsterChoice = 0
    monsterChoiceAction = ""
    monsterDamage = 0
    monsterDamageDebuff = 0
    monsterHealing = 0
  
    firstCard = ""
    secondCard = ""
    thirdCard = ""
    
    playerChoice = 0
    playerChoiceAction = ""
    
    health = variables.health
    healing = 0
    playerDamage = 0
    playerDamageDebuff = 0

    quickAttackLoops = 0
    quickAttackDamageTotal = 0
    
    stun = False

    success = ""

    if monster == "Zombie":
        monsterHealth = 20
        monsterHealthMax = 20
    if monster == "Golem":
        monsterHealth = 50
        monsterHealthMax = 50
    if monster == "Ghost":
        monsterHealth = 30
        monsterHealthMax = 30
    if monster == "Imp":
        monsterHealth = 25
        monsterHealthMax = 25
        
    # This is the loop we go through for combat (fulfills loop requirement)    
    while monsterHealth > 0 or health > 0:
        
      # Printout at beginning of turn
      print("\nEnemy: " + monster + "\nEnemy Health: " + str(monsterHealth))

      # Randomly chooses monsters attack
      monsterChoice = random.randrange(2)

      if monster == "Zombie":
          if monsterChoice == 0:
              monsterChoiceAction = "Rend"
          else:
              monsterChoiceAction = "Defend"
      if monster == "Golem":
          if monsterChoice == 0:
              monsterChoiceAction = "Slam"
          else:
              monsterChoiceAction = "Stone Armor"
      if monster == "Ghost":
          if monsterChoice == 0:
              monsterChoiceAction = "Imbue"
          else:
              monsterChoiceAction = "Otherworldly Screech"

      # Quick Claw is a special move, because it is used right at the beginning before the player has a chance to do anything. Therefore, the code for it's attack is placed here.
      if monster == "Imp":
          if monsterChoice == 0:
            monsterChoiceAction = "Quick Claw"
            if stun == False:
              monsterDamage = random.randrange(1,4)
              print ("The speedy imp uses their Quick Claw, dealing " + str(monsterDamage) + " damage.")
              health -= monsterDamage
            else:
              print("The " + monster + " would have used Quick Claw, but you succesfully stunned them.")
          else:
              monsterChoiceAction = "Slash of Fury"

      # If the player dies to Quick Claw, breaks
      if health < 1:
        print("Unfortunately, the " + monster + " has taken your life from you.")
        success = "Failure"
        return "Failure"

      # If the attack is not Quick Claw, print out the monsters intentions.
      if monsterChoiceAction != "Quick Claw":
          print("It seems like your foe will use their " + monsterChoiceAction + ".")            
      # Part of print out, shows how much health you have left.
      print("You have " + str(health) + " health points left.")

      # Reset stun.  
      stun = False

      # Refill card list
      cardListToChoose = []
      for item in cardListBackup:
        cardListToChoose.append(item)
        
      # Randomly chooses 3 cards for the player (fulfills list and selection requirements)
      firstCard = random.choice(cardListToChoose);
      cardListToChoose.remove(firstCard)

      secondCard = random.choice(cardListToChoose);
      cardListToChoose.remove(secondCard)

      thirdCard = random.choice(cardListToChoose);
      cardListToChoose.remove(thirdCard)
        
      # Print out the cards you received
      print("\nYour cards are: " + firstCard + ", " + secondCard + ", and " + thirdCard + ".")
        
      # The user chooses which card they want in a while True loop, so that if they choose a value out of range, it will simply ask again.
      while True:
        playerChoice = 0
        playerChoice = int(input("Which card shall you use? (1/2/3) "))
        
        if playerChoice == 1:
            playerChoiceAction = firstCard
            break
        elif playerChoice == 2:
            playerChoiceAction = secondCard
            break
        elif playerChoice == 3:
            playerChoiceAction = thirdCard
            break

      # Print out what the player has chosen, then deal with the ramifications.      
      print("\nYou have chosen to use " + playerChoiceAction + ".")

      # Strike is a basic attack. It simply randomly generates damage, and deals that to the enemy.    
      if playerChoiceAction == "Strike":
        playerDamage = random.randrange(4, 8)
        if monsterChoiceAction == "Defend":
          playerDamage = playerDamage - 2;
          print("The " + monster + "'s Defend limits the power of your attack.")
          int(playerDamage)
        playerDamage -= playerDamageDebuff
        if playerDamage <= 0:
            print("The " + monster + "'s defenses prevent you from dealing any damage.")
        else: 
          print("You have dealt " + str(playerDamage) + " damage to the " + monster + ".")
          monsterHealth -= playerDamage

      # Guard will limit the damage of the next attack by 3.
      elif playerChoiceAction == "Guard":
        monsterDamageDebuff = 3
        print("You bring up your shield, preparing for the assault.")

      # Bash does a little damage, but it's main thing is that is has a 1 in 3 chance to cause the enemy to NOT do it's attack. This is powerful, which is why Bash appears only twice in your deck, so it's less likely to appear as an option.
      elif playerChoiceAction == "Bash":
        playerDamage = random.randrange(2, 3)
        if monsterChoiceAction == "Defend":
          playerDamage = playerDamage - 2;
          print("The " + monster + "'s Defend limits the power of your attack.")
        print("You have dealt " + str(playerDamage) + " damage to the " + monster + ".")
        monsterHealth -= playerDamage
        stun = stunChance()
        if stun:
          print("Your bash stunned the enemy!")
          if monsterChoiceAction == "Defend":
            print(" Nothing comes of it, however, since the enemy wasn't likely to attack.")
        else:
          print("The " + monster + " is unfazed.")

      # The rest of the attacks are ones you earn by defeating enemies.

      # This attack deals low damage, but heals you for two times what you dealt.
      elif playerChoiceAction == "Leeching Claw":
        playerDamage = random.randrange(2, 3)
        if monsterChoiceAction == "Defend":
          playerDamage = playerDamage - 2;
          print("The " + monster + "'s Defend limits the power of your attack.")
        playerDamage -= playerDamageDebuff
        if playerDamage <= 0:
            print("The " + monster + "'s defenses prevent you from dealing any damage.")
            playerDamage = 0
        print("You have dealt " + str(playerDamage) + " damage to the " + monster + ".")
        monsterHealth -= playerDamage

        health += playerDamage * 2
        print("The leeching abilities of the zombies claw heals you for " + str(playerDamage * 2) + " as well.")
        if health > 50:
          print("The effect of your Leeching Claw isn't great, as you cannot hold much more health within.")
          health = 50

      # Switches the attack your enemy will do. This is VERY strong in some cases.
      elif playerChoiceAction == "Manipulate Elements":
        if monsterChoiceAction == "Rend":
          monsterChoiceAction == "Defend"

        elif monsterChoiceAction == "Defend":
          monsterChoiceAction == "Rend"

        elif monsterChoiceAction == "Slam":
          monsterChoiceAction == "Stone Armor"

        elif monsterChoiceAction == "Stone Armor":
          monsterChoiceAction == "Slam"

        elif monsterChoiceAction == "Imbue":
          monsterChoiceAction == "OtherworldlyScreech"

        elif monsterChoiceAction == "Otherworldly Screech":
          monsterChoiceAction == "Imbue"

        elif monsterChoiceAction == "Quick Claw":
          monsterChoiceAction == "Slash of Fury"

        elif monsterChoiceAction == "Slash of Fury":
          monsterChoiceAction == "Quick Claw"
        
        print("The monsters choice switches.")

      # Heals the player for a random amount between 8 and 12
      elif playerChoiceAction == "Spectral Leech":
        healing = random.randrange(6, 11)
        health += healing
        print("You absorb the spirits of the dead around you, healing " + str(healing) + " health.")
        if health > 50:
          print("The effect of your Spectral Leech isn't great, as you cannot hold many more souls within.")
          health = 50

      # This attack does low damage, but will loop between 1 and 3 times. Can lead to some strong damage overall.
      elif playerChoiceAction == "Quick Attack":
        
        quickAttackLoops = random.randrange(2,5)

        for i in range (quickAttackLoops):
          playerDamage = random.randrange(3, 5)
          if monsterChoiceAction == "Defend":
            playerDamage = playerDamage - 2;
          playerDamage -= playerDamageDebuff
          if playerDamage <= 0:
            print("The " + monster + "'s defenses prevent you from dealing any damage.")
            playerDamage = 0
          
          quickAttackDamageTotal += playerDamage
          if playerDamage > 0:
            print("You have dealt " + str(playerDamage) + " damage to the " + monster + ".")
          monsterHealth -= playerDamage
        
        print("You got in " + str(quickAttackLoops) + " attacks.")

      # If the monster dies, breaks
      if monsterHealth < 1:
        print("The " + monster + " perishes!")
        variables.health = health
        success = "Success"
        return success


      # Monster attacks. First checks and makes sure the enemy isn't stunned.
      if stun == False:

        if monsterChoiceAction == "Rend":
          monsterDamage = random.randrange(2, 6)
          monsterDamage = monsterDamage - monsterDamageDebuff
          if monsterDamage > 0:
            print("The gnarled claws of the " + monster + " tear your skin, dealing " + str(monsterDamage) + " damage!")
            health -= monsterDamage
          else:
            print("Your guard does wonders, protecting you from harm!")

        elif monsterChoiceAction == "Slam":
          monsterDamage = random.randrange(5, 8)
          monsterDamage = monsterDamage - monsterDamageDebuff
          print("The " + monster + " slams their giant fists into you, dealing " + str(monsterDamage) + " damage!")
          health -= monsterDamage

        elif monsterChoiceAction == "Stone Armor":
          print("The " + monster + " calls upon the elements and covers themselves in stone.")
          playerDamageDebuff += 1
          if playerDamageDebuff >= 3:
            playerDamageDebuff = 3
            print("They were already mostly covered in stone, so it had no effect.")
          else: 
            print("They will take less damage now!")

        elif monsterChoiceAction == "Imbue":
          monsterHealing = random.randrange(2, 5)
          monsterHealth += monsterHealing
          if monsterHealth > monsterHealthMax:
            monsterHealth = monsterHealthMax
          print("The " + monster + " absorbs the energy of the dead spirits here and give themselves strength. They have healed " + str(monsterHealing) + " health back.")

        elif monsterChoiceAction == "Otherworldly Screech":
          monsterDamage = random.randrange(3, 5)
          monsterDamage = monsterDamage - monsterDamageDebuff
          if monsterDamage > 0:
            print("The unholy scream of the " + monster + " breaks your mind, dealing " + str(monsterDamage) + " damage!")
            health -= monsterDamage
          else:
            print("Your guard does wonders, protecting you from harm!")

        elif monsterChoiceAction == "Slash of Fury":
          monsterDamage = random.randrange(5, 7)
          monsterDamage = monsterDamage - monsterDamageDebuff
          print("The " + monster + " double slashes you with their long claws, dealing " + str(monsterDamage) + " damage!")
          health -= monsterDamage

      else:
        print("The enemy is stunned and will not perform their action.")
        if monsterChoiceAction != "Quick Claw":
          stun = False

      # If the player dies, breaks
      if health < 1:
        print("Unfortunately, the " + monster + " has taken your life from you.")
        success = "Failure"
        variables.health = health
        return "Failure"
        
      
      monsterDamageDebuff = 0
        
      if playerChoiceAction == "Guard":
        print("The effect of your Guard wears off.")