import turtle  # We usually import at the very beginning
import math


def draw_fish(alex, a, steps):
    """Draws a curve with a simple shape of a fish"""
    t = 0  # initialization, angle = 0 we start at (a, 0)
    for i in range(steps + 1):  # Thousand points
        if i == 0:  # Draws the mouth
            alex.up()
            alex.forward(2 * a / 3)
            alex.down()
            alex.forward(a / 3)
        t += 2 * math.pi / steps  # When t span from 0 to 360, fish curve is complete
        x = a * math.cos(t) - a * (math.sin(t)) ** 2 / (2 ** 0.5)  # x coordinate
        y = a * math.cos(t) * math.sin(t)  # y
        alex.goto(x, y)
        if i == steps:  # Draws the eye
            alex.up()
            alex.goto(2 * a / 3, a / 4)
            alex.down()
            alex.circle(a / 30)


def main():
    alex = turtle.Turtle()  # Creates a turtle named alex
    alex.speed(10)  # Set alex's speed
    alex.width(7)  # Set alex's line width
    screen1 = turtle.Screen()  # Creating a screen object named screen1
    a = 180  # scale_parameter = 2
    draw_fish(alex, a, 100)  # Drawing fish with 100 goto steps
    screen1.exitonclick()  # Mouse click will close the window
    print(__name__)
    

if __name__ == "__main__":
    main()