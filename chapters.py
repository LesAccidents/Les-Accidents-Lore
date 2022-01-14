import colours as c
from basics import screenClear, pressEnter, confirm, slowType
import time
from bigText import bigText
import sound

def c1():
    screenClear()
    c.cyan("Chapter 1: The Birth of a Mistake")
    pressEnter()
    screenClear()
    time.sleep(1)
    slowType("Imagine...\n\n", 0.1)
    time.sleep(1)
    slowType("..a place..\n\n", 0.1)
    time.sleep(1)
    slowType("..where \033[1;31;48mANYTHING\033[1;37;48m can happen.", 0.1)
    time.sleep(2)
    screenClear()
    time.sleep(0.5)
    slowType("Les Accidents Inc. proudly presents:\n", 0.1)
    time.sleep(2.9)
    sound.music("intro")
    bigText("LES ACCIDENTS:", "white", "doom")
    time.sleep(8.3)
    bigText("THE GAME", "red")
    time.sleep(0.5)
    pressEnter()

    #1.1
    slowType("During an ordinary afternoon during June 2019, two young teenagers struggled through quite the task, a summative for their art class. These two were Ali-Hassan and Adib. Both were (mistakenly) taken for intelligent individuals, but Art truely was an enemy to be reckoned with. As the panic began to settle in, the two called each other, eager for help (and immensely bored) with the project.")
    slowType("\n\033[1;34;48m***DISCORD CALL SOUND***\033[1;37;48m", 0.1)
    slowType("\nAdib: Did you do the art project?\nAli-Hassan: My guy I ain't gonna lie I didn't.\nAdib: Well then we should get to work.")
    slowType("\nAs the two worked (but mostly messed around), the task revealed itself to be quite the pain in the ass. Thus, one of our protagonists suggested a solution.")
    slowType("\nAdib: Mind if I add ")
    slowType("\n\033[1;36;48mMathieu?\n\033[1;37;48m")
    slowType("\nAli-Hassan: The more the merrier really.")
    slowType("\n\033[1;30;48mAnd so...\033[1;37;48m")
    pressEnter()
    screenClear()
    slowType("\n\033[1;34;48mLittle did those three know\033[1;37;48m")
    slowType("\n\033[1;36;48mThat a new entity had entered their lives. Some might call it by simple names, but above all, it was a mistake, or a series of mistakes. And as the French might call the mistakes (especially the existence of the members) leading up to the creation of this entity:\033[1;37;48m")
    pressEnter()
    screenClear()
    slowType("\n\033[1;32;48m'Les Accidents'\033[1;37;48m",0.1)
    slowType("\nAs dramatic as I made that sound, les Accidents wasn't very, how shall I saw, 'le épique', at the beginning. This was due to multiple factors, but mostly the inactivity of Ali-Hassan, who was indulged in SnapHaram :vomit:. However, regular activity in les Accidents (then known as DaSexyDudes)included, but was not limited to, furry jokes, Roblox and Thanos jokes, Roblox shittery, and Mathieu getting scarred, leaving, and request a reinvite an hour later (through this experience one can deduce that Mathieu is in fact a closet masochist). These activities continued for the duration of summer 2019.")
    #1.2.1
    slowType("\nThroughout the beginning of the sophomore year, the events in Les Accidents had sticken to the same pattern. However, it was the wish of the members to increase the activity of the group chat. Although Ali-Hassan had appeared more often and increased his gayness levels, the GC still felt a bit empty.")
    pressEnter()
    screenClear()
    slowType("\n\033[1;36;48mEnter our newest character:\033[1;37;48m",0.06)
    slowType("\n\033[1;31;48mHadi!\033[1;37;48m",0.1)
    slowType("\nHadi was at the time, a very energetic and positive, yet eccentric and monkeylike guy. It was hoped that his presence would reinvigorate the group chat. However, Hadi was unfortunately too bewitched by women, with a figure best left only mentionned as: 'The Witch'. Hadi couldn't provide any support, as he himself is said to have stated: 'L'amour, c'est du chocolat.' Unfortunately as stated by experts, he could not contribue to Les Accidents because 'he sinned more than Diego in Dora and the Lost City of Gold'.")
    #1.2.2
    pressEnter()
    screenClear()
    slowType("\nLater during the year however, another event happened that would shape the history of Les Accidents. As it happened this was also a project, but it was the history project.")
    slowType("\nIn this project, the members of Les Accidents, plus a certain Jacob, worked on a project that was quite important for their grade. To communicate they used a server, that although still existing, doesn't hold the same place as Les Accidents, called now by the name Travail Ardu. During the project, Les Accidents' wild behavior continued, with a most controversial event happening in which Ali-Hassan requested to use Mathieu's bathroom. The events following this aren't clear, and experts are divided. Some claim that the projectile shitting and explosivity of Ali-Hassan's dump severely damaged the bathroom, while others claim that this is false, stating it is defamation. This event remains unresolved to this day. Nonetheless, Les Accidents decided to add their team mate to the project.")
    pressEnter()
    screenClear()
    slowType("\n\033[1;36;48mAnd so enters our newest character:\033[1;37;48m",0.06)
    slowType("\n\033[1;33;48mJacob!\033[1;37;48m", 0.1)
    slowType("\nOnce Jacob joined, he was immediately greeted with a dubious image from a visual novel. The following conversation ensued:")
    slowType("\nJacob: Bro wtf\nAdib: It's nothing.")
    slowType("\nIf Jacob was concerned by this, he had hidden it well, perhaps too well and for too long.")
    slowType("Because slowly and surely", 0.06)
    slowType("\n\033[1;31;48mHe was consumed, vored, by Les Accidents\033[1;37;48m", 0.1)

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c2()

def c2():
    screenClear()
    c.cyan("Chapter 2: The Attack of the Virus")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c3()

def c3():
    screenClear()
    c.cyan("Chapter 3: Hussein's Trial")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c4()

def c4():
    screenClear()
    c.cyan("Chapter 4: The Civil War")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c5()

def c5():
    screenClear()
    c.cyan("Chapter 5: Mathieu's ASCENT")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the special issue?")
    if confirm() == True:
        csi()

def csi():
    screenClear()
    c.cyan("Special Issue: Cerial vs Milk")
    pressEnter()
    screenClear()
