import turtle

screen = turtle.Screen()
screen.bgcolor("maroon")

pen = turtle.Turtle()
pen.speed(0)
pen.color("white", "red")
pen.pensize(3)

pen.penup()
pen.setpos(-240, -150)
pen.pendown()

def draw_triangle(length):
    pen.setheading(180)
    pen.begin_fill()
    for i in range(3):
        pen.rt(120)
        pen.fd(length)
    pen.end_fill()

def sierpinski_order_n_recursive(n, length):
    if n==1:
        draw_triangle(length)
    else:
        sierpinski_order_n_recursive(n - 1, length)
        pen.rt(120)
        pen.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        pen.lt(120)
        pen.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        pen.fd(length * 2 ** (n - 2))

sierpinski_order_n_recursive (4,50)

turtle.done()
