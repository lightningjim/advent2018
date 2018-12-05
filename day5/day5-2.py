import string

filepath = 'input.txt'
polymer = ''
result = ''
p_prime = ''
result_drops = []

with open(filepath, 'r') as f:
	polymer = f.read()
	f.close()

# print polymer

for letter in string.ascii_lowercase:
	for p in polymer:
		# print "Testing: " + p_prime + p
		#First character or same case (includes same character)
		if (p == letter) or (p == letter.upper()):
			# print("Dropping " + p + "/" + p.upper() + " unit")
			continue
		if p_prime == '' or (p_prime.islower() and p.islower()) or (p_prime.isupper() and p.isupper()):
			p_prime = p
			result += p
			# print("Nothing happens")
		else:
			if (p_prime.lower() == p) or (p_prime == p.lower()):
				result = result[:-1]
				if (len(result) > 0):
					p_prime = result[-1]
				else:
					p_prime = ''
				# print("Annihilated")
			else:
				p_prime = p
				result += p
				# print("Nothing happens")
		# print("String length: " + str(len(result)))
	result_drops.append([letter, len(result)])
	result = ''
	p_prime = ''

# print result
print result_drops