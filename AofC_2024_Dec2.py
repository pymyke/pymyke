'''
both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
'''
iSafeReports = 0

with open('AdventOfCode\data\Dec2-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()

	for aline in slines:
		# variable number of space-delimited integer values
		valuelist = aline.split(' ')
		icnt = 0
		bIncreasing = None
		bSafe = True 
		iprev = 0

		for svalue in valuelist:
			ivalue = int(svalue)
			icnt += 1
			if icnt == 1: 
				iprev = ivalue
			else:
				if ivalue > iprev:
					if icnt == 2:
						bIncreasing = True
					elif bIncreasing:
						pass
					else:
						bSafe = False
						break 
				elif ivalue == iprev:
					bSafe = False
					break 
				else: # decreasing
					if icnt == 2:
						bIncreasing = False
					elif bIncreasing:
						bSafe = False
						break 
					else:
						pass 
			
				if 1 <= abs(ivalue-iprev) <= 3:
					pass 
				else:
					bSafe = False
					break 

			iprev = ivalue 

		if bSafe:
			iSafeReports += 1


print (iSafeReports)  # 463

