from basics import screenClear, slowType, pressEnter
import players as p
import colours as c
import random as r
import time

def battle(player, opponent):
    turn = 0
    battleOver = 0 #if 1, lost. if 2, win.
    while battleOver == 0:
        while True:
            turn += 1
            dmgO = 0 #dmg done to opponent
            dmgP = 0 #dmg done to player
            rand = 0 #the 'random' variable, see dmg calculator in any case below
            dodge = 0 #if the player dodges, it will note if it was successful or not to print it after the opponents move
            screenClear()
            print("Turn", turn, "\n")
            p.healthBar(player)
            p.healthBar(opponent)
            print("\nWhat will you do?")
            c.red("Offensive:")
            print("1) Light attack\n2) Heavy attack\n")
            c.cyan("Defensive:")
            print("3) Block\n4) Dodge\n")
            c.green("Miscellaneous:")
            print("5) Run")
            choices = []
            choices.append(str(input("\nEnter the number for the action you want to take: ")))
            
            if choices[0] == '5': #if you run
                if player.agility < opponent.agility: #is opponent faster?
                    choices.append(1) #you get caught
                else:
                    choices.append(2) #you get away
            
            else: #if you actually fight
                rand = r.randint(1, 6)
                match choices[0]:
                    case '1': #if you do a quick attack
                        if rand == 5 or rand == 6:
                            rand = 3 #more chance of blocking
                    case '2': #if you do a heavy attack
                        if rand == 5 or rand == 6:
                            rand = 4 #more chance of dodging
                    case '3': #if you do a block
                        if rand == 5 or rand == 6:
                            rand = 2 #more chance of heavy attack
                    case '4': #if you do a dodge
                        if rand == 5 or rand == 6:
                            rand = 1 #more chance of quick attack
                choices.append(rand)

            match choices[0]: #heavy attacks give 3* attack, block five 3* defence
                case '1':
                    slowType("\nYou preform a \033[1;31;48mquick attack\033[1;37;48m.\n")
                    dmgO += (3*player.attack)
                case '2':
                    slowType("\nYou preform a \033[1;31;48mheavy attack\033[1;37;48m.\n")
                    dmgO += (2*(3*player.attack))
                case '3':
                    slowType("\nYou set up your guard to \033[1;34;48mblock\033[1;37;48m incoming attacks.\n")
                    dmgP -= (4*(3*player.defence))
                case '4':
                    slowType("\nYou prepare yourself to \033[1;34;48mdodge\033[1;37;48m.\n")
                    if r.randint(1,2) == 1:
                        dmgP -= 1000
                        dodge = 1 #dodge successful
                    else:
                        dodge = 2 #dodge unsuccessful

            match choices[1]:
                case 1:
                    slowType(opponent.name+" preforms a \033[1;31;48mquick attack\033[1;37;48m.\n")
                    dmgP += (3*opponent.attack)
                    break
                case 2:
                    slowType(opponent.name+" preforms a \033[1;31;48mheavy attack\033[1;37;48m.\n")
                    dmgP += (2*(3*opponent.attack))
                    break
                case 3:
                    slowType(opponent.name+" sets up his guard to \033[1;34;48mblock\033[1;37;48m.\n")
                    dmgO -= (4*(3*opponent.defence))
                    break
                case 4:
                    slowType(opponent.name+" prepares to \033[1;34;48mdodge\033[1;37;48m.\n")
                    if r.randint(1,2) == 1:
                        dmgO -= 1000
                        slowType(opponent.name+" successfully evaded your attack.\n")
                    else:
                        slowType("You manage to land a hit on "+opponent.name+".\n")
                    break
                case _:
                    c.red("Please input a number displayed.")
                    turn -= 1 
                    time.sleep(1.5)

        if dodge == 1:
            slowType("You successfully evade "+opponent.name+"'s attack.\n")
        elif dodge == 2:
            slowType(opponent.name+" still manages to land a hit on you.\n")
        if dmgO < 0:
            dmgO = 0
        if dmgP < 0:
            dmgP = 0
        player.hp -= dmgP
        opponent.hp -= dmgO
        dmgP = dmgP*10000
        dmgO = dmgO*10000
        slowType("\nYou take \033[1;31;48m"+str(dmgP)+"\033[1;37;48m damage, while "+opponent.name+" takes \033[1;31;48m"+str(dmgO)+"\033[1;37;48m damage.")
        pressEnter()
        if opponent.hp <= 0 and player.hp <= 0:
            battleOver = 3  #if its a tie
            opponent.hp = 0
            player.hp = 0
        elif opponent.hp <= 0:
            battleOver = 2  #if opponent is dead
            opponent.hp = 0
        elif player.hp <= 0:
            battleOver = 1  #if player is dead
            player.hp = 0
    if battleOver == 2:
        slowType("\n\033[1;36;48mYou win.\033[1;37;48m", 0.2)
    elif battleOver == 1:
        slowType("\n\033[1;31;48mYou lost.\033[1;37;48m", 0.2)
    else:
        slowType("\033[1;32;48mIt's a tie.\033[1;37;48m", 0.2)
    pressEnter()

    #if opponent.hp <= 0:
        #playerXP += 5 * enemyLvl
        #if playerXP > 100:
            #playerXP -= 100
            #p.levelUp()
        #break
