from basics import screenClear, slowType, pressEnter
import players as p
import colours as c
import random as r
import time

def battle(player, opponent):
    turn = 0
    battleOver = 0 #if 1, player lost. if 2, opponent lost.
    while battleOver == 0:
        while True:
            turn += 1
            dmgO = 0 #dmg done to opponent
            dmgP = 0 #dmg done to player
            rand = 0 #the 'random' variable, see dmg calculator in any case below
            screenClear()
            print("Turn", turn, "\n")
            p.healthBar(player)
            p.healthBar(opponent)
            print("\nWhat will you do?")
            c.yellow("Offensive:")
            print("1)Quick light attack\n2)Strong heavy attack")
            c.blue("Defensive:")
            print("3)Block\n4)Dodge")
            c.green("Miscellaneous:")
            print("5)RUN RUN RUN\n6)HIDE HIDE HIDE")
            choices = []
            choices.append(str(input("\nEnter the number for the action you want to take: ")))
            
            if choices[0] == '5': #if you run
                if player.agility < opponent.agility: #is opponent faster?
                    choices.append(1) #you get caught
                else:
                    choices.append(2) #you get away

            elif choices[0] == '6': #if you hide
                if player.intellect > opponent.intellect: #are you smarter?
                    choices.append(1) #you hid well
                else:
                    choices.append(2) #you were found

            elif choices[0].lower() == 's' or choices[0].lower() == 'stats':
                choices[0] = 's'

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
            print(choices)
            match choices: #heavy attacks give +10 attack, block five +15 defence
                case '1', 1:
                    pass

                case '1', 2:
                    pass

                case '1', 3: #common
                    dmgO = (5*player.attack)-(15+(3*opponent.defence))
                    slowType("You swifly swing at "+opponent.name+", but they block you attack. You deal \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                    pressEnter()
                    break
                case '1', 4:
                    pass

                case '2', 1:
                    pass

                case '2', 2:
                    pass

                case '2', 3:
                    pass

                case '2', 4: #common
                    if player.agility > opponent.agility and r.randint(1,2) == 1:
                        dmgO = (10+(5*player.attack))-(3*opponent.defence)
                        slowType("You preform a mighty swing and manage to hit "+opponent.name+". Dealing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                    else:
                        slowType("You attempt a hit but "+opponent.name+" dodged to quickly.")
                    pressEnter()
                    break
                case '3', 1:
                    pass

                case '3', 2: #common
                    dmgP = (5*opponent.attack)-(10+(3*player.defence))
                    if dmgP < 0:
                        dmgP = 1
                    slowType(opponent.name+" sends a big blow at you but you manage to block the incoming attack. Even with that block you absorb a smaller \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                    pressEnter()
                    break

                case '3', 3:
                    pass

                case '3', 4:
                    pass

                case '4', 1: #common
                    if player.agility < opponent.agility and r.randint(1,2) == 1:
                        slowType(opponent.name+" slashes at you but you dodge just in time, saving you from a hit.")
                    else:
                        dmgP = (5*opponent.attack)-(3*player.defence)
                        slowType(opponent.name+" preforms a quick jab in your direction and hits you, dealing \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                    pressEnter()
                    break

                case '4', 2:
                    pass

                case '4', 3:
                    pass

                case '4', 4:
                    pass

                case '5', 1:
                    pass

                case '5', 2:
                    pass

                case '6', 1:
                    pass

                case '6', 2:
                    pass

                case 's':
                    stats(player)

                case _:
                    c.red("Please input a number displayed.")
                    turn -= 1 
                    time.sleep(1.5)



        player.hp -= dmgP
        opponent.hp -= dmgO
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




#            case '3', 1:
#                dmgO = (r.randint(14,17)*player.attack)//opponent.defence
#                slowType("You drop kick on "+opponent.name+", kocking a tooth out and inflicting \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
#            case '4', 1:
#                slowType(opponent.name+" attempted to send a punch to your face, but you successfully blocked it with yo mousklees.")
                
#            case '5', 1:
#                dmgP = (r.randint(14,17)*opponent.attack)//player.defence
#                slowType("You try put up your guard on your right, but "+opponent.name+" sends a punch to your left dealing you \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")

#            case '1', 2: #player: punch, opp: bd
#                rand = r.randint(16,19)
#                dmgP = (rand*opponent.attack)//player.defence
#                slowType("You attemp to throw a punch but "+opponent.name+" sweeps you off your feet with a low kick.\nYou were inflicted with \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
#            case '2', 2:
#                slowType("You try to do a nice high kick with style, but notice that "+opponent.name+" is doing the exact same and you both end up just dancing, causing \033[1;31;48mno damage \033[1;37;48mto be done. IS THIS A DANCE OFF OR WHAT??!")
                
#            case '3', 2:
#                dmgP = (r.randint(8,15)*opponent.attack)//player.defence
#                slowType("You jump high in the air to land a drop kick on "+opponent.name+".\nBut he saw it coming. He punched your leg not the way its supposed to go before you could land your hit. Dealing you \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
#            case '4', 2:
#                dmgP = (r.randint(10,14)*opponent.attack)//player.defence
#                slowType('"'+opponent.moto+'!" screams '+opponent.name+'.\nWhile you foolishly attempt to cover your left side, '+opponent.name+' does an impressive spin kick and kocks you on the ground dealing you \033[1;31;48m'+str(dmgP)+'00000\033[1;37;48m points fo damage.') 
                
#            case '5', 2:
#                slowType(opponent.name+" attemps to do an upsidedown kick in ya face!\nBut this time, you were ready and successfully blocked it causing \033[1;31;48mno damage \033[1;37;48mto be dealt at all.")

#            case '1', 3:
#                dmgO = (r.randint(9,16)*player.attack)//opponent.defence
#                slowType(opponent.name+" attempted to drop kick you but you take this oppoeruninty to upper-cut-punch the life energy out of him, dealing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
#            case '2', 3:
#                dmgO = (r.randint(10,17)*player.attack)//opponent.defence
#                slowType("You wait for your oppenent's move, and as they attack you straight in the front, you feint and land a blow to their right, possibly shattering a rib, you say 'crounch', when the blow lands, dealing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
#            case '3', 3:
#                rand = r.randint(12,16)
#                dmgP = (rand*opponent.attack)//player.defence
#                dmgO = (rand*player.attack)//opponent.defence
#                slowType("You lift up your leg, aiming directly for your opponent's face, but they punch in the same direction, and your blows connect. As they hit, time seems to slow, as massive amounts of energy are released, knocking you both back, as you take \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m point of damage while "+opponent.name+" takes \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m.")
                
#            case '4', 3:
#                dmgP = (r.randint(14,17)*opponent.attack)//player.defence
#                slowType("You block your left, but all you see is an eclipse of "+ opponent.name+" falling from the sky and drop kicking the life outta you dealing \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
#            case '5', 3:
#                dmgP = (r.randint(14,18)*opponent.attack)//player.defence
#                slowType("Your opponent makes for your gut, however, as you raise your guard, they switch stance and hammer your side with a powerful kick. 'Damn, I wasn't able to rupture your kidney', your opponent says, nonetheless, you nearly retch from the pain, taking \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")

#            case '1', 4:
#                slowType("You attack quickly for your opponent's left, but they raise a block just in time, and your attack does \033[1;31;48m no damage\033[1;37;48m. You miraculously disengage before they can seize your arm and throw you over their shoulder.")
                
#            case '2', 4:
#                dmgO = (r.randint(11,16)*player.attack)//opponent.defence
#                slowType("Your opponent prepares to block their left, but you throw all your weight behind a flap palm hit to their stomach's left, channeling your inner chi. As the blow hits, you approach them whispering to them 'Shit yourself yet?'. You do \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
#            case '3', 4:
#                dmgO = (r.randint(13,17)*player.attack)//opponent.defence
#                slowType(opponent.name+" prepares for your next move, anticipating an attack from the left, but you instead strike like a cobra, hitting them with your hand rigid and extended like a dagger, crushing the cartilage of their nose, doing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")

#            case '1', 5:
#                dmgO = (r.randint(12,15)*player.attack)//opponent.defence
#                slowType("You make for your opponent's right, forcing them to commit to a block, and once their block is set, you switch directions, and karate chop them in the left of their gut. You do \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
#            case '2', 5:
#                dmgP = (r.randint(12,17)*opponent.attack)//player.defence
#                slowType("You make for your opponent's right, where they seize your arm and smash a karate chop into your arm, dislocating it at the elbow, dealing massive damage, although by sacrificing your life chi to pop it back in place, you take \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m damage points.")
                
#            case '3', 5:
#                dmgO = (r.randint(11,16)*player.attack)//opponent.defence
#                slowType("You make your opponent commit to a right block, but you strike, pouncing like a tiger and tackling them forward, knocking the air out of them and smashing your fist into their ribs, doing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m damage.")

#            case ['6', 1] | ['6', 2] | ['6', 3]: #player braces
#                dmgp = ((r.randint(5,7))*player.attack)//opponent.defence
#                slowType("You brace yourself, preparing for whatever comes.\n"+opponent.name+" takes a good smack at you. However, thanks to your mental preperation, you took a small \033[1;31;48m"+str(dmgp)+"00000\033[1;37;48m points of damage.")

#            case ['1', 6] | ['2', 6] | ['3', 6]: #opponent braces
#                dmgO = ((r.randint(5,7))*player.attack)//opponent.defence
#                slowType(opponent.name+" braced himself for the attack.\nYou swiftly preform your signiture move!\nYou inflicted a total of \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
            
#            case '0', 8: #opponent surrenders
#                slowType(opponent.name, "begs you for mercy.")
#                if player.charisma > opponent.charisma:
#                    battleOver = 2
#                    slowType("\nThanks to your supperior amount of charisma, you spare him and accept and \033[1;31;48measy win\033[1;37;48m.")
#                else:
#                    dmgO = 100
#                    slowType("You disregard his pathetic begging and prepare yourself to throw the final blow.")

#            case '8', 0: #player surrenders
#                slowType("You beg for mercy, surrendering your pride.")
#                if opponent.charisma > player.charisma:
#                    battleOver = 1
#                    slowType("\nWith "+opponent.name+"'s outstanding amount of charisma, he spares you. \033[1;31;48mYou must now accept defeat.\033[1;37;48m")
#                else:
#                    dmgP = 100
#                    slowType("\n"+opponent.name+", looks at you with disdain, and cruelly laughs as he lift you up from the neck with a single arm. As he crushes your windpipe with an iron grip, your world goes dark, you have \033[1;31;48mlost the fight\033[1;37;48m.")
                    
#            case '7', 0: #player runs
#                if player.agility > opponent.agility:
#                    battleOver = 1
#                    slowType("You succefully ran away like the coward you are.")
#                else:
#                    slowType(opponent.name+" caught you by the leg and dragged you back to continue the fight. Not today, coward.")
#            case '0', 7: #opponent runs
#                if oppoenent.agility > player.agility:
#                    battleOver = 2
#                    slowType("Darn.. "+opponent.name+"\033[1;31;48m got away \033[1;37;48m.")
#                else:
#                    slowType("You caught up to "+opponent.name+" and dragged him by the leg to finish the fight. Not today chief.")

 #           case ['4', 4] | ['5', 4] | ['6', 4] | ['4', 5] | ['5', 5] | ['6', 5] | ['4', 6] | ['5', 6] | ['6', 6]: #for any case that has both sides chosing a defensive move
 #               slowType("You both played defensively causing \033[1;31;48mno damage \033[1;37;48mto be done at all.")
 #           case _:
 #               c.red("An error occured. Please Try again.")     
 #               pressEnter()
    
 #       opponent.hp -= int(rounded_dmgO)
 #       player.hp -= int(rounded_dmgP)
 #       if opponent.hp <= 0 and player.hp <= 0:
 #           battleOver = 3  #if its a tie
 #           opponent.hp = 0
 #           player.hp = 0
 #       elif opponent.hp <= 0:
 #           battleOver = 2  #if opponent is dead
 #           opponent.hp = 0
 #       elif player.hp <= 0:
 #           battleOver = 1  #if player is dead
 #           player.hp = 0
 #       print("\n\nYour HP:")
 #       p.healthBar(player)
 #       print("\n"+opponent.name+"'s HP:")
 #       p.healthBar(opponent)

#        pressEnter()

#    if battleOver == 2:
#        slowType("\n\033[1;36;48mYou win.\033[1;37;48m", 0.2)
#    elif battleOver == 1:
#        slowType("\n\033[1;31;48mYou lost.\033[1;37;48m", 0.2)
#    else:
#        slowType("\033[1;32;48mIt's a tie.\033[1;37;48m", 0.2)
#    pressEnter()


    #if opponent.hp <= 0:
        #playerXP += 5 * enemyLvl
        #if playerXP > 100:
            #playerXP -= 100
            #p.levelUp()
        #break