T = int(input())
x = 0

for i in range(T):
    A,B = map(int, input().split())
    x += 1
    C = A + B

    print(f"Case #{x}: {A} + {B} = {C}")