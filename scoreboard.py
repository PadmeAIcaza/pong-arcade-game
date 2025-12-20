from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color('white')
        self.penup() # removes the movement line
        self.hideturtle() # removes the turtle
        self.right_score()
        self.left_score()

    def right_score(self):
        self.goto(200, 200)  # positioning of the text
        self.write(f'{self.score_r}', False, 'right', ('Courier', 50, 'normal'))

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.right_score()
        self.left_score()

    def left_score(self):
        self.goto(-200, 200)  # positioning of the text
        self.write(f'{self.score_l}', False, 'left', ('Courier', 50, 'normal'))

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.right_score()
        self.left_score()

    def right_wins(self):
        self.goto(0, 0)
        self.write('Right Wins!', False, 'center', ('Courier', 50, 'normal'))

    def left_wins(self):
        self.goto(0, 0)
        self.write('Left Wins!', False, 'center', ('Courier', 50, 'normal'))

