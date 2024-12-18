# find instances of 'xmas' from the input, any direction
import re

iTotal = 0
iRows = 0
iColumns = 0

# count occurrencs by row
with open('AdventOfCode\data\Dec4-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	icount = 0
	for aline in slines:
		icount += aline.count('XMAS') + aline.count('SAMX')
		iRows += 1

print(f'Occurrences for {iRows} rows: {icount}')
iTotal += icount

# count occurrences by column
with open('AdventOfCode\data\Dec4-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	scolumns = []
	for aline in slines:
		iColumns = len(aline)
		
		if len(scolumns) < 1:
			scolumns = ['' for y in range(iColumns)]
			
		for x in range(iColumns):
			scolumns[x] += aline[x]

icount = 0
for scol in scolumns:
	icount += scol.count('XMAS') + scol.count('SAMX')

print(f'Occurrences for {iColumns} columns: {icount}')
iTotal += icount

# count occurrences by diagonal, NW to SE
with open('AdventOfCode\data\Dec4-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	ddiagonal = {}
	iRows = 0
	
	for aline in slines:
		iCol = 0
		iRow = iRows
		for xstr in aline:
			if f'{iRow},{iCol}' in ddiagonal:
				ddiagonal[f'{iRow},{iCol}'] += xstr 
			else:
				ddiagonal[f'{iRow},{iCol}'] = xstr 
			
			# setting iCol MUST come before decrementing iRow
			if iRow == 0:
				iCol += 1

			iRow = max(0,iRow-1)
			
		iRows += 1

	# now go thru the dictionary of strings and find the tokens
	listValues = ddiagonal.values()
	icount = 0
	for svalue in listValues:  # a diagonal string
		icount += svalue.count('XMAS') + svalue.count('SAMX')

	print (f'Occurrences for NW-SE diagonals: {icount}')
	iTotal += icount

# count occurrences by diagonal, NE to SW
with open('AdventOfCode\data\Dec4-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	ddiagonal = {}
	iRows = 0
	# iColumns was set above
	
	for aline in slines:
		iCol = 0
		iRow = iRows
		for xstr in aline:
			if f'{iRow},{iCol}' in ddiagonal:
				ddiagonal[f'{iRow},{iCol}'] += xstr 
			else:
				ddiagonal[f'{iRow},{iCol}'] = xstr 
			
			# setting iCol MUST come before decrementing iRow
			iRow += 1
			if iRow >= iColumns:
				iRow = iColumns - 1
				iCol += 1
			
		iRows += 1

	# now go thru the dictionary of strings and find the tokens
	listValues = ddiagonal.values()
	icount = 0
	for svalue in listValues:  # a diagonal string
		icount += svalue.count('XMAS') + svalue.count('SAMX')

	print (f'Occurrences for NE-SW diagonals: {icount}')
	iTotal += icount

print(f'Total Count: {iTotal}')  # part 1, 2434

# part 2
# need to count occurrences of MAS/SAM in an X shape
# MAS can appear forward or backward in same X
#
# we'll process by rows, 3 at a time
# if 'a' appears in the middle row, then look for the 'X'

with open('AdventOfCode\data\Dec4-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	icount = 0

	sPrevious = ''
	sCurrent = ''
	sNext = ''

	for aline in slines:
		sPrevious = sCurrent
		sCurrent = sNext
		sNext = aline
		if sPrevious=='' or sCurrent=='' or sNext=='':
			continue # skip to next row

		# look for an 'a' in sCurrent, skipping left-most and 2 right-most
		for xpos in range(1,len(sCurrent)-2):
			if sCurrent[xpos] == 'A':
				if (sPrevious[xpos-1]+sNext[xpos+1] == 'MS' or
					sPrevious[xpos-1]+sNext[xpos+1] == 'SM'): 
					if (sPrevious[xpos+1]+sNext[xpos-1] == 'MS' or
						sPrevious[xpos+1]+sNext[xpos-1] == 'SM'):
						icount += 1
		
	print(f'Part 2 count: {icount}') # 1835

