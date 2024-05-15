A, B = input().split()
A, B = int(A), int(B)

C = int(input())

# 1000//60 = 16 | 17 16
if B+C >= 60:
    A += (B+C)//60
    if A >= 24:
        A = 40 - A
