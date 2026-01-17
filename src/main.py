from turtle import Screen
from src.paddle import Paddle
from ball import Ball
from src.scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('coral')
screen.title('Pong')
screen.tracer(0) # screen.tracer + screen.update

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect Out of Bounds on the right
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increase_score_l()

    # detect Out of Bounds on the left
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_score_r()

    # if right wins
    if scoreboard.score_r > 3:
        scoreboard.right_wins()
        game_on = False

    # if left wins
    if scoreboard.score_l > 3:
        scoreboard.left_wins()
        game_on = False




screen.exitonclick()

