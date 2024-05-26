import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

res = min(A)
result = max(A)

print(str(res) + " " + str(result))
