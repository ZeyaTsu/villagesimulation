from turtle import *
import turtle
import math
import random
turtle.setup(1920, 1080)
turtle.bgcolor("black")

s1 = turtle.Turtle()
s2 = turtle.Turtle()
s3 = turtle.Turtle()
s4 = turtle.Turtle()


t_list = [s1, s2, s3, s4]
for t in t_list:
	turtle.color("cyan")
	turtle.speed(2)
	s1.color("cyan")
	s2.color("cyan")
	s3.color("cyan")
	s4.color("cyan")

s1.forward(100)
s2.backward(100)

def setup1():
	s3.left(90)
	s3.forward(100)
	return
def setup2():
	s4.right(90)
	s4.forward(100)
	return
def village():
	ontimer(village, 5000)
	for i in range(7):
		a = random.randint(1, 7)
		if a == 1:
			s1.forward(40)
			return
		if a == 2:
			s1.backward(40)
			return
		if a == 3:
			s1.right(90)
			s1.forward(40)
			return
		if a == 4:
			s1.left(90)
			s1.forward(40)
			return
		if a == 5:
			s1.color("red")
			s1.circle(10)
			s1.color("cyan")
		if a == 6:
			s1.color("green")
			s1.stamp()
			s1.color("cyan")
			return
		if a == 7:
			s1.color("red")
			s1.circle(10)
			s1.color("cyan")
			return	

def village2():
	ontimer(village2, 5000)
	for i in range(7):
		a = random.randint(1, 7)
		if a == 1:
			s2.forward(40)
			return
		if a == 2:
			s2.backward(40)
			return
		if a == 3:
			s2.right(90)
			s2.forward(40)
			return
		if a == 4:
			s2.left(90)
			s2.forward(40)
			return
		if a == 5:
			s2.color("red")
			s2.circle(10)
			s2.color("cyan")
		if a == 6:
			s2.color("green")
			s2.stamp()
			s2.color("cyan")
			return
		if a == 7:
			s2.color("red")
			s2.circle(10)
			s2.color("cyan")
			return	

def village3():
	ontimer(village3, 5000)
	for i in range(7):
		a = random.randint(1, 7)
		if a == 1:
			s3.forward(40)
			return
		if a == 2:
			s3.backward(40)
			return
		if a == 3:
			s3.right(90)
			s3.forward(40)
			return
		if a == 4:
			s3.left(90)
			s3.forward(40)
			return
		if a == 5:
			s3.color("red")
			s3.circle(10)
			s3.color("cyan")
		if a == 6:
			s3.color("green")
			s3.stamp()
			s3.color("cyan")
			return
		if a == 7:
			s3.color("red")
			s3.circle(10)
			s3.color("cyan")
			return	

def village4():
	ontimer(village4, 5000)
	for i in range(7):
		a = random.randint(1, 7)
		if a == 1:
			s4.forward(40)
			return
		if a == 2:
			s4.backward(40)
			return
		if a == 3:
			s4.right(90)
			s4.forward(40)
			return
		if a == 4:
			s4.left(90)
			s4.forward(40)
			return
		if a == 5:
			s4.color("red")
			s4.circle(10)
			s4.color("cyan")
		if a == 6:
			s4.color("green")
			s4.stamp()
			s4.color("cyan")
			return
		if a == 7:
			s4.color("red")
			s4.circle(10)
			s4.color("cyan")
			return	






village4()
village3()
village2()
village()
mainloop()
