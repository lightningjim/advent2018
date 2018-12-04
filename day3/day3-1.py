import string
import re

filepath = 'input.txt'

side_length = 1000

cloth = [[0 for i in range(side_length)] for j in range(side_length)]
overlapArea = 0

regex_claim = re.compile("#(\d{1,4})\ ")
regex_start = re.compile("@\ (\d{1,4}),(\d{1,4})")
regex_size = re.compile(":\ (\d{1,4})x(\d{1,4})")
claims = []

unprocessed_claims = file(filepath).readlines()
for un_claim in unprocessed_claims:
	claim = regex_claim.findall(un_claim)[0]
	start = regex_start.findall(un_claim)[0]
	start_x = start[0]
	start_y = start[1]
	size = regex_size.findall(un_claim)[0]
	size_x = size[0]
	size_y = size[1]
	claims.append([int(start_x), int(start_y), int(size_x), int(size_y)])
	#print("Claim #" + str(claim) + ": " + str(start_x) + "," + str(start_y) + " size - " + str(size_x) + "x" + str(size_y))
for claim in claims:
	for x in range(claim[0], claim[0]+claim[2]):
		for y in range(claim[1], claim[1]+claim[3]):
			# if cloth[x][y] > 0:
			# 	print "Overlap"
			cloth[x][y] += 1

for row in cloth:
	for col in row:
		if col > 1:
			overlapArea += 1
print ("Overlap area: " + str(overlapArea))