N, M = map(int, input().split())
    # 첫번째 줄에서 N과 M을 입력받는다
A = [0] * (N+1)
    # 이가 N+1인 리스트를 생성하고 리스트의 모든 요소를 0으로 초기화

for s in range(M):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        A[l] = k

for k in range(1, len(A)):
    print(A[k], end=' ')
