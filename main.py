#import sys;print(sys.version)
from basics import screenClear, pressEnter, confirm, slowType
import colours as c
import chapters as chap
import players as p
import time, os, sys

while True:
    screenClear()
    name = (input("Character select\n\n1) Adib\n2) Mathieu\n3) Jacob\n4) Ali-Hassan\n5) Hadi\n6) Hussein\n\nWhat is your choice? ")) #asks which character the player picks
    match name:
        case '1':
            slowType("\nAdib is the sexiest man in the band. As the leader of the pack, he has the capacity to fulfill all your desires but he couldn't be bothered. He loves women and power and money and women. The first part may be inaccurate, but damn, that stache baby. He is the most experienced weeb of the lot. His body mass index is above 9000. 'Heavily' relient on\033[1;31;48m Le Ecchi\033[1;37;48m for his life force.\n")
            c.cyan('\nMoto: "Mumei best girl >:)"')
            c.green("\nDominant trait: Overall Balanced\n")
            pressEnter()
            player = p.Adib()
            print(player)
            if confirm() == True:
                break
        case '2':
            slowType("\nMathieu is a Jack of all trades, this character can fail you at every occasion. He likes money and power, but is especially attracted to money (but also power and influence, and sometimes women but mostly money and also power.) Often reffered to as 'Matoes', he is passionate about 2B and her story and strives to make his life something as exciting. Passive ability: He has a copious amount of wealth to his disposal.\n")
            c.cyan('\nMoto: "Looks like I\'m gonna have to Miracle Johnson on you."')
            c.green("\nDominant trait: Defence\n")
            pressEnter()
            player = p.Mathieu()
            print(player)
            if confirm() == True:
                break
        case '3':
            slowType("\nJacob, dit Jascorbut, Jascurvy, Jasboc, Basboco et Jascoom, is pretty understanding when it comes to talking about feeling, however he cannot stand society. While he boasts a modest weeb power, he is without the shadow of a doubt the one with the highest potential to become something truly terrifying. With his deep experience and understanding of edgyness (see what I did there ;)), he is able to stay under the radar. He is, however on his last life. He died of cringe twice already and is trying his best to preserve his final one.\n")
            c.cyan('\nMoto: "I\'m gonna Dust-eze out of here, the fish are calling me. *SCREECH*"')
            c.green("\nDominant trait: Agility\n")
            pressEnter()
            player = p.Jacob()
            print(player)
            if confirm() == True:
                break
        case '4':
            slowType("\nPersonality varies incredibly, a wildcard. Can go from sophisticated to monkey mode very quickly. Overall specialises in charisma but lacks in the bains department, due to extensive map gaming and history aids. Somewhat experienced in the consumption of weebery. With his high efforts in regards to learning strategies from historical battles, he is able to plan and cooridinate attacks extremly well, however his execution isn't always on par. He has a special ability known as :weary:, which helps to throw off opponents. Known weaknesses: Caffeine withdrawal.\n")
            c.cyan('\nMoto: "MY FEET ARE NUMB MAN! UEEEAAAAAAAHHHHHHHH!!"')
            c.green("\nDominant trait: Charisma\n") 
            pressEnter() 
            player = p.Ali()
            print(player)
            if confirm() == True:
                break
        case 'ovni':
            print("On m'appel l'ovni tutututututu")
            time.sleep(0.3)
        case '5':
            slowType("\nHadi, the one and only. With his experience of his travels up in the mointains, he is always ready to tell a story. He has a deep understanding in the pysics of this world and of nature. He is also a quick learner, thus able to understand enemy patterns and counter them in a matter of minutes. Somewhat experienced in the consumption of weebery. Has a shameful past, yet he has recovered well and become a true warrior of Les Accidents.\n")
            c.cyan('\nMoto: "I\'m gonna have to finish you, I don\'t care about your #DISTAVIE."')
            c.green("\nDominant trait: Intellect\n")
            pressEnter()
            player = p.Hadi()
            print(player)
            if confirm() == True:
                break
        case '6':
            slowType("\nHussein may seem like the 'goofy' character, however, do not be fooled. His expertise in the domain of anime has been tremendously helpful for his travels and they shows his great understanding of psychology and so called women. Extremely experienced in consuming weebery, perhaps even surpassing Adib levels. Has often been speculated to be the gayest of the lot, as he often wishes to do uh oh moments to other members of the squad. He relates very well with his monkey and ape brethren.\n")
            c.cyan('\nMoto: "Ayo fait attention sinon je vais te sucer les fesses >:)"')
            c.green("\nDominant trait: Attack\n")
            pressEnter()
            player = p.Hussein()
            print(player)
            if confirm() == True:
                break
        case 'd' | 'debug': #REMOVE WHEN DONE
            p.battle(p.Hussein(), p.Hadi())
        case _:
            c.red("Please input a number displayed.")        
            time.sleep(1.5)

while True:
    screenClear()
    chapSel = input("What chapter would you like to play? (1 - 5, 'si' or 'menu')\n") #asks what chapter they would like to play
    match chapSel: #depending on their choice, the correct chapter function will be called
        case '1':
            c.cyan("\nYou chose chapter 1: The Birth of a Mistake")
            time.sleep(1)
            if confirm() == True:
                chap.c1()
        case '2':
            c.cyan("\nYou chose chapter 2: The Attack of the Virus")
            time.sleep(1)
            if confirm() == True:
                chap.c2()
        case '3':
            c.cyan("\nYou chose chapter 3: Hussein's Trial")
            time.sleep(1)
            if confirm() == True:
                chap.c3()
        case '4':
            c.cyan("\nYou chose chapter 4: The Civil War")
            time.sleep(1)
            if confirm() == True:
                chap.c4()
        case '5':
            c.cyan("\nYou chose chapter 5: Mathieu's ASCENT")
            time.sleep(1)
            if confirm() == True:
                chap.c5()
        case 'si':
            c.cyan("\nYou chose the special issue: Cerial vs Milk")
            time.sleep(1)
            if confirm() == True:
                chap.csi()
        case 'menu':
            os.execl(sys.executable, sys.executable, *sys.argv)
        case _:
            c.red("\nPlease input a valid chapter")
            time.sleep(1)