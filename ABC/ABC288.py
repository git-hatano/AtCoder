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
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(a+b)


def B():
    a, b = map(int, input().split())
    s = []
    for i in range(a):
        s.append(input())
    t = s[:b]
    t.sort()
    for i in range(b):
        print(t[i])


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

def C():
    n, m = map(int, input().split())
    uf = UnionFind_simple(n)
    ans = 0
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans += 1
        else:
            uf.unite(a, b)
    print(ans)


def D_TLE_plot():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q): #O(2 * 10**5)
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        b = a[l:r+1]
        w = r-l+1
        for i in range(1, w): ##TLE-point O(2 * 10**5)
            c =  a[l+i-1] - a[l+i]
            for j in range(k):
                b[l+i+j] += c


"""
前計算が必要そう: どんな？
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]
for i in range(n-1):
    b.append(a[i]-a[i+1])

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

