from turtle import *
import colorsys as c
t = Turtle()
t.hideturtle()
screen = Screen()
screen.bgcolor("black")
t.speed(0)
for i in range(200):
    t.color(c.hsv_to_rgb(i/100, 0.9, 1))
    t.forward(i)
    t.circle(0.6*i, 180)
    t.left(135)
screen.exitonclick()