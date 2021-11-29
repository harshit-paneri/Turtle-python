import turtle
s = turtle.Screen()
s.bgcolor('black')
col=['yellow','blue','white','green']
c=0
t1=turtle.Turtle()
turtle.ht()
for e in range(7):
    x=t1.stamp()
    t1.fd(100)
    t1.lt(60)
    
    t1.clearstamp(x)
    t1.color(col[c])
    if c==3:
        c=0
    else:
        c=c+1
    #t1.fd(100)
    t1.ht()
    
