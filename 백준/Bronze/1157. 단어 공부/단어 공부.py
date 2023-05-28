word = input().upper()
count = [0] * 91

for i in range(len(word)):
    w = word[i]
    count[ord(w)] += 1

idx = count.index(max(count))
answer = chr(idx)

count.sort(key = lambda x : -x)

if len(word) >= 2 and count[0] == count[1]:
    answer = '?'
    
print(answer)