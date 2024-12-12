# find instances of 'mul(xxx,xxx)' from the input, multiple the values, and then add them up
# ignore any other characters or corruptions of mul(xxx,xxx)
import re
teststring = '{how()mul(1,2),how()when()+when()}what()mul(900,270)'

with open('AdventOfCode\data\Dec3-24.txt', 'r') as DecFile:
	slines = DecFile.readlines()
	isum = 0

	for aline in slines:
		result = re.findall(r'mul\((\d{1,3},\d{1,3})\)', aline)

		for x in range(len(result)):
			value1, value2 = result[x].split(',')
			iprod = int(value1)*int(value2)
			isum += iprod

print(isum) 	#  181345830

part2_test = "abcdo()mul(2,2)abc"

#with open('AdventOfCode\data\Dec3-24.txt', 'r') as DecFile:
#	slines = DecFile.readlines()

#	for aline in slines:
aline = part2_test
isum = 0
parsedline = ''
split_dont = aline.split("don't()")

for x in range(len(split_dont)):
	split_do = split_dont[x].split("do()")
	
	if x % 2 == 0: 	# then starts with do()
		for y in range(len(split_do)):
			if y % 2 == 0:
				parsedline = split_do[y]

				result = re.findall(r'mul\((\d{1,3},\d{1,3})\)', parsedline)

				for z in range(len(result)):
					value1, value2 = result[z].split(',')
					iprod = int(value1)*int(value2)
					isum += iprod

print(isum)

# part 2
#	split on "don't()"
#	then split each of those on "do()"
#	for all except the first list, pop(0) because that will be a "don't()"

