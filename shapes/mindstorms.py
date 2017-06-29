import turtle

def draw_something():
    window = turtle.Screen()
    window.bgcolor("green")
    t = turtle.Turtle()
    for i in range(1,50):
        draw_square(t)
        t.right(10)
    draw_circle(t)
    #draw_triangle()
    window.exitonclick()
    
def draw_square(t):
    i = 0
    while i < 5:
        t.forward(100)
        t.right(90)
        i = i + 1    
    
def draw_circle(t):
    t.circle(100)

def draw_triangle():
    triangle = turtle.Turtle()   
    triangle.forward(100)
    triangle.right(60)
       

draw_something()

