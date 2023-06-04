from sys import stdin

input = stdin.readline

result = 0
for _ in range(5):
    n = int(input().strip())
    if n < 40:
        n = 40
    result += n

print(result // 5)