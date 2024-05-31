while True:
    try:
        N = int(input().strip())
        break
    except ValueError:
        print("ERROR")
while True:
    try:
        M = int(input().strip())
        break
    except ValueError:
        print("ERROR")

i = 0
k = 0
j = 0

for s in range(M):
    i,j,k = int(input())

Arr = [i, j, k]

## 환장하겠노; 2024-06-01

