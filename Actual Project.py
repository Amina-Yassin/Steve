print ()
import turtle
import random
x = input("What is the name of the Turtle?")
y = input("What is the name of the Second Turtle?")
def still_in_screen(w,t):
    left_edge = - w.window_width() / 2
    right_edge = w.window_width() / 2
    top_edge = w.window_height() / 2
    bottom_edge = - w.window_height() / 2
 
    turtleX = t.xcor()
    turtleY = t.ycor()
 
    stillIn = True
    if turtleX > right_edge or turtleX <left_edge:
        stillIn = False
    if turtleY > top_edge or turtleY < bottom_edge:
        stillIn = False
 
    return stillIn
 
scr = turtle.Screen()
x = turtle.Turtle()
y = turtle.Turtle()
x.shape("turtle")
 
while still_in_screen(scr, x): #runs the loop as long as still_in_screen functions returns TRUE
    coin = random.randrange (0,3)
    if coin == 0:
        x.left(90)
        x.forward(50)
        y.right(90)
        y.forward(50)
    if coint == 2:
        x.left(90)
        x.forward(50)
        y.right(90)
        y.forward(50)
    else:
        x.right(90)
        x.forward(50)

print (x)
scr.exitonclick()
