print ()
import turtle
import random
 
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
 
win = turtle.Screen()
al = turtle.Turtle()
al.shape("turtle")
 
while still_in_screen(win, al): #runs the loop as long as still_in_screen functions returns TRUE
    coin = random.randrange (0,2)
    if coin == 0:
        al.left(90)
        al.forward(50)
    else:
        al.right(90)
        al.forward(50)
 
win.exitonclick()
