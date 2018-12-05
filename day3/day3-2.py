# import re
# from claim import Claim

# filepath = 'input.txt'
# claims = []
# unprocessed_claims = file(filepath).readlines()
# overlap = False
# claim_id_answer = 0
# for un_claim in unprocessed_claims:
# 	claims.append(Claim(un_claim))
# for first_claim_id, claim in enumerate(claims, 1):
# 	claim_id_answer = first_claim_id
# 	for second_claim_id in range(len(claims)):
# 		if first_claim_id == second_claim_id:
# 			second_claim_id += 1
# 		if claim.box.overlaps(claims[second_claim_id].box):
# 			# print str(first_claim_id) + " overlaps " + str(second_claim_id)
# 			claim_id_answer = 0
# 			break
# 	if not (claim_id_answer == 0):
# 		print("Claim ID #" + str(claim_id_answer) + " is the one")

from collections import defaultdict

#1373 @ 130,274: 15x26
C = defaultdict(int)
for line in open('input.txt'):	
	words = line.split()
	x,y = words[2].split(',')
	x,y = int(x), int(y[:-1])
	w,h = words[3].split('x')
	w,h = int(w), int(h)
	for dx in range(w):
		for dy in range(h):
			C[(x+dx, y+dy)] += 1
for line in open('input.txt'):
	words = line.split()
	x,y = words[2].split(',')
	x,y = int(x), int(y[:-1])
	w,h = words[3].split('x')
	w,h = int(w), int(h)
	ok = True
	for dx in range(w):
		for dy in range(h):
			if C[(x+dx, y+dy)] > 1:
				ok = False
	if ok:
		print words[0]

ans = 0
for (r,c),v in C.items():
    if v >= 2:
        ans += 1
print ans