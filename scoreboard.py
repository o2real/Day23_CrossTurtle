from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.penup()
        self.write("Game Over.", align="center", font=FONT)