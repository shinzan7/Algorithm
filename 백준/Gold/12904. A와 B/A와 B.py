from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/12904
S = input().strip()
T = input().strip()
answer = 0

# S와 T가 길이가 같아질 때까지 끝 문자에 규칙을 거꾸로 적용하기
while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

if S == T:
    answer = 1

print(answer)