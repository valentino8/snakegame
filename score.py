from turtle import Turtle
from food import Food
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, "center", ("Arial", 10, "normal"))
    def scorecount(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 10, "normal"))
        self.goto(5, -50)
        self.write(f"Your score: {self.score} ",False, "center", ("Courier", 10, "normal"))



