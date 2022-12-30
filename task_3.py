from turtle import * 
data = []

reverse_pos_x = -410
reverse_pos_y = 320

for unit in open("listy/lista05/dots.txt"):
    data.append(unit.strip().split(" "))
  
pu()
goto(int(data[0][0])  + reverse_pos_x, -int(data[0][1]) + reverse_pos_y)
pd()
    
for i in range(len(data)):
    x, y = int(data[i][0]) + reverse_pos_x, -int(data[i][1]) + reverse_pos_y
    goto(x, y) 
update()
exitonclick()
