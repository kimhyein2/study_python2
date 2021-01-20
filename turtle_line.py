import turtle
turtle.shape('turtle')
# .forward(거리 : px)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.fd(100)
#turtle.right(90)
#turtle.fd(100)

def draw_rect():
    for i in range(4):
        turtle.fd(100)
        turtle.right(90)

draw_rect()
