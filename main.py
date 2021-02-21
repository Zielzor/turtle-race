from turtle import Turtle, Screen
import random


def generate_turtles():
    for turtle_index in range(0, 6):
        turtle_names[turtle_index] = Turtle(shape="turtle")
        turtle_names[turtle_index].color(colors[turtle_index])
        turtle_names[turtle_index].penup()
        turtle_names[turtle_index].goto(x=-380, y=y_positions[turtle_index])
        racing_turtles.append(turtle_names[turtle_index])


race = False
screen = Screen()
screen.setup(width=800, height=600)
user_guess = screen.textinput(title="Choose your winner", prompt="Which turtle will be te fastest?:> ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-75, -45, -15, 25, 55, 85]
turtle_names = ["Bruce", "Time", "Yenna", "Vuko", "Dzban", "Rzułf"]
racing_turtles = []


generate_turtles()

if user_guess:
    race = True

while race:

    for racer in racing_turtles:
        if racer.xcor() > 370:
            race = False
            winner = racer.pencolor()
            if winner == user_guess:
                print(f"You picked the right turtle : {winner}!")
            else:
                print(f"You bet on a wrong turtle, Winner is {winner}")

        distance = random.randint(0, 10)
        racer.fd(distance)


screen.exitonclick()
