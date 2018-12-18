from turtle import *
speed(0)
color('Blue', 'Black')
begin_fill()
while True:
  
    forward(200)
    left(170)
    circle(99)
    forward(22)
    circle(155)
    left(120)
    right(175)
    circle(250)
    if abs (pos()) < 1:
        break
end_fill()
done()