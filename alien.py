import pgzrun
import random
WIDTH = 400
HEIGHT = 400

a = Actor("alien")
a.x = 200
a.y = 200
s = ""
p = 0
c = "#843300"
def draw():
    screen.fill(c)
    a.draw()
    screen.draw.text("Shoot the alien.",(10,10))
    screen.draw.text(s,(260,10))
    screen.draw.text(str(p),(150,10))
def on_mouse_down(pos):
    global s,p,c
    if a.collidepoint(pos):
        a.x = random.randint(25,375)
        a.y = random.randint(25,375)
        s = "Nice shot!"
        p += 1
        if p >= 10:
            c = "#461B00"
    else:
        s = "That was a miss!"
        p -= 1

        



pgzrun.go()