from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("pink")
screen.title("TURTLE RACE")
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race (Red, Orange, Yellow, Green, Blue or Purplr)? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_axis = [-100, -60, -20, 20, 60, 100]
all_turtles = []

race_on = False

if user_bet:
    race_on = True
    for i in range(0, 6):
        tim = Turtle(shape="turtle")
        tim.color(colors[i])
        tim.penup()
        tim.goto(x=-230, y=y_axis[i])
        all_turtles.append(tim)
else:
    print("Race didn't Started🥺")

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if user_bet == win_color:
                print(f"You've won🥇! The {win_color} turtle won.")
            else:
                print(f"You've lost🤪! The {win_color} turtle won.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
