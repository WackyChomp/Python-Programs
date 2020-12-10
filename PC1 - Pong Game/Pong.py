
import turtle         #basic graphics for games
import winsound       #adding sound

#window graphic for pong
windows = turtle.Screen()
windows.title("The Pong Game")
windows.bgcolor("black")
windows.setup(width = 1000 , height = 600)
windows.tracer(0)       #prevents the window from updating and speeds up gameplay


# Score
score1 = 0
score2 = 0


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
ball.dx = 0.2     #separate the ball into two movements x and y. Ball moves by pixels. Dependent on computer speed
ball.dy = 0.2         # + bounces up and - bounces down


# Pen (Shows the scoreboard)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Hero: 0     Villian: 0", align = "center" , font =("Courier", 24, "normal"))

# Function
def paddle1_up():
    y = paddle1.ycor()           #return y coordinates
    y += 20          #add to pixel
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20          #subract from pixel
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)   
    

# Keyboard binding / Function being called
windows.listen()
windows.onkeypress(paddle1_up, "w")
windows.onkeypress(paddle1_down, "s")
windows.onkeypress(paddle2_up, "Up")
windows.onkeypress(paddle2_down, "Down")


#Main game
while True:
    windows.update()      #everytime the loop runs, it updates the screen

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)        #combines current ball coordinates and pixel movement
    ball.sety(ball.ycor() + ball.dy) 

    #Border boundary
    if ball.ycor() > 290:
        ball.sety(290)      #ball bounces when it touches the top or bottom of the screen
        ball.dy *= -1       #reverses the direction when the ball hits the boundary
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)      #sound for top

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)       #sound for bottom

    if ball.xcor() > 390:
        ball.goto(0, 0)     #ball returns to the center of the screen after going to the left or right of the screen
        ball.dx *= -1       #reverses the direction when the ball hits the boundary
        score1 += 1
        pen.clear()         #replace previous number point
        pen.write("Hero: {}  Villian: {}".format(score1, score2), align = "center" , font =("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()            #replace previous number point
        pen.write("Hero: {}  Villian: {}".format(score1, score2), align = "center" , font =("Courier", 24, "normal"))


    #Collision between paddle and ball
    #Paddle2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)      #sound for right paddle

    #Paddle1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)      #sound for left paddle