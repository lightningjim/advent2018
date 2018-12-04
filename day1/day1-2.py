filepath = 'input.txt'
frequency_list = map(int,file(filepath).readlines())
running_freq_list = [0]
loop = 1
frequency = 0

while True:
    for freq_change in frequency_list:
        frequency += freq_change
        #Check if in list already
        if frequency in running_freq_list:
            print("Duplicate frequency found: " + str(frequency) + " in loop " + str(loop))
            exit(0)
        else:
            # print("Loop " + str(loop) + " - Freq "+ str(frequency) + " - length array " + str(len(running_freq_list)))
            running_freq_list.append(frequency)
    loop += 1