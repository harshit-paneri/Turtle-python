import turtle
t=turtle.Turtle()
s=turtle.Screen()
color = ['orange','red','grey','blue','pink','yellow']
t.speed(0)
s.bgcolor('green')
for i in range(120):
    t.pencolor(color[i%6])
    t.width(i/6)
    t.forward(i)
    t.left(20)
