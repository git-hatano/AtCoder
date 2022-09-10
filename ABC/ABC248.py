'''
Atcoderのインデントは、スペース2

# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
'''

# A
from re import A


if False:
    # 文字列を受け取る場合
    S = input() 

    s_list = []
    for s in S:
        s_list.append(int(s))

    for n in range(10):
        if n not in s_list:
            print(n)

# B
if False:
    # 複数の整数を入力
    A, B, K = map(int, input().split())

    cnt = 0
    while True:
        if A >= B:
            print(cnt)
            break
        else:
            A = A*K
            cnt += 1


# C
if False:
    N, M, K = map(int, input().split())
    A_list = [1]*N

    cnt = 0
    for n in range(N):
        for m in range(M):
            A_list[n] = m+1

            if sum(A_list) <= K:
                cnt+=1
        
# D
if False:
    import numpy as np

    N = int(input())
    A_list = np.array(list(map(int, input().split())))

    Q = int(input())
    query = []

    for q in range(Q):
        query.append(list(map(int, input().split())))

    for q in query:
        L = q[0] -1
        R = q[1]
        X = q[2]

        print( np.sum( A_list[L:R]==X ) )
   

def D():
    N, M, K = map(int, input().split())
    mod = 998244353

    dp = [[0]*(K+1) for i in range(N+1)]
    dp[0][0] = 1

    for x in range(1, N+1):
        for y in range(0, K+1):
            now = 0
            for i in range(1, M+1):
                if y-i >= 0:
                    now += dp[x-1][y-i]
                    now %= mod
            
            dp[x][y] = now

    ans = 0
    for y in range(0, K+1):
        ans += dp[N][y]
        ans %= mod

    print(ans)
