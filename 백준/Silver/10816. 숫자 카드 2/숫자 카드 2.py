from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/10816
N = int(input().strip())
cards = list(map(int, input().split()))

dic = {}

for c in cards:
    if dic.get(c):
        dic[c] += 1
    else:
        dic[c] = 1

N = int(input().strip())
find = list(map(int, input().split()))

for f in find:
    if dic.get(f):
        print(dic[f], end = ' ')
    else:
        print(0, end = ' ')