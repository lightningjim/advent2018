filepath = 'input.txt'
running_frequency = 0;
frequency_list = map(int,file(filepath).readlines())
for freq in frequency_list:
	running_frequency += freq
print ("Final Frequency: " + str(running_frequency));