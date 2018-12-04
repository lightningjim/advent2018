import string
import re
import array

filepath = 'input.txt'

regex_date = re.compile("\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]")
regex_start = re.compile("Guard #(\d{1,4}) begins shift")
regex_awake = re.compile("wakes up")
regex_sleep = re.compile("falls asleep")
highest_id = 10000;


guard_schedule = {}

lines = file(filepath).readlines()

lines.sort()
awake = True
current_guard = 0
last_minute = 0
last_guard = 0
current_guard_schedule = [0 for j in range(0,60)]

def add_schedule(guard, hour):
	found = False
	for number, schedule in guard_schedule.items():
		if number == guard:
			found = True
			new_schedule = [x + y for x, y in zip (schedule, hour)];
			guard_schedule[number] = new_schedule
			break;
	if not found:
		guard_schedule[guard] = hour

for line in lines:
	# test = regex_start.findall(line)
	# if test:
	# 	if int(test[0]) > highest_id:
	# 		highest_id = int(test[0])
	# New guard is new day
	current_minute = int(regex_date.findall(line)[0][4])
	if regex_start.search(line):
		last_minute = 0
		current_guard = int(regex_start.findall(line)[0])
		if not(last_guard == current_guard) and not (last_guard == 0):
			add_schedule(last_guard, current_guard_schedule)
			current_guard_schedule = [0 for j in range(0,60)]
		last_guard = current_guard
		awake = True
		# print("Guard #" + str(current_guard) + " started; is awake")
	if regex_sleep.search(line):
		awake = False
		last_minute = current_minute
		# print("Guard #" + str(current_guard) + " fell asleep at 00:" + str(current_minute))
	if regex_awake.search(line):
		for minute in range(last_minute, current_minute):
			current_guard_schedule[minute] += 1
			# print str(minute) + " - " + str(current_guard_schedule[minute])
		awake = True	
		last_minute = current_minute
		# print("Guard #" + str(current_guard) + " woke up at 00:" + str(current_minute))
# print guard_schedule
most_slept_guard = 0
most_slept_minutes = 0
for number, schedule in guard_schedule.items():
	# print ("Running set: " + str(most_slept_guard) + " - " + str(most_slept_minutes))
	total = sum(schedule)
	# print ("Guard #" + str(number) + " slept " + str(total) + " minutes")
	if total > most_slept_minutes:
		most_slept_minutes = total
		most_slept_guard = number
most_slept_time = 0
most_slept_amount = 0
for minutes, slept_minute in enumerate(guard_schedule[most_slept_guard]):
	if slept_minute > most_slept_amount:
		most_slept_amount = slept_minute
		most_slept_time = minutes
	# print str(minutes)  + " " + str(slept_minute)


print ("Guard #" + str(most_slept_guard) + " is the target, slept " + str(most_slept_minutes) + " minutes")
print ("Most slept time: 00:" + str(most_slept_time))
print("Answer: " + str(most_slept_guard * most_slept_time))
