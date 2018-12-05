import re
from claim import Claim

filepath = 'input.txt'

side_length = 1000

cloth = [[0 for i in range(side_length)] for j in range(side_length)]
overlapArea = 0
claims = []
# claims_obj = []

unprocessed_claims = file(filepath).readlines()
for un_claim in unprocessed_claims:
	claim = Claim(un_claim)
	claims.append(claim)
	# claim = regex_claim.findall(un_claim)[0]
	# start = regex_start.findall(un_claim)[0]
	# start_x = start[0]
	# start_y = start[1]
	# size = regex_size.findall(un_claim)[0]
	# size_x = size[0]
	# size_y = size[1]
	# claims.append([int(start_x), int(start_y), int(size_x), int(size_y)])
	# #print("Claim #" + str(claim) + ": " + str(start_x) + "," + str(start_y) + " size - " + str(size_x) + "x" + str(size_y))
for claim in claims:
	# print("Range: X - " + str(range(claim.start[0], claim.start[0]+claim.size[0])))
	for x in range(claim.start[0], claim.start[0]+claim.size[0]):
		for y in range(claim.start[1], claim.start[1]+claim.size[1]):
			# if cloth[x][y] > 0:
			# 	print "Overlap"
			cloth[x][y] += 1

for row in cloth:
	for col in row:
		if col > 1:
			overlapArea += 1
print ("Overlap area: " + str(overlapArea))