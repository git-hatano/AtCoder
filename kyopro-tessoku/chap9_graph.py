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
ans = True #ans = False
print("Yes" if ans else "No")

# リストの中身を文字列に
ans = " ".join([str(x) for x in a])
'''

def A61():
    from collections import defaultdict
    g = defaultdict(list)

    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, n+1):
        if i in g:
            print(str(i) +": {"+ ", ".join([str(x) for x in g[i]]) +"}")
        else:
            print(str(i) +": {}")


def B61():
    from collections import defaultdict
    g = defaultdict(list)

    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    person = -1
    friends = -1
    for i in range(1, n+1):
        if i in g:
            if len(g[i]) > friends:
                person = i
                friends = len(g[i])
    print(person)


def A62():
    import sys
    sys.setrecursionlimit(10**6)
    from collections import defaultdict
    g = defaultdict(list)

    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    visited = [False]*n
    def dfs(cur):
        if visited[cur]:
            return
        
        visited[cur] = True
        for nex in g[cur]:
            dfs(nex)
        return

    dfs(0)
    ans = "The graph is connected."
    for i in range(n):
        if not visited[i]:
            ans = "The graph is not connected."
    print(ans)


"""
単純パスの探索
TLE & WA
ルートの管理が分からない
再帰関数の設計がうまくできない
"""
def B62_WA():
    import sys
    sys.setrecursionlimit(10**6)
    from collections import defaultdict
    g = defaultdict(list)

    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    root = []
    def dfs(pre, cur):
        if len(root)>0 and root[-1]==0:
            return
        
        root.append(cur)
        for nex in g[cur]:
            if pre!=nex:
                dfs(cur, nex)
        return

    dfs(-1, n-1)
    ans = " ".join([str(x+1) for x in reversed(root)])
    print(ans)


"""
単純パスはstackで管理するとうまくいく
"""
def B62():
    import sys
    sys.setrecursionlimit(10**6)
    from collections import defaultdict
    g = defaultdict(list)

    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    visited = [False]*n
    path = []

    def dfs(cur):
        #ゴールに着いた時
        if cur==n-1:
            ans = " ".join([str(x+1) for x in path])
            print(ans)
            sys.exit()
        
        visited[cur] = True
        for nex in g[cur]:
            if not visited[nex]:
                path.append(nex)
                dfs(nex)
        path.pop()

    cur = 0
    path.append(cur)
    dfs(cur)


"""
最短経路問題: 幅優先探索
"""
def A63():
    from collections import deque
    from collections import defaultdict
    g = defaultdict(list)
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    dist = [-1]*n
    dist[0] = 0
    que = deque([])
    que.append(0)
    while len(que)>0:
        pos = que.popleft()
        if pos in g:
            for to in g[pos]:
                if dist[to]<0:
                    que.append(to)
                    dist[to] = dist[pos]+1
    for i in range(n):
        print(dist[i])


def B63():
    from collections import deque
    from collections import defaultdict
    g = defaultdict(list)

    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1
    start = sy*w+sx
    gy, gx = map(int, input().split())
    gy -= 1
    gx -= 1
    goal = gy*w+gx
    c = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if c[i][j]=="#" :
                continue
            #下方向
            if i+1<h and c[i+1][j]=="." :
                g[i*w+j].append((i+1)*w+j)
            #上方向
            if i-1>=0 and c[i-1][j]==".":
                g[i*w+j].append((i-1)*w+j)
            #右方向
            if j+1<w and c[i][j+1]==".":
                g[i*w+j].append(i*w+j+1)
            #左方向
            if j-1>=0 and c[i][j-1]==".":
                g[i*w+j].append(i*w+j-1)

    dist = [-1]*(h*w)
    dist[start] = 0
    que = deque([])
    que.append(start)

    while len(que)>0:
        pos = que.popleft()
        if pos in g:
            for to in g[pos]:
                if dist[to]==-1:
                    que.append(to)
                    dist[to] = dist[pos]+1
    print(dist[goal])


"""
重み付き最短経路問題
ダイクストラ法
heapqueを使って最小のコストを管理する
"""
def A64_ans():
    import heapq
    from collections import defaultdict
    g = defaultdict(list)
    n, m = map(int, input().split())
    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append([b, c])
        g[b].append([a, c])

    #配列の初期化
    kakutei = [False]*n
    cur = [10**10]*n
    cur[0] = 0
    #スタート地点をキューに追加
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (cur[0], 0))

    #ダイクストラ法
    while len(que)>0:
        #次に確定させるべき頂点を選ぶ
        pos = heapq.heappop(que)[1]
        #queの最小要素が既に確定した頂点の場合
        if kakutei[pos]:
            continue
        #cur[x]の値を更新
        kakutei[pos] = True
        for i in range(len(g[pos])):
            nex = g[pos][i][0]
            cost = g[pos][i][1]
            if cur[nex] > cur[pos]+cost:
                cur[nex] = cur[pos]+cost
                heapq.heappush(que, (cur[nex], nex))

    for i in range(n):
        if cur[i]==10**10:
            print(-1)
        else:
            print(cur[i])


def B64():
    import heapq
    from collections import defaultdict
    g = defaultdict(list)
    n, m = map(int, input().split())
    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append([b, c])
        g[b].append([a, c])

    #配列の初期化
    kakutei = [False]*n
    cur = [10**10]*n
    cur[0] = 0
    #スタート地点をキューに追加
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (cur[0], 0))

    #ダイクストラ法で各頂点への最短経路を求める
    while len(que)>0:
        #次に確定させるべき頂点を選ぶ
        pos = heapq.heappop(que)[1]
        #queの最小要素が既に確定した頂点の場合
        if kakutei[pos]:
            continue
        #cur[x]の値を更新
        kakutei[pos] = True
        for i in range(len(g[pos])):
            nex = g[pos][i][0]
            cost = g[pos][i][1]
            if cur[nex] > cur[pos]+cost:
                cur[nex] = cur[pos]+cost
                heapq.heappush(que, (cur[nex], nex))

    #頂点n-1から頂点0に戻るルートを復元
    root = []
    pos = n-1
    root.append(pos)
    while pos!=0:
        for i in range(len(g[pos])):
            nex = g[pos][i][0]
            cost = g[pos][i][1]
            if cur[nex] == cur[pos]-cost:
                root.append(nex)
                pos = nex
                break
    ans = " ".join([str(x+1) for x in reversed(root)])
    print(ans)


def A65():
    from collections import defaultdict
    g = defaultdict(list)
    n = int(input())
    a = list(map(int, input().split()))
    #上司と部下の関係をグラフに
    for i in range(n-1):
        g[a[i]-1].append(i+1)

    #dp[x]: 社員xの部下数
    dp = [0]*n
    for i in reversed(range(n)):
        for j in range(len(g[i])):
            dp[i] += dp[g[i][j]]+1

    ans = " ".join([str(x) for x in dp])
    print(ans)


"""
dfsの設計ができない
"""
def B56_ans():
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10**6)
    g = defaultdict(list)
    n, t = map(int, input().split())
    t -= 1
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    #dp[x]: 社員xの部下数
    ans = [-1]*n
    visited = [False]*n
    #社員posの階級を返す
    def dfs(pos):
        visited[pos] = True
        ans[pos] = 0
        for nex in g[pos]:
            if visited[nex] == False:
                ret = dfs(nex)
                ans[pos] = max(ans[pos], ret+1)#階級を更新
        return ans[pos]

    dfs(t)
    ans = " ".join([str(x) for x in ans])
    print(ans)


class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*n #最初は親がない
        self.siz = [1]*n #最初はグループの頂点数が1
    
    #頂点xの親を返す関数
    def root(self, x):
        while True:
            if self.par[x]==-1: #1個先(親)がなければここが親
                break
            x = self.par[x] #1個先(親)に進む
        return x
    
    #要素uと要素vを統合する関数
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u==root_v: #uとvが同じグループなら何もしない
            return
        if self.siz[root_u] < self.siz[root_v]:
            self.par[root_u] = root_v
            self.siz[root_v] += self.siz[root_u]
        else:
            self.par[root_v] = root_u
            self.siz[root_u] += self.siz[root_v]
    
    #uとvが同じグループかを返す関数
    def same(self, u, v):
        return self.root(u)==self.root(v)


def A66():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for i in range(q):
        t, u, v = map(int, input().split())
        u -= 1
        v -= 1
        if t==1:
            uf.unite(u, v)
        elif t==2:
            print("Yes" if uf.same(u, v) else "No")


"""
最小全域木問題
コストが小さい順につなげていく
"""
def A67():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    paths = [list(map(int, input().split())) for _ in range(m)]
    paths = sorted(paths, key=lambda x: x[2])
    ans = 0
    for i in range(m):
        a = paths[i][0]-1
        b = paths[i][1]-1
        c = paths[i][2]
        if not uf.same(a, b):
            ans += c
            uf.unite(a, b)
    print(ans)

"""
最大全域木問題
コストが大きい順につなげていく
"""
def B67():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    paths = [list(map(int, input().split())) for _ in range(m)]
    paths = sorted(paths, key=lambda x: x[2], reverse=True)###
    ans = 0
    for i in range(m):
        a = paths[i][0]-1
        b = paths[i][1]-1
        c = paths[i][2]
        if not uf.same(a, b):
            ans += c
            uf.unite(a, b)
    print(ans)


"""start-------------------------------maxflow------------------------------------------"""
#最大フロー用の構造体
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

"""
深さ優先探索
Fはスタートからposに到達する過程での残余グラフの辺の容量の最小値
帰り値は流したフローの量
"""
def dfs(pos, goal, F, G, used):
    #ゴールに到着: フローを流せる
    if pos == goal: 
        return F
    #探索
    used[pos] = True
    for e in G[pos]:
        #容量が1以上でかつ、まだ訪問していない頂点のみに行く
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            #フローを流せる場合、残余グラフの容量をflowだけ増減
            if flow>=1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    #全ての辺を探索しても見つからない場合
    return 0


"""
頂点sから頂点tまでの最大フローの総流量を返す
N: 頂点数
edges: 辺のリスト
"""
def maxflow(N, s, t, edges):
    #初期状態の残余グラフを構築
    G = [list() for i in range(N+1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a])-1))
    
    INF = 10**10
    total_flow = 0
    while True:
        used = [False]*(N+1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break #フローを流せなくなったら終了
    return total_flow

"""------------------------------------maxflow---------------------------------------end"""


#二部マッチング問題
def A69():
    n = int(input())
    c = [input() for i in range(n)]

    #最大フローを求めたいグラフを構築する
    #辺の要素は、(辺の始点番号, 辺の終点番号, 辺の容量) のタプル
    edges = []
    for i in range(n):
        for j in range(n):
            if c[i][j]=="#":
                edges.append((i+1, n+j+1, 1)) #i番目の青色頂点とj番目の赤色頂点をつなぐ

    for i in range(n):
        edges.append((2*n+1, i+1, 1)) #s→青色の辺
        edges.append((n+i+1, 2*n+2, 1)) #赤色→tの辺

    ans = maxflow(2*n+2, 2*n+1, 2*n+2, edges)
    print(ans)


"""
コードを書く前に適切なフローを書けたら上手くいけそう
"""
def B69():
    n, m = map(int, input().split())
    c = [input() for i in range(n)]
    lim_time = 10#一人当たりの最大勤務時間
    #edge[i]: (start, goal, cost)
    edges = []
    for i in range(n):
        for j in range(24):
            if c[i][j]=="1":
                edges.append((i+1, n+j+1, 1)) #青と赤をつなぐ

    for i in range(n):
        edges.append((n+25, i+1, lim_time)) #s→青色の辺
    for j in range(24):
        edges.append((n+j+1, n+26, m)) #赤色→tの辺

    ans = maxflow(n+26, n+25, n+26, edges)
    if ans == 24*m:
        print("Yes")
    else:
        print("No")


def A70():
    #頂点posから、ランプx,y,zの状態を反転させた時の頂点番号を返す関数
    def get_next(pos, x, y, z):
        #posの2進法表記を使って、頂点posが表すランプの状態 stateを計算
        state = [ (pos // (2**i)) %2 for i in range(n) ]
        #ランプx,y,zを反転
        state[x] = 1 - state[x]
        state[y] = 1 - state[y]
        state[z] = 1 - state[z]
        
        #ランプの状態stateを示す頂点の番号を計算
        ret = 0
        for i in range(n):
            if state[i]==1:
                ret += 2**i
        return ret

    from collections import deque
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    actions = [list(map(lambda x: int(x)-1, input().split())) for i in range(m)]

    #グラフに辺を追加
    G = [list() for i in range(2**n)]
    for i in range(2**n):
        for x, y, z in actions:
            nextstage = get_next(i, x, y, z)
            G[i].append(nextstage)

    #スタート地点、ゴール地点の頂点番号を決める
    start = 0
    for i in range(n):
        if a[i]==1:
            start += 2**i
    goal = 2**n -1

    #幅優先探索の初期化
    dist = [-1]*(2**n)
    dist[start] = 0
    q = deque()
    q.append(start)

    #幅優先探索
    while len(q)>=1:
        pos = q.popleft()
        for nex in G[pos]:
            if dist[nex]==-1:
                dist[nex] = dist[pos]+1
                q.append(nex)
    print(dist[goal])

