from sys import stdin

input = stdin.readline

# https://www.acmicpc.net/problem/18870
# 중복을 제거하여 오름차순으로 정렬한 리스트를 새로 만든다
N = int(input().strip())
arr = list(map(int, input().split()))
arr2 = list(set(arr))
arr2.sort()

dic = {arr2[i]:i for i in range(len(arr2))}
for a in arr:
    print(dic[a], end=' ')