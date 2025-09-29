import turtle
import random
import time
delay=0.1
sc=0
hs=0


#creating a body of a snake
bodies=[]
#creating a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("light Green")
s.setup(width=600,height=600)

#creating head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.direction="stop"


#creating snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.fillcolor("brown")
food.penup()
food.ht()   #for hiding turtle
food.goto(250,260)
food.st()   #for show turtle

#scoreboard
sb=turtle.Turtle()
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score:0  |  Highest Score:0")


def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#event handling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")


#mainloop
while True:
    s.update()   #to update screen
    #check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)


    #check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        body=turtle.Turtle()  #increase the length of the snake body
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)
        sc=sc+10     #increase scorboard
        delay=delay-0.001  #change delay
        if sc>hs:
            hs=sc
        sb.clear()
        sb.write("Score:{}  |  Highest Score:{}".format(sc,hs))
        #move snake bodies
    for index in range(len(bodies)-1,0,-1):
            x=bodies[index-1].xcor()
            y=bodies[index-1].ycor()
            bodies[index].goto(x,y)
    if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
    move()
#check collision with snake body--
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for body in bodies:  #hide bodies
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score:{}  |  Highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()
    













        
