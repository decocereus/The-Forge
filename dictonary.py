fname = input('Enter a file: ')
handle = open(fname)

python4eb = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        python4eb[word] = python4eb.get(word,0) + 1

#print(python4eb.items())

bigword = None
bigcount = None

for k,v in python4eb.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k

print(bigword,bigcount)
