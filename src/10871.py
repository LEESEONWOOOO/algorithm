import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
# 질문 : list[] 안에 쓰는게 아니라 list() 안에 쓰는거임?

S = ''
# S는 결괏값

for i in range(N):
    if A[i] <X:
        S += str(A[i]) + " "
        # 공백을 포함시켜야 함
print(S)
# 만약에 결과에 공백을 포함시키면 '1234 ' 로 출력됨 ㅡㅡ;
