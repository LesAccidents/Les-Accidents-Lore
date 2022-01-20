import os
from playsound import playsound
import winsound

def stop(): #abreviated function to stop music
    winsound.PlaySound(None, winsound.SND_PURGE)

def music(file, loop = 0): #function to play music >:)
    audioFile = os.path.dirname(__file__) + "\\music\\" + file + ".wav"
    print(str(audioFile))
    if loop == 1:
        winsound.PlaySound(audioFile, winsound.SND_LOOP + winsound.SND_ASYNC)
    else:
        winsound.PlaySound(audioFile, winsound.SND_ASYNC)
