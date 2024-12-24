# data file has 2 halves
#	top half is a page number pair which says first # must appear before the second #
# 	the second half is a sequence of pages that must be printed
#	only remember the sequences that do NOT violate any of the page requirements
#	of those good sequences, find the middle numbers and add them together, that's your answer
import re

iTotal = 0
iRows = 0
iColumns = 0
linecount = 0

# capture page ordering requirements
with open('data\Dec5-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	linesDict = {}
	bottomHalf = False

	for aline in slines:
		aline = aline.replace('\n', '')

		if aline == '':
			bottomHalf = True
			linecount = 0
			linebadcount = 0

		elif not bottomHalf:
			x1, x2 = aline.split("|")
			
			if x1 not in linesDict:
				linesDict[x1] = x2
			else:
				linesDict[x1] += "," + x2

		else: # on bottom half of the file	
			pageList = aline.split(',')
			bFailed = False 

			for nextcharindex in range(len(pageList)-1,1,-1):
				if bFailed:
					break

				nextchar = pageList[nextcharindex]
				dictlist = linesDict[nextchar]

				for checkcharindex in range(nextcharindex-1):
					checkchar = pageList[checkcharindex]

					if checkchar in dictlist:
						#print(f'failure, {checkchar} appears before {nextchar}')
						#print(f'line: {pageList}')
						#print(f'dictionary for {nextchar} : {dictlist}')
						bFailed = True 
						break 

			if bFailed:
				linebadcount += 1
			else: # was a good line so find middle value
				iTotal += int(pageList[(len(pageList) // 2) ])

			linecount += 1


print(f'{linebadcount} were bad out of {linecount}')
print(f'Total={iTotal}') # 5948

# part 2

# for the incorrect sequences, put them in order
# then just for those, take the sum of the  middle values


