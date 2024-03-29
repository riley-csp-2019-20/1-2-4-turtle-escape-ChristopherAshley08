#===================turtles===================

import turtle as trtl
joe=trtl.Turtle()
joe._delay(0)
import random
import turtle as player
player=player.Turtle()
import turtle as clickcount
clickcount=clickcount.Turtle

#===================variables===================

numwalls= 120
pencolor = "red"
distancewall=600 
wall_width = 5
door_width=10

#===================setup===================

joe.speed(0)
joe.pencolor(pencolor)
joe.pensize(5)
joe.ht()
joe.penup()
joe.goto(300,300)
joe.right(90)
joe.pendown()

player.pencolor("blue")
player.pensize(1)
player.speed(0)
player.ht()

clicks = 0
eraser=0

#===================def====================

def drawdoor():
    joe.penup()
    joe.forward(door_width)
    joe.pendown()

def drawbarrier():
    joe.right(90)
    joe.forward(door_width)
    joe.backward(door_width)
    joe.left(90)

def up():
    player.setheading(90)
    player.forward(1)

def right():
    player.setheading(0)
    player.forward(1)

def left():
    player.setheading(180)
    player.forward(1)

def down():
    player.setheading(90*3)
    player.forward(1)

def erase():
    global eraser
    if eraser == 0:
        player.pencolor("white")
        eraser = 1
    else:
        player.pencolor("blue")
        eraser = 0

#===================code====================

for i in range(numwalls):
    if i < numwalls - 5:
        door = random.randint(door_width, distancewall - 2*door_width)#new

        barrier= random.randint(2*wall_width, distancewall - 2*door_width)#new

        if door<barrier:#NEW
            joe.forward(door)#NEW
            drawdoor()
            joe.forward(barrier - door - door_width)#NEW
            drawbarrier()
            joe.forward(distancewall - barrier)#NEW
        else:
            joe.forward(barrier)#NEW
            drawbarrier()
            joe.forward(door - barrier)#NEW
            drawdoor()
            joe.forward(distancewall - door - door_width)#NEW

    joe.right(90)
    distancewall = distancewall - wall_width

#===================wn===================

wn = trtl.Screen()

wn.onkeypress(up,"w")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")
wn.onkeypress(right,"d")
wn.onkeypress(up,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(erase,"e")
wn.listen()

wn.mainloop()
