from turtle import Screen, Turtle
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Pong((350, 0))
l_paddle = Pong((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

speed = 0.05

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 315) or (ball.distance(l_paddle) < 50 and ball.xcor() < -315):
        ball.bounce_x()
        speed *= 0.9

    if ball.xcor() > 360:
        ball.reverse()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reverse()
        scoreboard.r_point()













screen.exitonclick()
