import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    a=random.randrange(0,5)
    b=random.randrange(0,255)
    c=random.randrange(0,255)
    lst=['red','yellow','green','blue','black']
    turtle.colormode(255)
    t.color(a,b,c)
    t.fillcolor(a,b,c)
    
    if coin == 0:
        t.begin_fill()
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.end_fill()
    else:
        t.right(90)
        t.forward(50)
    #t.end_fill()

wn.exitonclick()