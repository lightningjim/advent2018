import string

filepath = 'input.txt'
two_letters = 0;
three_letters = 0;
twoLettersFound = False;
threeLettersFound = False;
id_list = file(filepath).readlines()
letters = list(string.ascii_lowercase)
for box_id in id_list:
	for letter in letters:
		totalFound = box_id.count(letter)
		if totalFound == 2:
			if not twoLettersFound: 
				two_letters += 1
				twoLettersFound = True
		if totalFound == 3:
			if not threeLettersFound:
				three_letters += 1
				threeLettersFound = True
		if twoLettersFound and threeLettersFound:
			break
	twoLettersFound = False
	threeLettersFound = False
print("Checksum: " + str(two_letters * three_letters))