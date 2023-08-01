from turtle import *

speed('fastest')
colors = ['red','yellow','blue','green']
pensize(2)
for i in range(100):
   # print(i%4, colors[i%4])
   pencolor(colors[i%4])
   fd(i*5)
   lt(180)
   circle(i*5, 20)

mainloop()