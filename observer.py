from windowcapture import WindowCapture
from vision import Vision
import multiprocessing

class Observer:
    def __init__(self):
        self.wincap = WindowCapture()

        self.vision_enemyMinion = Vision('enemyMinionHP.png')
        self.vision_enemyChampion = Vision('enemyHP.png')
        self.vision_allyMinion = Vision('alliedMinionHP.png')
        self.vision_allyChampion = Vision('alliedChampion.png')

        self.screenshot = self.wincap.get_screenshot()
        self.array = multiprocessing.Array('i', 4)
        self.advantage = multiprocessing.Value('i', 0)

    def Observe(self):
        self.GetScreenshot()
        p_getEnemyMinions = multiprocessing.Process(target=self.GetEnemyMinions,args=[])
        p_getEnemyChampions = multiprocessing.Process(target=self.GetEnemyChampions,args=[])
        p_getAllyMinions = multiprocessing.Process(target=self.GetAllyMinions,args=[])
        p_getAllyChampions = multiprocessing.Process(target=self.GetAllyChampions,args=[])

        p_getEnemyChampions.start()
        p_getEnemyMinions.start()
        p_getAllyMinions.start()
        p_getAllyChampions.start()

        p_getEnemyChampions.join()
        p_getEnemyMinions.join()
        p_getAllyMinions.join()
        p_getAllyChampions.join()

        self.advantage = 0 - self.array[0] - (self.array[1]*3) + self.array[2] + (self.array[3]*3)

    def GetEnemyMinions(self):
        self.array[0] = len(self.vision_enemyMinion.find(self.screenshot,0.95))

    def GetEnemyChampions(self):
        self.array[1] = len(self.vision_enemyChampion.find(self.screenshot,0.95))

    def GetAllyMinions(self):
        self.array[2] = len(self.vision_allyMinion.find(self.screenshot,0.95))

    def GetAllyChampions(self):
        self.array[3] = len(self.vision_allyChampion.find(self.screenshot,0.95))

    def GetScreenshot(self):
        self.screenshot = self.wincap.get_screenshot()


