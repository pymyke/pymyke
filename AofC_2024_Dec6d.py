
# Part 2
# 	find the # of places that an obstacle could be placed to create an infinite loop of moves
# Part 2c
#	2b worked for the sample data but not the actual data
#	2b only looked to the right but 2c needs run the entire route to the right
#	and if it ever runs into a pre-visited cell IN THE SAME DIRECTION then a loop could be made
import re
import unittest
import json

obstacleCount = 0
dictList = {}
iTurn = 0
dictTurns = {}
iMyIndex = 82 # how far to traverse the path before I look for a loop


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
		#print('place obstacle next to guards current position')

	return bObstacleNeeded
# end of FindObstacle

def PlaceDirection(xMove, yMove, xCoord, yCoord):
	global iTurn
	iTurn += 1
	sDir = ''

	if xMove == 0:
		if yMove < 0:
			sDir = 'W'
		else:
			sDir = 'E'
	elif xMove < 0:
		sDir = 'N'
	else:
		sDir = 'S'

	sKey = str(xCoord)+','+str(yCoord)
	if sKey in dictList:
		dictList[sKey] += sDir
	else:
		dictList[sKey] = sDir
# end of PlaceDirection


def DetectLoop(sline, guardpos, moveX, moveY):
	global obstacleCount

	if moveX>0 or moveY<0:
		ssearch = sline[0:guardpos][::-1]
	else:
		ssearch = sline[guardpos+1:]

	print(f'DetectLoop ({ssearch},{guardpos},{moveX},{moveY})')

	poundX = ssearch.find('#')
	xX = ssearch.find('X#')		 # there has to be an obstacle on the other side

	bObstacleNeeded = False 

	if xX>=0: # we hit a previous path with an obstacle on the other side
		# only if we went in the right direction does this count as a loop
		print(f'Found X# at {xX}')
		bObstacleNeeded = True
	elif poundX >= 0:# need to check for a loop from this point
		pass 
		#DetectLoop(sline, guardpos, moveX, moveY)
	else: # nothing to bounce off from so no possible loop
		bObstacleNeeded = False

# end of DetectLoop

def Rotate(moveX, moveY):
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

	PlaceDirection(moveX, moveY, guardX, guardY)

linelist = []
columnlist = []
linecount = 0

""" 
# Load cells/directions Dictionary from the JSON file
with open("logs/Dec6_dictionary.json", "r") as file:
    dictList = json.load(file)

with open("logs/Dec6_turn_dictionary.json", "r") as file:
    dictTurns = json.load(file) 


print("Loaded dictionaries")
"""

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

			PlaceDirection(moveX, moveY, guardX, guardY)

		linecount += 1

colcount = len(linelist)

print(f'My index is {iMyIndex}')
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
bCheckLoop = False 

while bInRoom:
	if (0 > guardX+moveX) or (guardX+moveX >= linecount) or (0 > guardY+moveY) or (guardY+moveY >= colcount):
		# out of room
		bInRoom = False
	else: # still in the room
		if linelist[guardX+moveX][guardY+moveY] == '.': # open so ok to move
			guardX += moveX
			guardY += moveY

			PlaceDirection(moveX, moveY, guardX, guardY)

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

			PlaceDirection(moveX, moveY, guardX, guardY)

		else:  # hit an obstacle to turn 90 degrees clockwise
			Rotate(moveX, moveY)

	if iMyIndex == iTurn:
		# check if an obstacle here would create a loop
		if (moveX == 0):
			DetectLoop(columnlist[guardY], guardX, moveX, moveY)
		else:
			DetectLoop(linelist[guardX], guardY, moveX, moveY)

		for x in range(70,88):
			print(f'{linelist[x]}')

		break # done with the loop check 


print(f'Guard is now at [{guardX},{guardY}] at step {iTurn}')

print(f'Obstacle count is {obstacleCount}')

