# Part 2
# 	find the # of places that an obstacle could be placed to create an infinite loop of moves
import re
import unittest

linelist = []
columnlist = []
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

# create a list of the column strings
for x in range(colcount):
	newlist = []
	for y in range(len(linelist)):
		newlist.append(linelist[y][x])
	columnlist.append(newlist)

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

			# also put it in the column list
			str1 = columnlist[guardY][0:guardX]
			str2 = columnlist[guardY][guardX+1]
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


print(f'Guard is now at [{guardX},{guardY}] at step {iUniqueSteps}')

print(f'The guard took {iUniqueSteps} steps')	# 387 is too low

class TestRE(unittest.TestCase):

	# want to test where we should be an obstacle
	def test_cases(self):
	
		part2_tests = ["abcdon't()do()mul(2,2)abc", 
				   "abcdo()abcdo()mul(3,3)don't()abcmul(4,4)abcdo()",
			   		"do()do()do()don't()mul(5,5)don't()don't()do()mul(6,6)", 
					 "mul(2,2),don't(mul(3,3))don't()mul(4,4)",
					  "don'tmul(3,3)domul(5,5)",
					   "mul[2,3]don't()mul(5,6)abcdo()mul[9,9]abcdon't()",
						"!how()where()*mul(527,340)?why()^?mul(168,100)!^#mul(390,111)>'when()'select())((from()how()mul(412,526)/@wh" ,
						"do()who() {&}-:(mul(844,162)~from()/mul(77,769)%,how()@%(?who()]<mul(694,833)^from()how()> &mul(193,679),)&mul(565,339)?}what()!who(){mul(705,313)mul(294,50)+mul(201,534) )~how()mul(659,49)!mul(871,788)select()where()from()mul(346,618) *&@'why()&}#mul(483,765)!#select()^*+[what()when()mul(448,525)]>:where()&^who()&mul(611,331):!)*/]}mul(37,42)>mul(538,106)when()why()mul(36,120)~where()-{+from()$'mul(950,456))mul(28,237)what()when(479,124)mul(697,976)):**/]&#how()#mul(424,841)why()'!;~mul(108,859)~%{?!mul(40,521)do()[^when()/%$+ [where()mul(187,953)who()where()select()(select()what()mul(984,77)<@)(/where()from()~;mul(163,398)/who()who()~mul(445,94))what()what()][how(),mul(115,245)--}/#how()what()!mul(366,981)'$why()do()what(565,96)who()mul(128,999):mul(858,772)[,,mul(796,864)why()what()^(mul(136,980)when()?!when()}mul(142,552)(mul(354,328)[(@how() (/~#mul(159,715)where()&mul(567,560)from()$^'$&&+!when()mul(582,489);where();select(),mul(306,841)? ,)how()mul(274,549)@~what()~?*mul(448,441);&<'select()when()when()#select()from()mul(404,209)^/ @who()who()'mul(400,15)';^&&when():{mul(199,543)[from()~+mul(452,787)([select()>/]$!/mul(840,165)when()>^why()~>when()(mul(830,125)from():mul(433,238);%why(){';$mul(494,781),-mul(139,401)&&&+who()>/^select()]do()mul(116,181)+$*[:who() do()how()<what()+mul(392,879)()what()don't()~)&?#*}mul(909,275)mul(695,234):],from()++^how()>;mul(514,117)$who()*)~%mul(859,857)}mul(837,844)>{@-what())-@@mul(574,73)]<[[why(608,495)how()who()when()mul(937,176)(%mul(471,325){'+)?:}mul(695,347)mul(56,888)where()##;#>who()+mul(157,650)mul(847,72):,[(how(144,703):mul(294,627)})>@mul(74,230)@)+what()mulhow()><<,$!(;why()mul(635,532)-select()mul(171,737)?select()[why()&^mul(587,686)$how()from())when()>;where()&mul(600,336)}@&{mul(651,690)from()?->&%mul(454,745)mul(387,378)mul(142,934)]mul(820,891)@#why()&how();;why()mul(337,723)&]from()when(894,39) ,>( mul/%(mul(271,558)#}']what()$-<^(mul(234 [what()when()select()($)+!don't()/ %<?%!]^mul(752,478)]how()mul(719,540)'when() why():(&'from(59,581)~mul(921,696)who()@,**%from(918,170))mul(224,391),where(104,159)do()from(339,837)}<<where()?{&how()mul(329,298)<who()what(937,474)&]@?mul(920,516);mul(438,991);{why()!]~'from()>mul(927,106)why()<%{{&~'<from()mul(950,746)'mul(240,649)?what(827,689)(mul(750,353)select(720,6)^mul(663,218)<,(why()<who()^>%why()mul(617?from()select()<what()mul(873,278)&^where(86,235)mul(170,108)!select()mul(66,5)@$^,~%from()mul(785,826): ~who(){mul(383,166):!![:~}+-'mul(554,291)@^)(^#when()when()why()mul(330,699)[:how(888,93)who()how(863,345)who()mul{how()-why()who()]$^mul(512,474)^@:mul(728,970)%mul(779,946)&& mul(216,667) where()^'%mul(788,642)how()>from()}$mul(915,977)& &mul(477,287){# mul(798,930)]mul(111select()*^@@/what()mul(518,86):('({&~{why()mul(991,855)*%^who()who()$/:{$mul(827,700)-'(mul(377,585)#&mul(171,537)when()@/>{< ,*:mul(349,478)!&^{-/mul(448,750)mul(868,546)mul(893,203)",
						"do()who() {&}-:(mul(844,162)~from()/mul(77,769)%,how()@%(?who()]<mul(694,833)^from()how()> &mul(193,679),)&mul(565,339)?}what()!who(){mul(705,313)mul(294,50)+mul(201,534) )~how()mul(659,49)!mul(871,788)select()where()from()mul(346,618) *&@'why()&}#mul(483,765)!#select()^*+[what()when()mul(448,525)]>:where()&^who()&mul(611,331):!)*/]}mul(37,42)>mul(538,106)when()why()mul(36,120)~where()-{+from()$'mul(950,456))mul(28,237)what()when(479,124)mul(697,976)):**/]&#how()#mul(424,841)why()'!;~mul(108,859)~%{?!mul(40,521)do()[^when()/%$+ [where()mul(187,953)who()where()select()(select()what()mul(984,77)<@)(/where()from()~;mul(163,398)/who()who()~mul(445,94))what()what()][how(),mul(115,245)--}/#how()what()!mul(366,981)'$why()do()what(565,96)who()mul(128,999):mul(858,772)[,,mul(796,864)why()what()^(mul(136,980)when()?!when()}mul(142,552)(mul(354,328)[(@how() (/~#mul(159,715)where()&mul(567,560)from()$^'$&&+!when()mul(582,489);where();select(),mul(306,841)? ,)how()mul(274,549)@~what()~?*mul(448,441);&<'select()when()when()#select()from()mul(404,209)^/ @who()who()'mul(400,15)';^&&when():{mul(199,543)[from()~+mul(452,787)([select()>/]$!/mul(840,165)when()>^why()~>when()(mul(830,125)from():mul(433,238);%why(){';$mul(494,781),-mul(139,401)&&&+who()>/^select()]do()mul(116,181)+$*[:who() do()how()<what()+mul(392,879)()what()do()from(339,837)}<<where()?{&how()mul(329,298)<who()what(937,474)&]@?mul(920,516);mul(438,991);{why()!]~'from()>mul(927,106)why()<%{{&~'<from()mul(950,746)'mul(240,649)?what(827,689)(mul(750,353)select(720,6)^mul(663,218)<,(why()<who()^>%why()mul(617?from()select()<what()mul(873,278)&^where(86,235)mul(170,108)!select()mul(66,5)@$^,~%from()mul(785,826): ~who(){mul(383,166):!![:~}+-'mul(554,291)@^)(^#when()when()why()mul(330,699)[:how(888,93)who()how(863,345)who()mul{how()-why()who()]$^mul(512,474)^@:mul(728,970)%mul(779,946)&& mul(216,667) where()^'%mul(788,642)how()>from()}$mul(915,977)& &mul(477,287){# mul(798,930)]mul(111select()*^@@/what()mul(518,86):('({&~{why()mul(991,855)*%^who()who()$/:{$mul(827,700)-'(mul(377,585)#&mul(171,537)when()@/>{< ,*:mul(349,478)!&^{-/mul(448,750)mul(868,546)mul(893,203)",
						]
    		


if __name__ == "__main__":
	unittest.main()
