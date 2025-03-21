
# Part 2
# 	find the # of places that an obstacle could be placed to create an infinite loop of moves
import re
import unittest

obstacleCount = 0

# X is the line, so the row index
# Y is the position in the line, so the column index
#   yes, this is reversed of normal

# returns True if an obstacle can be created
def FindObstacle (sline, guardpos, moveX, moveY):
	global obstacleCount

	if moveX>0 or moveY<0:
		ssearch = sline[0:guardpos][::-1]
	else:
		ssearch = sline[guardpos+1:]

	#print(f'({sline},{guardpos},{moveX},{moveY}) searching {ssearch} ')

	poundX = ssearch.find('#')
	xX = ssearch.find('X#')		 # there has to be an obstacle on the other side

	bObstacleNeeded = False 

	if poundX < 0: # no obstacle found
		if xX < 0:  # no path found either
			#print('neither # nor X found')
			pass
		else:
			# put obstacle to the left of guardx,guardy
			#print('place obstacle next to guards current position')
			bObstacleNeeded = True
	elif xX < 0: # no path found
		pass 
	elif poundX < xX:
		#print('obstacle appears before path')
		pass
	else:
		# put obstacle to the left of guardx,guardy
		#print('place obstacle next to guards current position')
		bObstacleNeeded = True

	if bObstacleNeeded:
		obstacleCount += 1
		print('place obstacle next to guards current position')

	return bObstacleNeeded
# end of FindObstacle


linelist = []
columnlist = []
linecount = 0

with open('data\Dec6-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	
	for aline in slines:
		linelist.append(aline)
		if '^' in aline:
			guardX = linecount # X is the row
			guardY = aline.index('^')  # Y is the column

			moveX = -1
			moveY = 0

			# put an 'X' in the line string at our current location
			str1 = linelist[guardX][0:guardY]
			str2 = linelist[guardX][guardY+1:]
			linelist[guardX] = str1 + "X" + str2

		linecount += 1

colcount = len(linelist)

print(f'There are {linecount} rows with {colcount} columns')
print(f'The guard is currently at ({guardX},{guardY})')

# create a list of the column strings to make searching easier
for x in range(colcount):
	newstr = ''
	for y in range(len(linelist)):
		newstr += linelist[y][x]
	columnlist.append(newstr)

bInRoom = True   # turns FALSE when outside the rows/columns
iUniqueSteps = 1

while bInRoom:
	if (0 > guardX+moveX) or (guardX+moveX >= linecount) or (0 > guardY+moveY) or (guardY+moveY >= colcount):
		# out of room
		bInRoom = False
	else: # still in the room
		if linelist[guardX+moveX][guardY+moveY] == '.' or linelist[guardX+moveX][guardY+moveY] == '^': # open so ok to move
			guardX += moveX
			guardY += moveY

			# put an 'X' in the line string at our current location
			str1 = linelist[guardX][0:guardY]
			str2 = linelist[guardX][guardY+1:]
			linelist[guardX] = str1 + "X" + str2

			# put an 'X' in the column string at our current location
			str1 = columnlist[guardY][0:guardX]
			str2 = columnlist[guardY][guardX+1:]
			columnlist[guardY] = str1 + "X" + str2

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

		#print(f'The guard is currently at ({guardX},{guardY}) moving ({moveX},{moveY})')

		if (moveX == 0):
			FindObstacle(columnlist[guardY], guardX, moveX, moveY)
		else:
			FindObstacle(linelist[guardX], guardY, moveX, moveY)

print(f'Guard is now at [{guardX},{guardY}] at step {iUniqueSteps}')

print(f'The guard took {iUniqueSteps} steps')	# 387 is too low

# 747 is too low
print(f'You could place {obstacleCount} obstacles to create an infinite loop')
