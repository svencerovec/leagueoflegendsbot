from windowcapture import WindowCapture
from vision import Vision
import multiprocessing

class Locator:
    def __init__(self, side):
        self.wincap = WindowCapture()
        self.screenshot = self.wincap.get_screenshot()
        self.side = side

        self.vision_enemyMinion = Vision('enemyMinionHP.png')
        self.vision_enemyChampion = Vision('enemyHP.png')
        self.vision_enemyTurret = Vision('enemyTurretHP.png')
        self.vision_enemyTurretPlate = Vision('enemyTurretHPplate.png')
        self.vision_shop = Vision('shop.png')
        self.vision_settUlt = Vision('settUlt.png')
        self.vision_voliUlt = Vision('voliUlt.png')
        self.vision_dead = Vision('dead.png')
        
        self.enemyMinionPosition = multiprocessing.Array('i', 2)
        self.enemyChampionPosition = multiprocessing.Array('i', 2)
        self.enemyTurretPosition = multiprocessing.Array('i', 2)

        self.enemyMinions = []
        self.enemyChampions = []
        self.enemyTurrets = []
        self.enemyTurretsP = []

    def LocateEnemyMinion(self):
        self.GetScreenshot()
        self.enemyMinions = self.vision_enemyMinion.find(self.screenshot, 0.95)
        if len(self.enemyMinions):
            if self.side == "blue":
                self.enemyMinionPosition[0] = self.enemyMinions[len(self.enemyMinions)-1][0]+30
                self.enemyMinionPosition[1] = self.enemyMinions[len(self.enemyMinions)-1][1]+60
            if self.side == "red":
                self.enemyMinionPosition[0] = self.enemyMinions[0][0]+30
                self.enemyMinionPosition[1] = self.enemyMinions[0][1]+60

    def LocateEnemyChampion(self):
        self.GetScreenshot()
        self.enemyChampions = self.vision_enemyChampion.find(self.screenshot,0.95)
        if len(self.enemyChampions):
            self.enemyChampionPosition[0] = self.enemyChampions[len(self.enemyChampions)-1][0]+50
            self.enemyChampionPosition[1] = self.enemyChampions[len(self.enemyChampions)-1][1]+120

    def LocateEnemyTurret(self):
        self.GetScreenshot()
        self.enemyTurrets = self.vision_enemyTurret.find(self.screenshot,0.95)
        if len(self.enemyTurrets):
            self.enemyTurretPosition[0] = self.enemyTurrets[len(self.enemyTurrets)-1][0]+75
            self.enemyTurretPosition[1] = self.enemyTurrets[len(self.enemyTurrets)-1][1]+150
            return
        self.GetScreenshot()
        self.enemyTurretsP = self.vision_enemyTurretPlate.find(self.screenshot,0.95)
        if len(self.enemyTurretsP):
            self.enemyTurretPosition[0] = self.enemyTurretsP[len(self.enemyTurretsP)-1][0]+75
            self.enemyTurretPosition[1] = self.enemyTurretsP[len(self.enemyTurretsP)-1][1]+150
            return
        self.enemyTurretPosition[0] = 0
        self.enemyTurretPosition[1] = 0
    
    def shopIsOpen(self):
        self.GetScreenshot()
        if len(self.vision_shop.find(self.screenshot,0.95)):
            return True
        return False
    
    def SettUltimateReady(self):
        if len(self.vision_settUlt.find(self.screenshot,0.95)):
            return True
        return False
    def VoliUltimateReady(self):
        if len(self.vision_voliUlt.find(self.screenshot,0.95)):
            return True
        return False

    def GetScreenshot(self):
        self.screenshot = self.wincap.get_screenshot()


