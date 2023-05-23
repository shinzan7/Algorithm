from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for w in words:
    print(w[0])