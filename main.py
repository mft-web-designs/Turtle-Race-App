from turtle import Turtle, Screen
import random

# Change Control Test

# Set up the display parameters
display = Screen()
display.setup(width=500, height=400)
display.setworldcoordinates(0, 0, 500, 400)

# Get the turtles
turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_y_positions = [75, 125, 175, 225, 275, 325]
turtle_competitors = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=10, y=turtle_y_positions[turtle_index])
    turtle_competitors.append(new_turtle)

# Get the players bet as to the winner of the race
is_race_on = False
players_bet = display.textinput(title="Make your bet, the turtles are ready to start",
                                prompt="Which turtle will win the race? Enter a colour: ")
if players_bet:
    is_race_on = True

# Main game loop
while is_race_on:

    for turtle in turtle_competitors:

        if turtle.xcor() > 480:
            is_race_on = False
            winner = turtle.pencolor()

            if winner == players_bet:
                print(f"You've Won!! The winning turtle was {winner}")
            else:
                print(f"You've Lost!! The winning turtle was {winner}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

display.exitonclick()