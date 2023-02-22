from sys import stdin
from itertools import permutations

input = stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))
arr = []
arr += ['+']*temp[0]
arr += ['-']*temp[1]
arr += ['*']*temp[2]
arr += ['/']*temp[3]

nset = set(permutations(arr))
maxx = int(-1e9)
minn = int(1e9)

def calcul(a,str,b):
    if str == '+':
        return a+b
    elif str == '-':
        return a-b
    elif str == '*':
        return a*b
    else:
        if a*b < 0:
            return -(-a//b)
        else:
            return a//b

for n in nset:
    cur = nums[0]
    for i in range(1,N):
        cur = calcul(cur,n[i-1],nums[i])
    maxx = max(maxx, cur)
    minn = min(minn, cur)

print(maxx)
print(minn)