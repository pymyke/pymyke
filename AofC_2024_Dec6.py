# Find the angle symbol (<  >  V  ^) and then move the character in straight lines
# when an obstacle is hit, rotate 90 degrees clockwise and move again.
# until it exits the play area
# count how many UNIQUE steps it took, so need to change the cell to 'X'
import re
import unittest

linelist = []
linecount = 0

with open('data\Dec6-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	
	for aline in slines:
		linelist.append(aline)
		if '^' in aline:
			guardX = linecount
			guardY = aline.index('^')

			moveX = -1
			moveY = 0
		
		linecount += 1

colcount = len(linelist)

print(f'There are {linecount} rows with {colcount} columns')
print(f'The guard is currently at ({guardX},{guardY})')

bInRoom = True 
iUniqueSteps = 1

while bInRoom:
	if (0 > guardX+moveX) or (guardX+moveX >= linecount) or (0 > guardY+moveY) or (guardY+moveY >= colcount):
		# out of room
		bInRoom = False
	else: # still in the room
		if linelist[guardX+moveX][guardY+moveY] == '.' or linelist[guardX+moveX][guardY+moveY] == '^': # open so ok to move
			guardX += moveX
			guardY += moveY

			str1 = linelist[guardX][0:guardY]
			str2 = linelist[guardX][guardY+1:]
			linelist[guardX] = str1 + "X" + str2

			iUniqueSteps += 1
		elif linelist[guardX+moveX][guardY+moveY] == 'X': # already been here
			guardX += moveX
			guardY += moveY

		else:  # hit an obstacle to turn 90 degrees clockwise
			if moveX == 0:
				if moveY == -1: 
					moveX = -1
				else:	
					moveX = 1
				moveY = 0
			else:
				if moveX == -1: 
					moveY = 1
				else:	
					moveY = -1
				moveX = 0


print(f'Guard is now at [{guardX},{guardY}] at step {iUniqueSteps}')

print(f'The guard took {iUniqueSteps} steps')	# 387 is too low
