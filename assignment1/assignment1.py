import re, sys
fname = sys.argv[1]
with open(fname, 'r') as file:
	fstring = file.read()
num_list = re.findall('[0-9]+',fstring)
num_list = map(lambda x:int(x), num_list)
print sum(num_list)