# data file has 2 halves
#	top half is a page number pair which says first # must appear before the second #
# 	the second half is a sequence of pages that must be printed
#	only remember the sequences that do NOT violate any of the page requirements
#	of those good sequences, find the middle numbers and add them together, that's your answer
import re

iTotal = 0
iRows = 0
iColumns = 0

# capture page ordering requirements
with open('data\Dec5-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	linesDict = {}
	bottomHalf = False

	for aline in slines:
		aline = aline.replace('\n', '')

		if aline == '':
			bottomHalf = True
		elif not bottomHalf:
			x1, x2 = aline.split("|")
			
			if x1 not in linesDict:
				linesDict[x1] = x2
			else:
				linesDict[x1] += "," + x2
		else: # on bottom half of the file	
			pageList = aline.split(',')

			# go thru the list to make sure all pages satisfy the order requirements
			for x in pageList:
				pass

