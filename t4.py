from turtle import *

speed('fastest')
pensize(2)
bgcolor('black')
pencolor('white')
colors = ['red','yellow','green','orange','purple','blue']
side = 6
for i in range(side):
    fd(200)
    for i in range (side):
        fd(100)
        lt(360/side)
        begin_fill()
        fillcolor(colors[i%6])
        for i in range(side):
            fd(50)
            lt(360/side)
        end_fill()
    lt(360/side)
hideturtle() 
mainloop()            

            