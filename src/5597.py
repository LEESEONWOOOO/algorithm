A = [i for i in range(1,31)]

for j in range(28):
    S = int(input())
    A.remove(S)

print(min(A))
print(max(A))