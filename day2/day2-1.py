import string

filepath = 'input.txt'
two_letters = 0;
three_letters = 0;
twoLettersFound = False;
threeLettersFound = False;
letters = list(string.ascii_lowercase)
with open(filepath) as fp:
	line = fp.readline()
	while line:
		for letter in letters:
			totalFound = line.count(letter)
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
		line = fp.readline()
print("Checksum: " + str(two_letters * three_letters))