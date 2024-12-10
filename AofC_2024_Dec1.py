# read input file
leftlist = []
rightlist = []

# part 1 - find differences between lists by compare lowest to highest values

with open('data\Dec1-24.txt', 'r') as Dec1File:
	slines = Dec1File.readlines()

	for aline in slines:
		value1, value2 = aline.split('   ')
		leftlist.append(value1)
		rightlist.append(value2)
	
leftlist.sort()
rightlist.sort()

sum = 0

for x in range(len(leftlist)):
	sum += abs(int(leftlist[x])-int(rightlist[x]))

print (sum)	 # 2176849

# part 2 - find the 'similarity' score between the lists

isum = 0
for left in leftlist:
	newlist = [x for x in rightlist if int(x) == int(left)]
	isum += len(newlist) * int(left)

print(isum) # 23384288
