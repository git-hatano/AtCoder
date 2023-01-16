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
    d, t, s = map(int, input().split())
    ans = (t >= d/s)
    print("Yes" if ans else "No")


def B():
    s = input()
    t = input() 
    len_s = len(s)
    len_t = len(t)

    same = 0
    for i in range(len_s - len_t +1):
        tmp_same = 0
        for j in range(len_t):
            if t[j] == s[i+j]:
                tmp_same += 1
        same = max(same, tmp_same)

    ans = len_t - same
    print(ans)


"""
累積和
"""
def C():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] + list(accumulate(a))
    mod = 10**9 +7

    ans = 0
    for i in range(n-1):
        ans += (a[i] * (s[-1] - s[i+1]))%mod
    print(ans%mod)


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

def D():
    n, m = map(int, input().split())
    uf = UnionFind_simple(n)
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1 
        uf.unite(a, b)

    ans = max(uf.siz)
    print(ans)

