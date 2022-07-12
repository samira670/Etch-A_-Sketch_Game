from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(10)


def  backward():

    timmy.backward(10)


def clockwise():
    define_angel =timmy.heading()
    timmy.setheading(define_angel-5)


def unclockwise():
    define_angel =timmy.heading()
    timmy.setheading(define_angel+5)

def clear():
    screen.reset()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "a")
screen.onkey(unclockwise, "d")
screen.onkey(clear, "c")


#Press w = forward
#Press s = backward
#Press a = counter_clockwise
#press d = clock_wise
#Press c = clear
















screen.exitonclick()