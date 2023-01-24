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
    a, b = map(int, input().split())
    c = (a-b)/3 +b
    print(c)


def B():
    s = []
    for _ in range(4):
        s.append(input())
    s = set(s)

    if len(s)==4:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No") 


"""
もらうDP
"""
def C_ans1():
    s = input()
    mod = 10**9+7

    n = len(s)
    dp = [[0]*(9) for i in range(n+1)]
    dp[0][0] = 1

    t = "chokudai"
    for i in range(n):
        for j in range(9):
            dp[i+1][j] = (dp[i+1][j]+dp[i][j])%mod
            if j<8 and s[i]==t[j]:
                dp[i+1][j+1] = (dp[i+1][j+1]+dp[i][j])%mod
    print(dp[n][8])


"""
配るDP
"""
def C_ans2():
    s = input()
    mod = 10**9+7

    n = len(s)
    dp = [[0]*(9) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    t = "chokudai"
    for i in range(n):
        for j in range(8): #8=len(t)
            if s[i]!=t[j]:
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j])%mod
    print(dp[n][8])


"""
AC24, WA6: 数え漏れの経路がありそう
"""
def D_WA():
    from collections import defaultdict, deque
    mod = 10**9 +7
    n, m = map(int, input().split())
    g = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    #BFSで予め最短距離を求める
    dist = [10**9]*n
    dist[0] = 0
    que = deque()
    que.append(0)
    s = set([0])
    while que:
        v = que.popleft()
        for i in g[v]:
            if i not in s:
                que.append(i)
                s.add(i)
                dist[i] = min(dist[i], dist[v]+1)
    min_dist = dist[n-1]

    #BFSで最短距離になる経路数を数える
    ans = 0
    dist = [10**9]*n
    dist[0] = 0
    que = deque()
    que.append(0)
    s = set([0])
    while que:
        v = que.popleft()
        for i in g[v]:
            if i==n-1 and dist[v]+1==min_dist:
                ans += 1
                ans %= mod
            if i not in s: #多分ここで引っかかってるけど無くしたら無限ループ
                que.append(i)
                s.add(i)
                dist[i] = min(dist[i], dist[v]+1)
    print(ans)


"""
最短経路の数え上げ : ダイクストラ法の応用
https://qiita.com/taka256/items/a023a11efe17ab097433#:~:text=%7D%0A%20%20%20%20%7D%0A%7D-,%E7%B5%8C%E8%B7%AF,-%E3%81%AE%E6%95%B0%E3%81%88
これを改変すればコストありのグラフにも応用できそう
"""
def D():
    from collections import defaultdict
    import heapq
    mod = 10**9 +7
    n, m = map(int, input().split())
    g = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    cost = 1
    d = [float("inf")]*n
    cnt = [0]*n
    d[0] = 0 #頂点0への距離
    cnt[0] = 1 #頂点0への経路数

    que = []
    heapq.heapify(que)
    heapq.heappush(que, (d[0], 0)) #(dist: 頂点i)

    while len(que)>0:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in g[v]: #頂点vから出る辺eを走査
            if d[i] > d[v]+cost: #今の最短距離よりも小さければ更新
                d[i] = d[v]+cost
                heapq.heappush(que, (d[i], i))
                cnt[i] = cnt[v]%mod #コストが更新された場合は直前の頂点への最短経路数で上書き
            elif d[i] == d[v]+cost: 
                cnt[i] += cnt[v]%mod #コストが一致する場合はこれまでの最短経路数を足し合わせ
    print(cnt[n-1]%mod)
