A, B, C = map(int, input().split())
D = 0

arr = [A, B, C]
arr.sort()

if A == B and B == C:
    D = 10000 + A * 1000
elif A == B:
    D = 1000 + A * 100
elif B == C:
    D = 1000 + B * 100
elif A == C:
    D = 1000 + A * 100
else:
    D = arr[2] * 100

print(D)
