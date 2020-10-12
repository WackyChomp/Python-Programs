
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
paddle1.goto(-350, 0)       #left side


# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid = 5 , stretch_len = 1)#default shape is 20px by 20px
paddle2.penup()         #draw lines when moving
paddle2.goto(350, 0)       #right side


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)          #center of screen


#Main game
while True:
    windows.update()      #everytime the loop runs, it updates the screen

