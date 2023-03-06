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

def A():
    s = input()
    print(s.upper())


def B():
    from collections import defaultdict
    n, q = map(int, input().split())
    d = defaultdict(int)
    for i in range(q):
        t, x = input().split()
        t = int(t)
        if t==1:
            d[x] += 1
        elif t==2:
            d[x] += 2
        else:
            if d[x]>=2:
                print("Yes")
            else:
                print("No")


"""
簡単な数学的な考察問題
苦手
"""
def C_ans():
    import math
    n = int(input())
    ans = 0
    for i in range(1, n):
        x = i #ここを変数で置けなかった
        y = n-x
        cnt_x = 0
        cnt_y = 0
        for j in range(1, int(math.sqrt(x))+1):
            if x%j==0:
                cnt_x += 1
                if x!=j*j:
                    cnt_x += 1
        for j in range(1, int(math.sqrt(y))+1):
            if y%j==0:
                cnt_y += 1
                if y!=j*j:
                    cnt_y += 1
        ans += cnt_x*cnt_y
    print(ans)


"""
無向グラフの連結性: UnionFind
"""
class UnionFind_simple:
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

def D_ans():
    n, m = map(int, input().split())
    uf = UnionFind_simple(n)
    edges = [0]*n
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf.unite(a, b)
        edges[a] += 1
        edges[b] += 1

    #連結成分ごとに辺数を集計
    edges_sum = [0]*n
    for i in range(n):
        root = uf.root(i)
        edges_sum[root] += edges[i]

    #親に含まれる頂点数と辺数が同じかを確認
    ans = 0
    ans = True
    for i in range(n):
        if uf.par[i]==-1:
            if uf.siz[i]*2!=edges_sum[i]:
                ans = False
    print("Yes" if ans else "No")
