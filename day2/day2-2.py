import string

filepath = 'input.txt'
id_list = file(filepath).readlines()
for first_index, box_id in enumerate(id_list):
	second_index = first_index + 1
	while second_index < len(id_list):
		second_box_id = id_list[second_index]
		differences = 0
		for i in range(25):
			if not(box_id[i] == second_box_id[i]):
				differences += 1
		if differences == 1:
			print ("Box IDs are " + box_id + " and " + second_box_id)
			exit(0)
		second_index += 1

