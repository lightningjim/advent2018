# import array

# filepath = 'input.txt'
# frequency = 0;
# #frequency_list = [0 for x in xrange(-124339,440)]
# #frequency_list[0] = 1
# #print(frequency_list)
# #min = 0;
# #max = 0; 
# frequency_list = [0];
# for y in range(0,100):
# 	with open(filepath) as fp:
# 		line = fp.readline()
# 		while line:
# 			#print(int(line));
# 			frequency += int(line)
# 			#if frequency > max:
# 			#	max = frequency
# 			#if frequency < min:
# 			#	min = frequency
# 			#print(str(frequency) + " | "  + str(frequency_list[frequency]))
# 			for freq in frequency_list:
# 				if(freq == frequency):
# 					print("Loop " + str(y) + ": duplicate found at " + str(frequency))
# 			frequency_list.append(frequency)
# 			line = fp.readline()
# #print ("Final Frequency: " + str(frequency));
# #print ("Min: " + str(min) + " | Max: " + str(max))
path = './input.txt'
observations = open(path, 'r')
 
# read observations from file
obsFromFile = observations.read()
obsFromFile = obsFromFile.split('\n')
observations.close()
 
# remove last element in list - empty
obsFromFile.pop()
results = list(map(int, obsFromFile))
 
whileCount = 0
resFreq = []
tempSum = 0
count = 0
 
while True:
    whileCount = whileCount + 1;
    resFreq = []
    tempSum = 0
 
    for res in results:
 
        tempSum = tempSum + res
 
        resFreq.append(tempSum)
 
        dupes = []
        unique = []
 
        for rf in resFreq:
            if rf not in unique:
                unique.append(rf)
            else:
                dupes.append(rf)
                print('Iteration: ', whileCount, 'First Dup: ', dupes)
                exit(0)
 
    results = resFreq