from time import sleep
from observer import Observer
import keyboard
import multiprocessing
from volibear import Volibear
from sett import Sett
from locator import Locator

if __name__ == '__main__':
    observer = Observer()
    championName = input('Enter champion name (Volibear/Sett): ')
    championSide = input('Enter what side of the map you are on (blue/red): ')
    if championName == "Volibear":
        champ = Volibear(championSide)
    if championName == "Sett":
        champ = Sett(championSide)
    locator = Locator(championSide)
    input('Press ENTER to start.')
    observer.Observe()
    sleep(3)
    champ.buyStartingItem()
    while(not keyboard.is_pressed('esc')):
        p_Observe = multiprocessing.Process(target=observer.Observe(),args=[])
        p_Act = multiprocessing.Process(target=champ.Act(observer.advantage, locator),args=[])
        p_Observe.start()
        p_Act.start()
        p_Observe.join()
        p_Act.join()
    print("Done")
    
