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
    c = 0

    xs = [4, 2, 1]
    for x in xs:
        if a>=x or b>=x:
            c += x
            if a>=x:
                a -= x
            if b>=x:
                b -= x

    print(c)


def B():
    x, y, z= map(int, input().split())
    ans = -1
    if x>0:
        if y<0:
            ans = abs(x)
        elif x<y:
            ans = x
        elif z<0:
            ans = abs(z)*2 +x
        elif z>0 and z<y:
            ans = x

    elif x<0:
        if y>0:
            ans = abs(x)
        elif y<x:
            ans = abs(x)
        elif z<0 and y<z:
            ans = abs(x)
        elif z>0:
            ans = 2*z+abs(x)
    print(ans)


"""
深さ優先探索（DFS）
DFSは木構造と相性が良い、らしい
pypy3だとTLE, python3だと間に合ってAC
"""
def C():
    #再帰回数の上限を変更
    import sys
    sys.setrecursionlimit(1000000)

    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    g = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    """
    v: 現在のノード
    p: 親ノード (1つ前のノード)
    """
    def dfs(v, p):
        if v==x:
            ans.append(v)
            return True
        for u in g[v]:
            if u==p:
                continue
            if dfs(u, v):
                ans.append(v)
                return True
        return False

    ans = []
    dfs(y, -1)
    print(" ".join([str(a+1) for a in ans]))


"""
BFS(幅優先探索)でもDFS(深さ優先探索)でも解けるらしい
https://qiita.com/MoroeTachibana-oh/items/a340ede2a70815e60ad8#1-4-c%E5%95%8F%E9%A1%8C-simple-path
"""
"""
dfsのパターン
xからyまでの道のりを探索した後、yからxに戻って道順を作る
pypy3だとTLE, python3だと間に合ってAC
"""
def C_ans_dfs():
    #再帰回数の上限を変更
    import sys
    sys.setrecursionlimit(10**9)

    n, x, y = map(int, input().split())
    x -= 1; y -= 1

    g = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)

    rec = {}#nxt:now
    def dfs(now, prev):
        for nxt in g[now]:
            if nxt==prev:
                continue
            #キーにnxtが存在しない時、値nowを格納
            rec.setdefault(nxt, now)
            dfs(nxt, now)
        return

    dfs(x, None)
    ans = []
    now = y
    while now!=x:
        ans.append(now+1)
        now = rec[now]
    ans.append(now+1)
    print(*reversed(ans), sep=" ")


"""
貪欲法では解けないようになっている問題らしい
"""
def D_WA():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    takahashi = 0
    aoki = 0

    from bisect import bisect_left
    i = 0
    while n>=a[0]:
        less_n = bisect_left(a, n)
        if less_n<k and a[less_n]==n:
            less_n = less_n
        else:
            less_n -= 1
        
        if i%2==0:
            if less_n>0:
                takahashi += a[less_n]
                n -= a[less_n]
            else:
                takahashi += a[0]
                n -= a[0]
        else:
            if less_n>0:
                aoki += a[less_n]
                n -= a[less_n]
            else:
                aoki += a[0]
                n -= a[0]
        i += 1
    print(takahashi)

