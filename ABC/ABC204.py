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
ans = False
print("Yes" if ans else "No")
'''

def A():
    x, y = map(int, input().split())
    if x==y:
        ans = x
    else:
        tmp = [0, 1, 2]
        tmp.remove(x)
        tmp.remove(y)
        ans = tmp[0]
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i]>10:
            ans += (a[i]-10)
    print(ans)


"""
dfs 
グラフ理論全然分からん
再起関数の書き方分からん
どちらも今まで当たったことないから苦手なので、これから問題を通して慣れていく
"""
def C():
    #再帰回数の上限を変更
    import sys
    sys.setrecursionlimit(10000)

    n, m = map(int, input().split())
    g = [[] for i in range(n)]
    #g[i]は都市iから道路で直接つながっているリスト
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)

    def dfs(v):
        if temp[v]:
            #同じ頂点を2度調べないためのreturn
            return 
        temp[v] = True
        for vv in g[v]:
            dfs(vv)

    ans = 0
    #都市iからスタートする場合
    for i in range(n):
        #temp[j]は都市jに到達可能かを表す
        temp = [False]*n
        dfs(i)
        ans += sum(temp)
        
    print(ans)


"""
いくつかの値を選んで作ることができるか？』は、部分和問題という有名な問題で、
動的計画法

dp[i][j]
i個目まで決めて、sum(a)をjとできるか
O(n*t)
"""
def D_ans():
    n = int(input())
    t = list(map(int, input().split()))
    s = sum(t)

    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(s+1):
            """
            dp[i + 1][j]がTrueになるのは、
            dp[i][j] が True（T[i]を使わない場合）
            dp[i][j - t] が True（T[i]を使う場合）
            のどちらかです
            """
            if dp[i][j]:
                dp[i+1][j] = True
            if j-t[i]>=0 and dp[i][j-t[i]]:
                dp[i+1][j] = True

    ans = 10**10
    for i in range(s+1):
        if dp[n][i]:
            score = max(i, s-i) # 片方をiにすると、もう片方はs-i
            ans = min(ans, score)
    print(ans)

