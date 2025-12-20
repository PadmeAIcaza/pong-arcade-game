from turtle import Screen, Turtle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('coral')
screen.title('Pong')
screen.tracer(0) # screen.tracer + screen.update

paddle = Turtle()
paddle.shape('square')
paddle.shapesize(5, 1)
paddle.color('white')
paddle.penup() # removes the line
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_on = True

while game_on:
    screen.update()


screen.exitonclick()

