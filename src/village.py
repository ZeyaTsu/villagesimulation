from turtle import *
import turtle
import math
import random
turtle.setup(800, 800)
turtle.color("cyan")
turtle.bgcolor("black")
turtle.speed(2)

def village():
	ontimer(village, 2000)
	for i in range(7):
		a = random.randint(1, 7)
		if a == 1:
			forward(40)
			return
		if a == 2:
			backward(40)
			return
		if a == 3:
			right(90)
			forward(40)
			return
		if a == 4:
			left(90)
			forward(40)
			return
		if a == 5:
			circle(10)
		if a == 6:
			stamp()
			return
		if a == 7:
			circle(10)
			return	

village()
mainloop()
