from time import sleep
import win32api, win32con
import keyboard
from champion import Champion
from vision import Vision
from observer import Observer
import multiprocessing
import pyautogui
import time

class Volibear(Champion):
    def Combo(self, locator):
        elapsed = time.time() - self.gameTimer
        if elapsed > 600:
            self.useAbility("q")
            locator.LocateEnemyChampion()
            self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
            self.useAbility("e")
            if locator.VoliUltimateReady():
                self.useAbility("r")
                sleep(0.5)
                locator.LocateEnemyChampion()
                win32api.SetCursorPos((locator.enemyChampionPosition[0],locator.enemyChampionPosition[1]))
            sleep(0.5)
            locator.LocateEnemyChampion()
            win32api.SetCursorPos((locator.enemyChampionPosition[0],locator.enemyChampionPosition[1]))
            self.useAbility("w")
            sleep(0.1)
            locator.LocateEnemyChampion()
            win32api.SetCursorPos((locator.enemyChampionPosition[0],locator.enemyChampionPosition[1]))
            self.useAbility("d")
            self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
        else:
            self.lvlUp()
            self.useAbility("2")
            self.useAbility("q")
            locator.LocateEnemyChampion()
            self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
            self.useAbility("e")
            sleep(0.5)
            locator.LocateEnemyChampion()
            win32api.SetCursorPos((locator.enemyChampionPosition[0],locator.enemyChampionPosition[1]))
            self.useAbility("w")
            self.useAbility("d")
            self.moveBack()
    def Act(self, advantage, locator):
        pixelLowHP = pyautogui.screenshot().getpixel((841, 1053))
        if pixelLowHP == (1, 13, 7) or time.time() - self.backTimer >= 300:
            self.rightClick(self.run[0], self.run[1])
            locator.LocateEnemyChampion()
            locator.LocateEnemyMinion()
            while(len(locator.enemyChampions) > 0 or len(locator.enemyMinions) > 0):
                self.rightClick(self.run[0], self.run[1])
                self.useAbility("f")
                sleep(0.5)
                locator.LocateEnemyChampion()
                locator.LocateEnemyMinion()
            self.useAbility("b")
            sleep(9)
            self.buyItem()
            self.backTimer = time.time()
            sleep(6)
        if locator.shopIsOpen():
            if not self.doransSold and time.time() - self.gameTimer > 1200:
                self.doransSold = True
                self.rightClick(1090,1010)
            self.buyItem()
        self.lvlUp()
        for i in range(3):
            locator.LocateEnemyTurret()
            if advantage >= 10:
                if len(locator.enemyTurrets) | len(locator.enemyTurretsP):
                    self.rightClick(locator.enemyTurretPosition[0], locator.enemyTurretPosition[1])
                    sleep(0.2)
                    continue
                locator.LocateEnemyChampion()
                if len(locator.enemyChampions):
                    self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
                    self.Combo(locator)
                    sleep(0.2)
                    continue
                locator.LocateEnemyMinion()
                if len(locator.enemyMinions):
                    self.rightClick(locator.enemyMinionPosition[0], locator.enemyMinionPosition[1])
                    sleep(0.2)
                    continue
                self.moveForward()
                sleep(0.2)
                continue
            locator.LocateEnemyTurret()
            if len(locator.enemyTurrets) | len(locator.enemyTurretsP):
                self.moveBack()
                sleep(0.2)
                continue
            if advantage >= 3:
                locator.LocateEnemyChampion()
                if len(locator.enemyChampions):
                    self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
                    self.Combo(locator)
                    sleep(0.2)
                    continue
                locator.LocateEnemyMinion()
                if len(locator.enemyMinions):
                    self.rightClick(locator.enemyMinionPosition[0], locator.enemyMinionPosition[1])
                    sleep(0.2)
                    continue
                self.moveForward()
                sleep(0.2)
                continue
            if advantage >= -1:
                locator.LocateEnemyTurret()
                if len(locator.enemyTurrets) | len(locator.enemyTurretsP):
                    self.moveBack()
                    sleep(0.2)
                    continue
                locator.LocateEnemyMinion()
                if len(locator.enemyMinions):
                    self.rightClick(locator.enemyMinionPosition[0], locator.enemyMinionPosition[1])
                    sleep(0.2)
                    continue
                locator.LocateEnemyChampion()
                if len(locator.enemyChampions):
                    self.rightClick(locator.enemyChampionPosition[0], locator.enemyChampionPosition[1])
                    self.Combo(locator)
                    sleep(0.2)
                    continue
                self.moveForward()
                sleep(0.2)
                continue
            self.moveBack()
            sleep(0.2)
            self.useAbility("s")
            