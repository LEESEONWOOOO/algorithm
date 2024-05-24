N = int(input())
A = 0

for i in range(1, N + 1):
    A = " " * (N - i)

    print(A + i * "*")