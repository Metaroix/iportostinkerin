import turtle

def draw_rectangle(t, width, height, fill_color=None, pen_color="black", pen_size=2):
    t.penup()
    t.goto(-width / 2, height / 2)
    t.pendown()
    t.color(pen_color)
    t.pensize(pen_size)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Rectangle with turtle")
    screen.setup(width=600, height=400)

    pen = turtle.Turtle()
    pen.speed(3)

    rectangle_width = 300
    rectangle_height = 150
    outline_color = "navy"
    fill = "lightblue"

    draw_rectangle(pen, rectangle_width, rectangle_height, pen_color=outline_color, pen_size=4)

    pen.hideturtle()
    screen.exitonclick()
