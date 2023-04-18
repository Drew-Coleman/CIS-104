import re
rev = []
rev_ave = 0
fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()
for line in fhand:
    line = line.rstrip()
    rev_temp = re.findall('^New Revision: ([0-9.]+)', line)
    for val in rev_temp:
        val = float(val)            
        rev = rev + [val]           
rev_sum = sum(rev)
count = float(len(rev))
if count:
    rev_ave = rev_sum / count
print(rev_ave)