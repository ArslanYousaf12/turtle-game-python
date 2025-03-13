from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(canvwidth=500, canvheight=400)
user_bet =screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color ")
print(user_bet)
colors_list = ["red", "orange", "green", "purple", "blue", "yellow"]
turtle_list = []
gap = 0
is_game_on = False
for num in range(6):

    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors_list[num])
    new_turtle.goto(-350  , -150 + gap )
    gap += 40
    turtle_list.append(new_turtle)
    

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 330:
            is_game_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won! the wining color is {wining_color}")
            else:
                print(f"You loose! The wining color is {wining_color}")
        distance = random.randint(1,10)
        turtle.forward(distance)
    






screen.exitonclick()