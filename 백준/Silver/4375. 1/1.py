import sys

result = []

while(True):
    line = sys.stdin.readline()
    line = line.strip().replace('\n', '')
    if(len(line) == 0):
        break
    else:
        N = int(line)
        a = 1
        while(a % N != 0):
            a = a * 10 + 1
        result.append(len(str(a)))

for i in result:
    print(i)