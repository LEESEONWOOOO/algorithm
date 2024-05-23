import sys

T = int(input())
C = 0
# Case의 수 T를 초기화

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    C += 1
    # if C = 5라면 1부터 5까지 차례대로 출력

    D = A + B
    # 문자열끼리 더할 수 없으므로 미리 더한 값을 정의

    print("Case #" + str(C) + ": " + str(D))
    # 문자열끼리 더해야 하므로 C와 D를 문자로 변환시켜줌
