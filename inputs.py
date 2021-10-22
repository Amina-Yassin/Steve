import random
import turtle
print ("""Hello. Thank you for playing the Turtle Escape Game TM by RodmanShop Inc.
    We shall now begin the game. 
    Ay bets should be placed at this time with the attendant on your left.""")
print()

Tur1 = input ("Please enter the name of your first turtle in the race.")
Tcolor = input ("Please enter the colour of your turtle.")
Tur2 = input("Please enter of the 2nd competitor Turtle.")
Tcolor2 = input ("Please enter the colour you wish the second turtle to take on.")

def still_in_screen(w,t,t2):
    left_edge = - w.window_width() / 2
    right_edge = w.window_width() / 2
    top_edge = w.window_height() / 2
    bottom_edge = - w.window_height() / 2
 
    turtleA = t.xcor()
    turtleB = t.ycor()
    turtleC = t2.xcor()
    turtleD = t2.ycor()
    
    stillIn = True
    if turtleA > right_edge or turtleA <left_edge:
        stillIn = False
    if turtleB > top_edge or turtleB < bottom_edge:
        stillIn = False
    if turtleC > right_edge or turtleC <left_edge:
        stillIn = False
    if turtleD > top_edge or turtleD < bottom_edge:
        stillIn = False 
    return stillIn

arena = turtle.Screen()
arena.setup (width=800, height=800)
Tur1 = turtle.Turtle()
Tur2 = turtle.Turtle()
Ref = turtle.Turtle()
Ref.color("black")
Ref.pensize(10)
Tur1.color(Tcolor)
Tur2.color(Tcolor2)
Tur1.shape("turtle")
Tur1.pensize(3)
Tur2.pensize(3)
Tur2.shape("turtle")
arena.bgcolor("Tan")


def playingarea (r):
    r.penup()
    r.goto(800,-800)
    r.right(90)
    r.pendown()
    for loop in range(4):
        r.left(90)
        r.forward(770)


playingarea(Ref)

while still_in_screen(arena,Tur1,Tur2):
    coin = random.randrange (0,3)
    angle = random.randrange (0,360)
    if coin == 1:
        Tur1.left(angle)
        Tur1.forward(50)
        Tur2.right(angle)
        Tur2.forward(50)
    if coin == 2:
        Tur1.right(angle)
        Tur1.forward(50)
        Tur2.left(angle)
        Tur2.forward(50)
    else:
        Tur1.right(angle)
        Tur1.forward(50)
        Tur2.right(angle)
        Tur2.backward(50)


arena.exitonclick()