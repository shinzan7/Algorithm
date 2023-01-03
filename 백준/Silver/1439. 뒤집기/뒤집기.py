import sys

S = sys.stdin.readline().strip()

cnt0 = 0
cnt1 = 0

a = S[0]
if(a == "0"):
    cnt0 += 1
else:
    cnt1 += 1

for i in S:
    if(a != i):
        if(a == "0"):
            cnt1 += 1
        else:
            cnt0 += 1
        a = i

print(cnt0 if cnt0 <= cnt1 else cnt1)