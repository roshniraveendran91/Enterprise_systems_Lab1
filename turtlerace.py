import random
import turtle as t
myscreen = t.Screen()
is_race_on = False
user_turtle = t.textinput(title="Turtle Race", prompt="Which turtle will win?(Choose: Red, Orange, Yellow, Green,Blue, Purple)")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cordinates = [100, 60, 20, -20, -60, -100]
myscreen.setup(width=1000, height=500)
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-490, y=y_cordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_turtle:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 490:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_turtle:
                print(f"You have won! The winning turtle is {winning_color} ")
            else:
                print(f"You have Lost! The winning turtle is {winning_color} ")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

myscreen.exitonclick()
