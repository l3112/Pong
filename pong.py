# it's pong

import turtle

#make a window!
window = turtle.Screen()
window.title("Pong - l3112 from TokyoEdTech tutorial")
window.bgcolor("black") 
window.setup(width=800, height=600)
window.tracer(0) #stop auto updating

#SCOOOOORE!
score_a = 0
score_b = 0

#main game loop
# how it works


#game objects
#the sticks
# the square ball

# Paddle A
pad_a = turtle.Turtle()
#small is module, capital is class

pad_a.speed(0) #speed of animation, max
pad_a.shape("square") #should be square
pad_a.color("cyan")
pad_a.shapesize(stretch_wid=6,stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()

pad_b.speed(0) #speed of animation, max
pad_b.shape("square") #should be square
pad_b.color("cyan")
pad_b.shapesize(stretch_wid=6,stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("triangle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
#movement
ball.dx = 2
ball.dy = -2

#Ready Player One
# Pen from Turtle module/class
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup() #no middle
pen.hideturtle() #no line
pen.goto(0, 260)
pen.write("Player A: 0 |||| Player B: 0", align="center", font=("Courier", 24, "normal"))

#functions for paddle movement
def pad_a_up():
    y = pad_a.ycor() #returns y coordinate
    y += 20
    pad_a.sety(y) #set to new y

def pad_a_down():
    y = pad_a.ycor() #returns y coordinate
    y -= 20
    pad_a.sety(y) #set to new y


def pad_b_up():
    y = pad_b.ycor() #returns y coordinate
    y += 20
    pad_b.sety(y) #set to new y

def pad_b_down():
    y = pad_b.ycor() #returns y coordinate
    y -= 20
    pad_b.sety(y) #set to new y

# Keyboard Binding
window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "s")  

#for b
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")    




#this actually has to be last to work.
while True:
    window.update()

#move that ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#border checking

# could use os system to post sound
    #compare y coordinates
    #height is 600, width is 800
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    #left and right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} |||| Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} |||| Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


     # collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() -40):   
         ball.setx(340)
         ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() -40):   
         ball.setx(-340)
         ball.dx *= -1
