from basics import screenClear, pressEnter, slowType, confirm
import colours as c
import battle as b
import random as r
import time, json, os, sys

def savefile():
    while True:
        screenClear()
        for i in range(1, 4): #repeats 3 times for each slot (theres 3)
            if os.path.isfile("LAL_saveSlots/slot"+str(i)+".txt"): #opens a file
                with open("LAL_saveSlots/slot"+str(i)+".txt") as save_file: data = json.load(save_file) #reads it
                for k in data['player']: name = k['character']; level = k['level'] #finds the name and level inside that save file
                print("Slot "+str(i)+": "+name+", Level "+str(level)) #prints that muzaphuka
            else: #if it does not find that file, it says empty
                print("Slot "+str(i)+": --Empty--")
        
        global slotSelection
        slotSelection = str(input("\nType the slot number of your save file (or 'delete'): ")) #asks what file you wanna use 
        if slotSelection.lower() == 'del' or slotSelection.lower() == 'delete': #checks if a file wants to be deleted
            while True:
                slotSelection = str(input("\nWhich save file you would you like to delete? (or type 'cancel'): ")) #asks what file to be deleted
                if slotSelection == 'cancel': #if user wants to cancel it breaks
                    break
                else:
                    if os.path.isfile("LAL_saveSlots/slot"+str(slotSelection)+".txt") == True:
                        if confirm("Are you sure you want to delete this save file? It will be gone\033[1;31;48m F O R E V E R!!\033[1;37;48m (y or n):    ") == True:#confirmation
                            os.remove("LAL_saveSlots/slot"+slotSelection+".txt")    #deletes the file
                            slowType("\nBombing save file...")
                            time.sleep(1)
                            slowType(" No survivors left.")
                            slotSelection = "menu"
                            time.sleep(0.5)
                    else:
                        c.red("That save file does not exist. Try again.")
                        time.sleep(1.5)
                        slotSelection = "menu"
                    break

        #elif slotSelection.lower() == 'debug' or 'd':#REMOVE
         #   b.battle(Hussein(), Hadi())
          #  break
        
        if slotSelection == '1' or slotSelection == '2' or slotSelection == '3':
            try: #tries the value inputted
                slowType("\nLoading save file... ") 
                with open("LAL_saveSlots/slot"+slotSelection+".txt") as save_file:
                    data = json.load(save_file)
                    for i in data['player']: player = i['character'];
                    if player == "blank":
                        return False
                    else:
                        return True #to skip character selection screen, if player is already chosen
                    time.sleep(1) #simulates loading time
                    slowType("Success.")
                    pressEnter()
                    break
                
            except: #if it fails, it asks if you want to create a save file, or that the file does not exist
            
                    if confirm("This slot is empty, would you like to use it? (y or n): ") == True:
                        screenClear()
                        save(slotSelection, newFile=True) #saves using the save function in basics.py
                        return False
                        pressEnter()
                        break
        elif slotSelection == "menu":
            pass
        else:
            c.red("That save file does not exist. Try again.")
            time.sleep(1.5)

def characterSelection():
    while True:
        screenClear()
        name = (input("Character select\n\n1) Adib\n2) Mathieu\n3) Jacob\n4) Ali-Hassan\n5) Hadi\n6) Hussein\n\nWhat is your choice? ")) #asks which character the player picks
        match name:
            case '1':
                slowType("\nAdib is the sexiest man in the band. As the leader of the pack, he has the capacity to fulfill all your desires but he couldn't be bothered. He loves women and power and money and women. The first part may be inaccurate, but damn, that stache baby. He is the most experienced weeb of the lot. His body mass index is above 9000. 'Heavily' relient on\033[1;31;48m Le Ecchi\033[1;37;48m for his life force.\n")
                c.cyan('\nMoto: "Mumei best girl >:)"')
                c.green("\nDominant trait: Overall Balanced\n")
                pressEnter()
                player = Adib()
                print(player)
                if confirm() == True:
                    break
            case '2':
                slowType("\nMathieu is a Jack of all trades, this character can fail you at every occasion. He likes money and power, but is especially attracted to money (but also power and influence, and sometimes women but mostly money and also power.) Often reffered to as 'Matoes', he is passionate about 2B and her story and strives to make his life something as exciting. Passive ability: He has a copious amount of wealth to his disposal.\n")
                c.cyan('\nMoto: "Looks like I\'m gonna have to Miracle Johnson on you."')
                c.green("\nDominant trait: Defence\n")
                pressEnter()
                player = Mathieu()
                print(player)
                if confirm() == True:
                    break
            case '3':
                slowType("\nJacob, dit Jascorbut, Jascurvy, Jasboc, Basboco et Jascoom, is pretty understanding when it comes to talking about feeling, however he cannot stand society. While he boasts a modest weeb power, he is without the shadow of a doubt the one with the highest potential to become something truly terrifying. With his deep experience and understanding of edgyness (see what I did there ;)), he is able to stay under the radar. He is, however on his last life. He died of cringe twice already and is trying his best to preserve his final one.\n")
                c.cyan('\nMoto: "I\'m gonna Dust-eze out of here, the fish are calling me. *SCREECH*"')
                c.green("\nDominant trait: Agility\n")
                pressEnter()
                player = Jacob()
                print(player)
                if confirm() == True:
                    break
            case '4':
                slowType("\nPersonality varies incredibly, a wildcard. Can go from sophisticated to monkey mode very quickly. Overall specialises in charisma but lacks in the bains department, due to extensive map gaming and history aids. Somewhat experienced in the consumption of weebery. With his high efforts in regards to learning strategies from historical battles, he is able to plan and cooridinate attacks extremly well, however his execution isn't always on par. He has a special ability known as :weary:, which helps to throw off opponents. Known weaknesses: Caffeine withdrawal.\n")
                c.cyan('\nMoto: "MY FEET ARE NUMB MAN! UEEEAAAAAAAHHHHHHHH!!"')
                c.green("\nDominant trait: Charisma\n") 
                pressEnter() 
                player = Ali()
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
                player = Hadi()
                print(player)
                if confirm() == True:
                    break
            case '6':
                slowType("\nHussein may seem like the 'goofy' character, however, do not be fooled. His expertise in the domain of anime has been tremendously helpful for his travels and they shows his great understanding of psychology and so called women. Extremely experienced in consuming weebery, perhaps even surpassing Adib levels. Has often been speculated to be the gayest of the lot, as he often wishes to do uh oh moments to other members of the squad. He relates very well with his monkey and ape brethren.\n")
                c.cyan('\nMoto: "Ayo fait attention sinon je vais te sucer les fesses >:)"')
                c.green("\nDominant trait: Attack\n")
                pressEnter()
                player = Hussein()
                print(player)
                if confirm() == True:
                    break

                b.battle(Hussein(), Hadi())
            case _:
                c.red("Please input a number displayed.")        
                time.sleep(1.5)
    save(slotSelection, player)

def autosave():
    slowType("Preforming an autosave, just a moment...\n")
    time.sleep(0.5)
    with open("LAL_saveSlots/slot"+slotSelection+".txt") as save_file:
        data = json.load(save_file)
        for i in data['player']: player = i['character'];
    player += "()"
    print(player)
    save(slotSelection, player)

def save(slot, self='blank', newFile=False):
    save = {}
    save['player'] = []
    save['progression'] = []
    if newFile == True:
        slowType("Creating save file... ")
        save['player'].append({
        'character': 'blank',
        'level': '0',
        'xp': '0',
        'hp': '0',
        'attack': '0',
        'defence': '0',
        'charisma': '0',
        'intellect': '0',
        'agility': '0',
        })
    else:
        slowType("Do not turn off the power. Saving your progress... ")
        print(self)
        save['player'].append({
        'character': self.name,
        'level': self.level,
        'xp': self.xp,
        'hp': self.hp,
        'attack': self.attack,
        'defence': self.defence,
        'charisma': self.charisma,
        'intellect': self.intellect,
        'agility': self.agility,
        })

    with open("LAL_saveSlots/slot"+slot+'.txt', 'w') as outfile:
        json.dump(save, outfile)
    time.sleep(1) #simulates saving time (we just have so little data to save..)
    slowType("All done.")


def stats(self):
    atStat = "Attack:    "
    for i in range(self.attack):
        atStat += "■"
        if self.attack >= 10:
            atStat = "Attack:    \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.attack):
        atStat += "-"
    defStat = "Defence:   "
    for i in range(self.defence):
        defStat += "■"
        if self.defence >= 10:
            defStat = "Defence:   \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.defence):
        defStat += "-"
    charStat = "Charisma:  "
    for i in range(self.charisma):
        charStat += "■"
        if self.charisma >= 10:
            charStat = "Charisma:  \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.charisma):
        charStat += "-"
    intStat = "Intellect: "
    for i in range(self.intellect):
        intStat += "■"
        if self.intellect >= 10:
            intStat = "Intellect: \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.intellect):
        intStat += "-"
    agStat = "Agility:   "
    for i in range(self.agility):
        agStat += "■"
        if self.agility >= 10:
            agStat = "Agility:   \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.agility):
        agStat += "-"
    return str("Player Stats:\n\n"+atStat+"\n"+defStat+"\n"+charStat+"\n"+intStat+"\n"+agStat+"\nHealth Points: "+str(self.hp)+"\n")

def healthBar(self): #when you want to display someone's health, just do healthBar(player) for example
    hpAmount = self.name+'\'s HP:\n|'
    for i in range(self.hp//3):
        hpAmount += "■"
    for i in range((100 - self.hp)//3):
        hpAmount += "-"
    hpAmount += "| "+str(self.hp)+"%"
    print(hpAmount)

def xpBar(self, xp):
    xpAmountpre = '('
    xpAmountnew = ''
    xpAmountend = ''
    xpTotal = self.xp + xp
    for i in range(self.xp//2):
        xpAmountpre += "■"
    while xpTotal >= 100:
        self.level += 1
        xpTotal -= 100
        xp -= 100
    for i in range(xp//2):
        xpAmountnew += "□"
    for i in range((100 - xpTotal)//2):
        xpAmountend += "-"
    self.xp = xpTotal
    print(xpAmountpre+xpAmountnew+xpAmountend+") "+str(xpTotal)+"%\nCurrent level: "+str(self.level)+"\nLevel up in: "+str(100-xpTotal)+"xp")

class Adib():
    def __init__(self): #overall balanced
        screenClear()
        self.attack = 3
        self.defence = 3
        self.charisma = 2
        self.intellect = 2
        self.agility = 3
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Adib'
        self.moto = "Mumei best girl >:)"
    #def levelUp(self):
        #for i in self.stats:
            #i += 1

    def __repr__(self):
        return stats(self)
        
class Mathieu():
    def __init__(self): #dominant in defence
        screenClear()
        self.attack = 3
        self.defence = 5
        self.charisma = 1
        self.intellect = 2
        self.agility = 2
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Mathieu'
        self.moto = "Looks like I'm gonna have to Miracle Johnson on you."

    def __repr__(self):
        return stats(self)

class Jacob():
    def __init__(self): #dominant in agility
        screenClear()
        self.attack = 2
        self.defence = 1
        self.charisma = 3
        self.intellect = 2
        self.agility = 5
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Jacob'
        self.moto = "I'm gonna Dust-eze out of here, the fish are calling me. *SCREECH*"

    def __repr__(self):
        return stats(self)

class Ali():
    def __init__(self): #dominant in charisma
        screenClear()
        self.attack = 3
        self.defence = 3
        self.charisma = 5
        self.intellect = 0
        self.agility = 2
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Ali-Hassan'
        self.moto = "MY FEET ARE NUMB MAN! UEEEAAAAAAAHHHHHHHH!!"

    def __repr__(self):
        return stats(self)

class Hadi():
    def __init__(self): #dominant in intellect
        screenClear()
        self.attack = 3
        self.defence = 1
        self.charisma = 2
        self.intellect = 5
        self.agility = 2
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Hadi'
        self.moto = "I'm gonna have to finish you, I don't care about your #DISTAVIE."

    def __repr__(self):
        return stats(self)

class Hussein():
    def __init__(self): #dominant in attack
        screenClear()
        self.attack = 5
        self.defence = 2
        self.charisma = 2
        self.intellect = 1
        self.agility = 3
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Hussein'
        self.moto = "Ayo fait attention sinon je vais te sucer les fesses"

    def __repr__(self):
        return stats(self)

def levelUp(self):
    screenClear()
    slowType("Congratulations monke man, you have levelled up!")
    while True:
        slowType("What would you like to improve? You have one",level_point,"to spend.\n"
        "A --- ATK"
        "B --- DEF"
        "C --- INT"
        "D --- CHA"
        "E --- AGI")
        levelChoice=input()
        match levelChoice:
            case "a" | "atk" | "1":
                self.attack += 1
                slowType("You have levelled up your attack. Congratulations, may you clap the cheeks of your enemies. Your attack is now", self.attack,".")
                break
            case "b" | "def" | "2":
                self.defence += 1
                slowType("You have levelled up your defense. Congratulations, may you be able to tank more damage, you filthy masoschist. Your defense is now",self.attack,".")
                break
            case "c" | "int" | "3":
                self.intellect += 1
                slowType("You have levelled up your intellect. Congratulations, you are evolving from monke to ape, may your gorilla powers manifest themselves. Your intellect is now",self.intellect,".")
                break
            case "d" | "cha" | "4":
                self.charisma += 1
                slowType("You have levelled up your charisma. Congratulations, you sexy beast, the laws of physics bend to your way with words :flushed:. Your charisma is now",self.charisma,".")
                break
            case "e" | "agi" | "5":
                self.agility += 1
                slowType("You have levelled up your agility. Congratulations, you speedy boi, may you move faster than le jongleur eventually.",self.agility,".")
                break
            case _:
                c.red("Please select a valid option.")
                time.sleep(1.5)
                screenClear()
    pressEnter()
    screenClear()
    print(stats(player))
    pressEnter()
    screenClear()
