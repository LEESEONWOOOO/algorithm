N = 9
A = []

for i in range(N):
    A.append(int(input()))

res = max(A)
print(res)
print(A.index(res) + 1)