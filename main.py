from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('coral')
screen.title('Pong')
screen.tracer(0) # screen.tracer + screen.update

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    screen.update()


screen.exitonclick()

