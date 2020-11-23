import re
hand = open('a.txt')
numlist = list()
count = 0
for line in hand:
   line = line.rstrip()
   stuff = re.findall('([0-9]+)', line)
   if len(stuff) !=1 : continue
   for nm in stuff: 
     num = int(nm)
     numlist.append(num)
print(sum(numlist))
print(numlist)
