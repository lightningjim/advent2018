import re
from shapely.geometry import box

class Claim:

	regex_claim = re.compile("#(\d{1,4})\ ")
	regex_start = re.compile("@\ (\d{1,4}),(\d{1,4})")
	regex_size = re.compile(":\ (\d{1,4})x(\d{1,4})")

	def __init__(self, init_string):
		self.claim_id = int(self.regex_claim.findall(init_string)[0])
		self.start = [int(number) for number in self.regex_start.findall(init_string)[0]]
		self.size = [int(number) for number in self.regex_size.findall(init_string)[0]]
		self.box = 	box(self.start[0], self.start[1], self.start[0] + self.size[0], self.start[1] + self.size[1])
		# print(list(self.box.bounds))