from turtle import Turtle, Screen


timy = Turtle()
my_screen = Screen()






def move_forward():
    timy.forward(10)


my_screen.listen()

my_screen.onkey(key="space", fun=move_forward)




my_screen.exitonclick()