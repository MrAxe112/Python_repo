import turtle
import time


class TrafficLight:
    def __init__(self, colour='red'):
        self.__colour = colour

    def running(self, t1, t2, t3):
        while True:
            if self.__colour == "green":
                t2.fillcolor((178, 190, 181))
                t1.fillcolor((102, 204, 0))
                time.sleep(5)
                self.__colour = "red"
            elif self.__colour == "yellow":
                t3.fillcolor((178, 190, 181))
                t2.fillcolor((255, 255, 51))
                time.sleep(2)
                self.__colour = "green"
            elif self.__colour == "red":
                t3.fillcolor((227, 0, 34))
                t1.fillcolor((178, 190, 181))
                time.sleep(7)
                self.__colour = "yellow"


def draw_body():
    turtle_1.goto(-50, -50)
    turtle_1.pensize(2)
    turtle_1.color('black', 'white')
    turtle_1.begin_fill()
    turtle_1.right(90)
    turtle_1.circle(40, 180)
    turtle_1.forward(150)
    turtle_1.circle(40, 180)
    turtle_1.forward(150)
    turtle_1.left(90)
    turtle_1.end_fill()


def circle(trtl, height):
    trtl.penup()
    trtl.goto(-10, -50)
    trtl.left(90)
    trtl.forward(height)
    trtl.shape("circle")
    trtl.turtlesize(stretch_wid=2)
    trtl.fillcolor((178, 190, 181))


screen = turtle.Screen()

turtle_1 = turtle.Turtle()
turtle_2 = turtle.Turtle()
turtle_3 = turtle.Turtle()
turtle.colormode(255)

draw_body()
circle(turtle_1, 10)
circle(turtle_2, 80)
circle(turtle_3, 150)

obj = TrafficLight()
obj.running(turtle_1, turtle_2, turtle_3)
