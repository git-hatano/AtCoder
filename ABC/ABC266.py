'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# Yes/Noテンプレ
ans = True
print("Yes" if ans else "No")
'''

def A():
    s = input() 
    i = (len(s)-1+1)//2
    print(s[i])

def B():
    v = 998244353
    n = int(input())

    i = n//v
    x = n - v*i
    print(x)

def C():
    """
    三角形の符号付き面積
        角v0-v1-v2 のなす角の大きさを判定
        https://qiita.com/NULLchar/items/aef3c133ee7a98410039
    [in]
        v0: [x0, y0]
        v1: [x1, y1]
        v2: [x2, y2]
    [return]
        s>0: 180度未満
        s<0: 180を超える
    """
    def func(v0, v1, v2):
        s = 1/2*(v0[0]*v1[1] + v1[0]*v2[1] + v2[0]*v0[1] - v0[1]*v1[0] - v1[1]*v2[0] - v2[1]*v0[0])
        return s

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    ans = True
    #A
    s = func(d, a, b)
    if s<0:
        ans = False
    #B
    s = func(a, b, c)
    if s<0:
        ans = False
    #C
    s = func(b, c, d)
    if s<0:
        ans = False
    #D
    s = func(c, d, a)
    if s<0:
        ans = False
        
    print("Yes" if ans else "No")


"""
多分DP、選ぶ選ばないの場合分けをしていく感じ？
Ans: DPだった

DP[x][t]
高橋君が時刻tに座標xにいるときの、それまでに捕まえた大きさの合計の最大値
"""
def D():
    m = 10**5 +5
    n = int(input())
    X = [0]*m
    A = [0]*m
    for i in range(n):
        t, x, a = map(int, input().split())
        X[t] = x
        A[t] = a

    INF = 10**18
    dp = [[-INF]*5 for i in range(m)]
    dp[0][0] = 0
    for i in range(m-1):
        ni = i+1
        for j in range(5):
            for nj in range(j-1, j+2):
                if nj<0 or 5<=nj:
                    continue
                dp[ni][nj] = max(dp[ni][nj], dp[i][j])
        dp[ni][X[ni]] += A[ni]

    ans = -INF
    for j in range(5):
        ans = max(ans, dp[m-1][j])
    print(ans)
