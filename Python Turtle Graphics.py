import turtle

screen = turtle.Screen()
screen.title("Python Turtle Graphics")
screen.setup(width=600, height=600)

player = turtle.Turtle()
player.shape("turtle")
player.speed(0)

def move_up():
    player.stamp()
    player.setheading(90)
    player.forward(50)

def move_down():
    player.stamp()
    player.setheading(270)
    player.forward(50)

def move_left():
    player.stamp()
    player.setheading(180)
    player.forward(50)

def move_right():
    player.stamp()
    player.setheading(0)
    player.forward(50)

def quit_program():
    screen.bye()

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(quit_program, "Escape")

screen.mainloop()
