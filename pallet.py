from graphics import *
import threading
import copy
import random
import math
import time

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

class Brick1:
    def __init__(self, point):
        self.posx = point.x
        self.posy = point.y
        self.Bricks = []
        self.isChecked = False
        self.createBrick()
        self.color = color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        #zero pionowo 1 poziomo
        self.state = 0

    def createBrick(self):
        for i in range(0, 4):
            self.Bricks.append(Rectangle(Point(self.posx,self.posy-i*10), Point(self.posx+10,self.posy-i*10+10)))

    def drawthis(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else: i.setFill(self.color)
            i.draw(win)

    def checkForClick(self, point):
        for i in self.Bricks:
            p1 = i.getP1()
            p2 = i.getP2()
            if point.x >= p1.x and point.x < p2.x:
                if point.y >= p1.y  and point.y < p2.y :
                    if self.isChecked == False:
                        self.isChecked = True
                        return True
                    else:
                        self.isChecked = False
                        return False

    def rotate(self,klocek,klocki,key):
        #obrot poziomo
        canRotate = True
        if self.state == 0 and (key == 'a' or key == 'd'):
            self.state = 1
            self.Bricks[0].move(-10,-20)
            self.Bricks[1].move(0,-10)
            self.Bricks[2].move(10,0)
            self.Bricks[3].move(20,10)
            for b in klocek.Bricks:
                if b.getCenter().x < 50 or b.getCenter().x > 200 or b.getCenter().y < 50 or b.getCenter().y > 300:
                    canRotate = False
            for b in klocek.Bricks:
                for l in klocki:
                    if l == klocek:
                        continue
                    else:
                        for s in l.Bricks:
                            if math.fabs(b.getCenter().x - s.getCenter().x) < 2 and math.fabs(
                                    b.getCenter().y - s.getCenter().y) < 2:
                                canRotate = False
                                break
            if not canRotate:
                self.state = 0
                self.Bricks[0].move(10, 20)
                self.Bricks[1].move(0, 10)
                self.Bricks[2].move(-10, 0)
                self.Bricks[3].move(-20, -10)

        elif self.state == 1 and (key == 'a' or key == 'd'):
            canRotate = True
            self.state = 0
            self.Bricks[0].move(10, 20)
            self.Bricks[1].move(0, 10)
            self.Bricks[2].move(-10, 0)
            self.Bricks[3].move(-20, -10)
            for b in klocek.Bricks:
                if b.getCenter().x < 50 or b.getCenter().x > 200 or b.getCenter().y < 50 or b.getCenter().y > 300:
                    canRotate = False
            for b in klocek.Bricks:
                for l in klocki:
                    if l == klocek:
                        continue
                    else:
                        for s in l.Bricks:
                            if math.fabs(b.getCenter().x - s.getCenter().x) < 2 and math.fabs(
                                    b.getCenter().y - s.getCenter().y) < 2:
                                canRotate = False
                                break
            if not canRotate:
                self.state = 1
                self.Bricks[0].move(-10, -20)
                self.Bricks[1].move(0, -10)
                self.Bricks[2].move(10, 0)
                self.Bricks[3].move(20, 10)


    def changeColour(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else: i.setFill(self.color)


class Brick2:
    def __init__(self, point):
        self.posx = point.x
        self.posy = point.y
        self.Bricks = []
        self.isChecked = False
        self.state = 0
        self.color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.createBrick()

    def createBrick(self):
        for i in range(0, 2):
            self.Bricks.append(Rectangle(Point(self.posx,self.posy-i*10), Point(self.posx+10,self.posy-i*10+10)))
        for i in range(0, 2):
            self.Bricks.append(Rectangle(Point(self.posx+10,self.posy-i*10), Point(self.posx+20,self.posy-i*10+10)))

    def drawthis(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else:
                i.setFill(self.color)
            i.draw(win)

    def checkForClick(self, point):
        for i in self.Bricks:
            p1 = i.getP1()
            p2 = i.getP2()
            if point.x >= p1.x and point.x < p2.x:
                if point.y >= p1.y and point.y < p2.y:
                    if self.isChecked == False:
                        self.isChecked = True
                        return True
                    else:
                        self.isChecked = False
                        return False

    def rotate(self, klocek, klocki, key):
        return


    def changeColour(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else:
                i.setFill(self.color)


class Brick3:
    def __init__(self, point):
        self.posx = point.x
        self.posy = point.y
        self.Bricks = []
        self.isChecked = False
        self.state = 0
        self.color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.createBrick()

    def createBrick(self):
        for i in range(0, 3):
            self.Bricks.append(Rectangle(Point(self.posx,self.posy-i*10), Point(self.posx+10,self.posy-i*10+10)))
        self.Bricks.append(Rectangle(Point(self.posx+10,self.posy-20),Point(self.posx+20,self.posy-10)))

    def drawthis(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else:
                i.setFill(self.color)
            i.draw(win)

    def checkForClick(self, point):
        for i in self.Bricks:
            p1 = i.getP1()
            p2 = i.getP2()
            if point.x >= p1.x and point.x < p2.x:
                if point.y >= p1.y and point.y < p2.y:
                    if self.isChecked == False:
                        self.isChecked = True
                        return True
                    else:
                        self.isChecked = False
                        return False

    def rotate(self, klocek, klocki, key):
        buff = self.state
        wrongRot = False
        if key != 'a' and key != 'd': return
        elif key == 'd':
            if self.state == 3: self.state = 0
            else: self.state += 1
            if self.state == 0:
                if not self.helpFunc(klocek, klocki,
                                     [Point(-10,10),Point(0,0),Point(10,-10),Point(20,0)]): wrongRot = True
            if self.state == 1:
                if not self.helpFunc(klocek, klocki,
                                     [Point(-10, -10), Point(0, 0), Point(10, 10), Point(0, 20)]): wrongRot = True
            if self.state == 2:
                if not self.helpFunc(klocek, klocki,
                                     [Point(10, -10), Point(0, 0), Point(-10, 10), Point(-20, 0)]): wrongRot = True
            if self.state == 3:
                if not self.helpFunc(klocek, klocki,
                                     [Point(10, 10), Point(0, 0), Point(-10, -10), Point(0, -20)]): wrongRot = True
        elif key == 'a':
            if self.state == 0:
                self.state = 3
            else:
                self.state -= 1
            if self.state == 0:
                if not self.helpFunc(klocek, klocki,
                                     [Point(10,10), Point(0, 0), Point(-10, -10), Point(0, -20)]): wrongRot = True
            if self.state == 1:
                if not self.helpFunc(klocek, klocki,
                                     [Point(-10, 10), Point(0, 0), Point(10, -10), Point(20, 0)]): wrongRot = True
            if self.state == 2:
                if not self.helpFunc(klocek, klocki,
                                     [Point(-10, -10), Point(0, 0), Point(10, 10), Point(0, 20)]): wrongRot = True
            if self.state == 3:
                if not self.helpFunc(klocek, klocki,
                                     [Point(10, -10), Point(0, 0), Point(-10, 10), Point(-20, 0)]): wrongRot = True

        if wrongRot:
            self.state = buff


    def helpFunc(self, klocek,klocki,Punkty):
        canMove = True
        for i, p in zip(klocek.Bricks, Punkty):
            i.move(p.x, p.y)
        for b in klocek.Bricks:
            if b.getCenter().x < 50 or b.getCenter().x > 200 or b.getCenter().y < 50 or b.getCenter().y > 300:
                canMove = False
        for b in klocek.Bricks:
            for l in klocki:
                if l == klocek:
                    continue
                else:
                    for s in l.Bricks:
                        if math.fabs(b.getCenter().x - s.getCenter().x) < 2 and math.fabs(
                                b.getCenter().y - s.getCenter().y) < 2:
                            canMove = False
                            break
        if not canMove:
            for i, p in zip(klocek.Bricks, Punkty):
                i.move(-p.x,-p.y)
            return False
        else: return True

    def changeColour(self):
        for i in self.Bricks:
            if self.isChecked:
                i.setFill('blue')
            else:
                i.setFill(self.color)




def MoveBrick(klocek, klocki, dir):
    if dir == 0: return
    canMove = True
    x=0
    y=0
    if dir == 1:
        x = -1
        y = 0
    elif dir == 2:
        x = 0
        y = -1
    elif dir == 3:
        x = 1
        y = 0
    elif dir == 4:
        x = 0
        y = 1
    for i in klocek.Bricks:
        i.move(10*x,10*y)
    for b in klocek.Bricks:
        if b.getCenter().x < 50 or b.getCenter().x>200 or b.getCenter().y<50 or b.getCenter().y>300:
            canMove = False
    for b in klocek.Bricks:
        for l in klocki:
            if l == klocek:
                continue
            else:
                for s in l.Bricks:
                    if math.fabs(b.getCenter().x - s.getCenter().x)<2 and math.fabs(b.getCenter().y-s.getCenter().y)<2:
                        canMove = False
                        break
    if canMove:
        return True
    else:
        for i in klocek.Bricks:
            i.move(-10*x,-10*y)
        return False


def GetDir(key):
    if key == 'Left':
        return 1
    elif key == 'Right':
        return 3
    elif key == 'Down':
        return 4
    elif key == 'Up':
        return 2
    else: return 0

def createGame():
    klocki = []
    xpos = 50
    ypos = 80
    for i in range(0, 5):
        xpos = 60 + (i % 2) * 30
        for j in range(0, 3):
            n = random.randint(0, 2)
            if n == 0:
                klocki.append(Brick1(Point(xpos, ypos + 40)))
            elif n == 1:
                klocki.append(Brick2(Point(xpos, ypos + 40)))
            else:
                klocki.append(Brick3(Point(xpos, ypos + 40)))
            xpos += 40
            n = random.randint(0, 4)
            for rot in range(n):
                klocki[-1].rotate(klocki[-1], klocki, 'd')
        ypos += 40
    return klocki


def MoveToTarget(klocek,klocki,target):
    while not(math.fabs(klocek.Bricks[0].getP1().x - target.x) < 2):
        time.sleep(0.05)
        if klocek.Bricks[0].getP1().x - target.x > 0:
            if not MoveBrick(klocek,klocki,1):
                MoveBrick(klocek,klocki,2)
        else:
            if not MoveBrick(klocek,klocki,3):
                MoveBrick(klocek,klocki,2)

    while not (math.fabs(klocek.Bricks[0].getP1().y - target.y) < 2):
        time.sleep(0.05)
        MoveBrick(klocek,klocki,2)


def Place(klocki):
    B1 = None
    B2 = None
    B3 = None
    lastB1 = []
    lastB2 = []
    lastB3 = []
    Target = Point(0,0)
    placeFound = False
    Cubes = [[0,0,0,0]]
    for i in klocki:
        while i.state != 0:
            time.sleep(0.25)
            i.rotate(i,klocki,'d')
    for i in klocki:
        if isinstance(i,Brick1):
            while i.state != 0:
                time.sleep(0.05)
                i.rotate(i,klocki,'d')
            if B1 == None:
                c = 0
                x = 0
                for c in range(len(Cubes)):
                    for x in range(0, 4):
                        if c > 1 and Cubes[c - 2][x] == 0:
                            continue
                        elif Cubes[c][x] == 0 and x % 2 == 0:
                            placeFound = True
                            lastB1 = [c,x]
                            Cubes[c][x] = 1
                            B1 = Point(60 + x * 10 + (c % 2 * 40), 80 + math.floor(c / 2) * 40)
                            Target = Point(B1.x - 10, B1.y)
                            break
                if not placeFound:
                    Cubes.append([0,0,0,0])
                    for c in range(len(Cubes)):
                        for x in range(0, 4):
                            if c > 1 and Cubes[c - 2][x] == 0:
                                continue
                            elif Cubes[c][x] == 0 and x % 2 == 0:
                                placeFound = True
                                lastB1 = [c,x]
                                Cubes[c][x] = 1
                                B1 = Point(60 + x * 10 + (c % 2 * 40), 80 + math.floor(c / 2) * 40)
                                Target = Point(B1.x - 10, B1.y)
                                break
            else:
                Cubes[lastB1[0]][lastB1[1]+1] = 1
                Target = B1
                B1 = None
            MoveToTarget(i,klocki,Target)
            placeFound = False

        if isinstance(i,Brick2):
            if B2 == None:
                for c in range(len(Cubes)):
                    for x in range(0, 4):
                        if c > 1 and Cubes[c - 2][x] == 0:
                            continue
                        elif Cubes[c][x] == 0 and x % 2 == 0:
                            placeFound = True
                            Cubes[c][x] = 1
                            B2 = Point(50 + x * 10 + (c % 2 * 40), 80 + math.floor(c / 2) * 40)
                            Target = Point(B2.x , B2.y-20)
                            break
                if not placeFound:
                    Cubes.append([0,0,0,0])
                    for c in range(len(Cubes)):
                        for x in range(0, 4):
                            if c > 1 and Cubes[c - 2][x] == 0:
                                continue
                            elif Cubes[c][x] == 0 and x % 2 == 0:
                                placeFound = True
                                Cubes[c][x] = 1
                                B2 = Point(50 + x * 10 + (c % 2 * 40), 80 + math.floor(c / 2) * 40)
                                Target = Point(B2.x, B2.y-20)
                                break
            else:
                Target = B2
                B2 = None
            MoveToTarget(i,klocki,Target)
            placeFound = False

        if isinstance(i,Brick3):
            if B3 == None:
                while i.state != 0:
                    time.sleep(0.05)
                    i.rotate(i, klocki, 'd')
                for c in range(len(Cubes)):
                    for x in range(0, 4):
                        if c > 1 and Cubes[c - 2][x] == 0:
                            continue
                        elif Cubes[c][x] == 0 and x % 2 == 0:
                            placeFound = True
                            Cubes[c][x] = 1
                            B3 = Point(60 + x * 10 + (c % 2 * 40), 60 + math.floor(c / 2) * 40)
                            Target = Point(B3.x-10 , B3.y+10)
                            break
                if not placeFound:
                    Cubes.append([0,0,0,0])
                    for c in range(len(Cubes)):
                        for x in range(0, 4):
                            if c > 1 and Cubes[c - 2][x] == 0:
                                continue
                            elif Cubes[c][x] == 0 and x % 2 == 0:
                                placeFound = True
                                Cubes[c][x] = 1
                                B3 = Point(60 + x * 10 + (c % 2 * 40), 60 + math.floor(c / 2) * 40)
                                Target = Point(B3.x-10, B3.y+10)
                                break
            else:
                while i.state != 2:
                    time.sleep(0.05)
                    i.rotate(i, klocki, 'd')
                Target = B3
                B3 = None
            MoveToTarget(i,klocki,Target)
            placeFound = False


def play(klocki,win):
    klocki.clear()
    clear(win)
    klocki = createGame()
    rect.draw(win)
    for i in klocki:
        i.drawthis()
    Place(klocki)


win = GraphWin('Paleta', 250, 350) # give title and dimensions

sizeofRect = Point(150, 250)
StartPt = Point(50,50)
rect = Rectangle(StartPt, Point(StartPt.x+sizeofRect.x,StartPt.y+sizeofRect.y))
rect.draw(win)
klocki = createGame()
for i in klocki:
    i.drawthis()
p = Point(0, 0)
while True:
    key = win.checkKey()
    k = win.checkMouse()
    if k != None:
        p = k
        for i in klocki:
            if(i.checkForClick(p)):
                for j in klocki:
                    if i != j:
                        j.isChecked = False
            for z in klocki:
                z.changeColour()
    if key != None:
        for i in klocki:
            if i.isChecked:
                MoveBrick(i, klocki, GetDir(key))
                i.rotate(i,klocki,key)
                break
        if key == 'space': break

play(klocki,win)
win.getMouse()
win.close()



