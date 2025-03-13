from turtle import Turtle, Screen


timy = Turtle()
my_screen = Screen()






def move_forward():
    timy.forward(10)
    
    
def move_backward():
    timy.backward(10)

def turn_left():
    timy.left(10)

def turn_right():
    timy.right(10)

def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()
    timy.setheading(0)

my_screen.listen()

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear)




my_screen.exitonclick()