import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import keyboard
import matplotlib.pyplot as plt
import numpy

c = numpy.array([])

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

clicks = 0
clickpow = 1

def getCookies():
    output = ""

    raw = driver.find_element(By.ID, "cookies").text
    run = True
    for c in raw:
        if c == " " or c == "\n":
            run = False
        if run:
            if c != ",":
                output += c
                    
    output = int(float(output))
    if "million cookies" in raw.lower():
        output *= 10**6
    if "billion cookies" in raw.lower():
        output *= 10**9
    return output

def getCps():
    output = ""

    raw = driver.find_element(By.ID, "cookies").text
    run = True
    for c in raw[raw.find("per second")+12]:
        if c == " " or c == "\n":
            run = False
        if run:
            if c != ",":
                output += c
                    
    output = int(float(output))
    if "million cookies" in raw.lower():
        output *= 10**6
    if "billion cookies" in raw.lower():
        output *= 10**9
    return output+1

def findImage(path):
    return pyautogui.locateOnScreen(path, confidence=0.6)

class Upgrade:
    def __init__(self, image, cost, type, condition):
        self.on = False
        self.cost = cost
        self.image = "upgrades/"+image
        self.amount = 0
        self.type = type
        self.condition = condition
        self.power = 0
        self.updateScore()
    def updateScore(self):
        global clicks
        if self.type == "cursor":
            self.power = (items[0].amount*items[0].power)*5
            if (not self.on and self.amount == 0) and items[0].amount > self.condition:
                self.on = True
                print("can get cursor upgrade for "+str(self.cost))
        elif self.type == "grandma":
            self.power = (items[1].amount*items[1].power)*5
            if (not self.on and self.amount == 0) and items[1].amount > self.condition:
                self.on = True
                print("can get grandma upgrade for "+str(self.cost))
        elif self.type == "farm":
            self.power = (items[2].amount*items[2].power)*5
            if (not self.on and self.amount == 0) and items[2].amount > self.condition:
                self.on = True
                print("can get farm upgrade for "+str(self.cost))
        elif self.type == "mine":
            self.power = (items[3].amount*items[3].power)*5
            if (not self.on and self.amount == 0) and items[3].amount > self.condition:
                self.on = True
                print("can get mine upgrade for "+str(self.cost))
        elif self.type == "factory":
            self.power = (items[4].amount*items[4].power)*5
            if (not self.on and self.amount == 0) and items[4].amount > self.condition:
                self.on = True
                print("can get factory upgrade for "+str(self.cost))
        elif self.type == "bank":
            self.power = (items[5].amount*items[5].power)*5
            if (not self.on and self.amount == 0) and items[5].amount > self.condition:
                self.on = True
                print("can get bank upgrade for "+str(self.cost))
        elif self.type == "clicking":
            self.power = getCps()*150
            if (not self.on and self.amount == 0) and clicks > self.condition:
                self.on = True
                print("can get clicking upgrade for "+str(self.cost))
        self.score = max(self.cost - getCookies(), 0)/getCps() + self.cost/max(self.power, 1)
    def buy(self):
        global clickpow
        size = pyautogui.size()
        r = (int(size[0]*0.8), 175, int(size[0]*0.2), 125)
        image = pyautogui.locateCenterOnScreen(self.image, confidence=0, region=r)
        pyautogui.moveTo(image[0], image[1])
        pyautogui.click()
        self.on = False
        self.amount = 1
        if self.type == "cursor":
            items[0].power *= 2
            clickpow *= 2
        elif self.type == "grandma":
            items[1].power *= 2
        elif self.type == "farm":
            items[2].power *= 2
        elif self.type == "mine":
            items[3].power *= 2
        elif self.type == "factory":
            items[4].power *= 2
        elif self.type == "bank":
            items[5].power *= 2
        elif self.type == "clicking":
            clickpow += getCps()*0.01

class Item:
    def __init__(self, image, cost, power, on=True, max=5000):
        self.on = on
        self.cost = cost
        self.image = "buildings/"+image
        self.power = power
        self.amount = 0
        self.max = max
        self.updateScore()
    def changeCost(self, cost=0):
        if cost == 0:
            cost = self.cost*1.15
        self.cost = cost
        self.updateScore()
    def updateScore(self):
        self.score = self.power/self.cost
        self.score = max(self.cost - getCookies(), 0)/getCps() + self.cost/self.power
    def buy(self):
        size = pyautogui.size()
        r = (int(size[0]*0.79), 320, int(size[0]*0.15), int(size[1])-300)
        pyautogui.screenshot("screenshot.png", r)
        image = pyautogui.locateCenterOnScreen(self.image, confidence=0.8, region=r)
        pyautogui.moveTo(image[0], image[1])
        pyautogui.click()
        self.amount += 1
        self.changeCost()

winsearch = findImage("winSearch.png")
pyautogui.moveTo(winsearch[0]+100, winsearch[1]+10)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite("livesplit", 0.2)
time.sleep(5)
open = findImage("open.png")
pyautogui.moveTo(open[0]+20, open[1]+20)
pyautogui.click()

time.sleep(2)
ingles = findImage("ingles.png")
pyautogui.moveTo(ingles[0]+100, ingles[1]+10)
pyautogui.click()
time.sleep(0.1)
pyautogui.hotkey("F11")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

time.sleep(1)
gotit = findImage("gotit.png")
pyautogui.moveTo(gotit[0]+10, gotit[1]+10)
pyautogui.click()
pyautogui.scroll(-360)

time.sleep(1)
livesplit = pyautogui.getWindowsWithTitle("LiveSplit")[0]
pyautogui.moveTo(livesplit.right-20, livesplit.top + 20)
pyautogui.dragTo(575, pyautogui.size()[1]+170, duration=0.3, button="left")

time.sleep(0.5)
name = findImage("cookietop.png")
pyautogui.moveTo(name[0]+50, name[1]+5)
pyautogui.click()
pyautogui.typewrite("PyAutoGUI", 0.2)

items = []
items.append(Item("cursor.png", 15, 0.1))
items.append(Item("grandma.png", 100, 1, False))
items.append(Item("farm.png", 1100, 8, False))
items.append(Item("mine.png", 12000, 47, False))
items.append(Item("factory.png", 130000, 260, False))
items.append(Item("bank.png", 1400000, 1400, False))
items.append(Item("temple.png", 20000000, 7800, False))
items.append(Item("wizard.png", 330000000, 44000, False))
items.append(Item("shipment.png", 5100000000, 260000, False))
items.append(Item("alchemy.png", 75000000000, 1600000, False))
items.append(Item("portal.png", 1000000000000, 10000000, False))
items.append(Upgrade("click1.png", 100, "cursor", 1))
items.append(Upgrade("click2.png", 500, "cursor", 1))
items.append(Upgrade("click3.png", 10000, "cursor", 10))
items.append(Upgrade("click4.png", 100000, "cursor", 25))
items.append(Upgrade("clack1.png", 50000, "clicking", 1000))
items.append(Upgrade("grand1.png", 1000, "grandma", 1))
items.append(Upgrade("grand2.png", 5000, "grandma", 5))
items.append(Upgrade("grand3.png", 50000, "grandma", 25))
items.append(Upgrade("grand4.png", 5000000, "grandma", 50))
items.append(Upgrade("farm1.png", 11000, "farm", 1))
items.append(Upgrade("farm2.png", 55000, "farm", 5))
items.append(Upgrade("farm3.png", 550000, "farm", 25))
items.append(Upgrade("farm4.png", 55000000, "farm", 50))
items.append(Upgrade("mine1.png", 120000, "mine", 1))
items.append(Upgrade("mine2.png", 600000, "mine", 5))
items.append(Upgrade("mine3.png", 6000000, "mine", 25))
items.append(Upgrade("fact1.png", 1300000, "factory", 1))
items.append(Upgrade("fact2.png", 6500000, "factory", 5))
items.append(Upgrade("fact3.png", 65000000, "factory", 25))
items.append(Upgrade("bank1.png", 14000000, "bank", 1))
items.append(Upgrade("bank2.png", 70000000, "bank", 5))

cookie = findImage("cookie.png")
# submits name and starts timer
pyautogui.hotkey("ENTER")

while True:
    pyautogui.moveTo(cookie[0]+200, cookie[1]+200)

    best = items[0]
    for i in items:
        i.updateScore()
        if i.score < best.score and i.on:
            best = i

    while getCookies() < best.cost+5:
        pyautogui.click()
        clicks += clickpow
        c = numpy.append(c, getCookies())
        if keyboard.is_pressed("q"):
            # quit
            pyautogui.hotkey("enter")
            stats = findImage("stats.png")
            pyautogui.moveTo(stats[0]+10, stats[1]+10)
            pyautogui.click()
            plt.xlabel("Time (Clicks)")
            plt.ylabel("Cookies")
            plt.plot(c)
            plt.show()
            time.sleep(10000)
        if keyboard.is_pressed("x"):
            # pause
            time.sleep(60)

    for i in items:
        if i.__class__.__name__ == "Item" and (not i.on) and getCookies() >= i.cost*0.6:
            i.on = True
            print("can get "+i.image+" for "+str(i.cost))
    
    #lol get it best buy
    time.sleep(0.2)
    best.buy()
    print("bought "+best.image+", have "+str(best.amount)+" now.")
    print()