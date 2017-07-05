import turtle


def draw_tringle():
    window = turtle.Screen()
    window = turtle.bgcolor("red")

    tri = turtle.Turtle()
    tri.forward(100)
    tri.left(120)
    tri.forward(100)
    tri.left(120)
    tri.forward(100)

    window.exitonclick()


draw_tringle()
