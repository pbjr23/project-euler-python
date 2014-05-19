fin = open('pr18.txt')
all = []
for i in fin:
	all.append(i.strip().split(' '))

for row in range(len(all)):
	print all[row]