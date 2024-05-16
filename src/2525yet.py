A, B = input().split()
A, B = int(A), int(B)

C = int(input())

# 1000//60 = 16 | 17 40 60 |
if B + C >= 60:
    A += (B + C) // 60
    B = (B + C) % 60
    if A >= 24:
        A -= 24
else:
    B = B + C

print(A, B)
