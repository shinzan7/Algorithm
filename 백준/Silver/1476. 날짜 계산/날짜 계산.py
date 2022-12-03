from sys import stdin
E, S, M = map(int, stdin.readline().split())
e, s, m = 1, 1, 1
result = 0

for i in range(1, 7981):
    if(e == E and s == S and m == M):
        result = i
        break
    else:
        e += 1
        s += 1
        m += 1
        if(e > 15):
            e = 1
        if(s > 28):
            s = 1
        if(m > 19):
            m = 1

print(result)