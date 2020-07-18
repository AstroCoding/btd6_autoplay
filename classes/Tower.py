from pyautogui import click, press, moveTo, locateOnScreen, center, size
from time import sleep

class Tower:
    def __init__(self, hotkey, image, conf, name):
        self.hotkey = hotkey
        self.pos = self.getPos(image, conf)
        self.name = name
        self.path = [0,0,0]

    def getPos(self, image, conf=0.3):
        location = locateOnScreen(image, confidence=conf)
        if location == None:
            return None
        locationCenter = center(location)
        return locationCenter

    def place(self):
        print(f'{self.name}: Place')
        press(self.hotkey)
        sleep(0.1)
        moveTo(self.pos)
        click()

    def select(self):
        print(f'{self.name}: Select')
        moveTo(self.pos)
        click()
        sleep(0.2)

    def upgrade(self, path):
        if path == ',':
            self.path[0] += 1
        elif path == '.':
            self.path[1] += 1
        elif path == '/':
            self.path[2] += 1
        print(f"{self.name}: Upgrade | {'|'.join(self.path)}")
        moveTo(self.pos)
        click()
        sleep(0.2)
        press(path)
        sleep(0.2)