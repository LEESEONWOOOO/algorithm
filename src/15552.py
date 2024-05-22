import sys
# 한 줄 단위로 입력되기 때문에 개행문자를 제거하기 위해
# import를 해야 str 형태의 변수를 정수로 사용가능

T = int(input())

for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)

# 여러줄을 입력받아야 할 때는 시간초과가 생길 수 있으므로
# input() 대신 sys.stdin.readline() 사용