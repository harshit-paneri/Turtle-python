import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col=['yellow','blue','white','green']
c=0
for i in range(100):
    t.forward(i*5)
    t.right(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c=c+1
