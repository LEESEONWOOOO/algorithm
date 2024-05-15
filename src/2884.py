A, B = input().split()
A, B = int(A), int(B)

# 01:45 23:45
if 0 <= A < 24 and 45 <= B <= 59:
    print(A, B - 45)
# 01:44 23:44
if 0 < A <= 24 and B < 45:
    print(A - 1, 60 - (45 - B))
# 00:44
if A == 0 and B < 45:
    print(23, 60 - (45 - B))
# 00:45
