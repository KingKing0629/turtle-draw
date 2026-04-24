import sys
import turtle
import os
screen = turtle.Screen()
screen.setup(width=450, height=450)
t = turtle.Turtle() 
t.speed(10)
t.penup()


#FILENAME = 'TurtleDrawInfo.txt'
print("Enter file name(i.e., TurtleDrawInfo.txt):")
FILENAME = input()
if os.path.exists(FILENAME):
	print("Opening file...")
else:
	print("File does not exist. Exiting program.")
	sys.exit()

TurtleDrawFile = open(FILENAME, 'r')

line = TurtleDrawFile.readline()



while line:
	Scraps = line.split() 
	if len(Scraps) == 3:
		print(Scraps)
		color = Scraps[0]
		x = int(Scraps[1])
		y = int(Scraps[2])
		
		t.pencolor(color)
		t.goto(x, y)
		t.pendown()

	if len(Scraps) == 1:
		t.penup()
		

	line = TurtleDrawFile.readline()

print("Drawing complete. Press Enter to exit.")
input()
TurtleDrawFile.close()
try:
	turtle.bye()
except turtle.Terminator:
	pass
