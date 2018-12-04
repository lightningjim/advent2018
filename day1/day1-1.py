filepath = 'input.txt'
frequency = 0;
with open(filepath) as fp:
	line = fp.readline()
	while line:
		#print(int(line));
		frequency += int(line)
		line = fp.readline()
print ("Final Frequency: " + str(frequency));