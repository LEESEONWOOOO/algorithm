import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = []
C = []

for j in range(N):
    B.append(j+1)

for i in range(N):
    if A[i] != B[i]:
        C.append(i)

print(len(C))

