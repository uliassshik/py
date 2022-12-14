import turtle


def a(x, y):
    return (x[0]+y[0]) / 2, (x[1] + y[1]) / 2


def triangle(tp, depth):
    t.up()
    t.goto(tp[0][0], tp[0][1])
    t.down()
    t.goto(tp[1][0], tp[1][1])
    t.goto(tp[2][0], tp[2][1])
    t.goto(tp[0][0], tp[0][1])

    if depth > 0:
        triangle([tp[0], a(tp[0], tp[1]), a(tp[0], tp[2])], depth-1)
        triangle([tp[1], a(tp[0], tp[1]), a(tp[1], tp[2])], depth-1)
        triangle([tp[2], a(tp[2], tp[1]), a(tp[0], tp[2])], depth-1)


t = turtle.Turtle()
t.ht()
t.speed(10)
t.pencolor('blue')

t.speed(0)
tpx = [[-175, -125], [0, 175], [175, -125]]

triangle(tpx, 5)