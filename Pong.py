
import turtle         #basic graphics for games

#window graphic for pong
windows = turtle.Screen()
windows.title("The Pong Game")
windows.bgcolor("black")
windows.setup(width = 1000 , height = 600)
windows.tracer(0)       #prevents the window from updating and speeds up gameplay


# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid = 5 , stretch_len = 1)#default shape is 20px by 20px
paddle1.penup()         #draw lines when moving
paddle1.goto(-350, 0)


# Paddle 2


# Ball


#Main game
while True:
    windows.update()      #everytime the loop runs, it updates the screen

