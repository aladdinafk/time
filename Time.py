import datetime
import turtle
import time
t = turtle.Turtle()
t.back(250)
t.clear()
while True:
    t.clear()
    d = datetime.datetime.today()
    t.write(d, font= ("Times new roman", 30, "normal"))
    time.sleep(1)
