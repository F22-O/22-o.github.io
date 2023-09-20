import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.title("yourName")

T = turtle.Turtle()
T.color("black")
T.begin_fill()
# Draw
T.circle(100)
T.end_fill()

TB = turtle.Turtle()
TB.color("blue")
TB.up()
#move
TB.goto(0,50)
TB.down()
TB.begin_fill()
# Draw
TB.circle(50)
TB.end_fill()

turtle.done()
