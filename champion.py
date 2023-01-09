from time import sleep
import win32api, win32con
import keyboard
import time

class Champion:
    def __init__(self, side):
        self.blueBase = (1665, 1060)
        self.redBase = (1900, 820)
        if side == "blue":
            self.allyBase = self.blueBase
            self.enemyBase = self.redBase
            self.run = (255,875)
        if side == "red":
            self.allyBase = self.redBase
            self.enemyBase = self.blueBase
            self.run = (1675,210)
        self.item = (960, 540)
        self.side = side
        self.backTimer = time.time()
        self.gameTimer = time.time()
        self.lvlQ = False
        self.lvlW = False
        self.lvlE = False
        self.doransSold = False

    def rightClick(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

    def leftClick(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def lvlUp(self):
        if self.lvlE == False:
            keyboard.press("ctrl+e")
            sleep(0.01)
            keyboard.release("e")
            self.lvlE = True
        if self.lvlQ == False:
            keyboard.press("ctrl+q")
            sleep(0.01)
            keyboard.release("q")
            self.lvlQ = True
        if self.lvlW == False:
            keyboard.press("ctrl+w")
            sleep(0.01)
            keyboard.release("w")
            self.lvlW = True
        keyboard.press("ctrl+r")
        sleep(0.01)
        keyboard.release("r")
        keyboard.press("ctrl+q")
        sleep(0.01)
        keyboard.release("q")
        keyboard.press("ctrl+w")
        sleep(0.01)
        keyboard.release("w")
        keyboard.press("ctrl+e")
        sleep(0.01)
        keyboard.release("e")
        keyboard.release("ctrl")
        sleep(0.01)

    def buyItem(self):
        keyboard.press("z")
        sleep(0.2)
        keyboard.release("z")
        sleep(0.1)
        self.rightClick(600,340)
        sleep(0.05)
        self.rightClick(665,340)
        sleep(0.05)
        self.rightClick(720,340)
        sleep(0.05)
        self.rightClick(775,340)
        sleep(0.05)
        self.rightClick(830,340)
        sleep(0.05)
        self.rightClick(885,340)
        sleep(0.05)
        self.rightClick(940,340)
        sleep(0.05)
        self.rightClick(600,460)
        sleep(0.05)
        self.rightClick(665,460)
        sleep(0.05)
        self.rightClick(720,460)
        sleep(0.05)
        self.rightClick(775,460)
        sleep(0.05)
        self.rightClick(830,460)
        keyboard.press("z")
        sleep(0.2)
        keyboard.release("z")

    def buyStartingItem(self):
        keyboard.press("z")
        sleep(0.2)
        keyboard.release("z")
        self.rightClick(610,577)
        sleep(0.05)
        self.rightClick(665,577)
        sleep(0.05)
        keyboard.press("z")
        sleep(0.2)
        keyboard.release("z")
    
    def moveBack(self):
        self.rightClick(self.allyBase[0],self.allyBase[1])

    def moveForward(self):
        self.rightClick(self.enemyBase[0],self.enemyBase[1])

    def useAbility(self,ability):
        keyboard.press(ability)
        sleep(0.01)
        keyboard.release(ability)

    