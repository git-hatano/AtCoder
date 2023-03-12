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
    n = len(s)
    ans = []
    for i in range(n//2):
        ans.append(s[2*i+1])
        ans.append(s[2*i])
    if len(ans)<n:
        ans.append(s[-1])
    ans = "".join([str(x) for x in ans])
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in range(1, n+1):
        if i not in s:
            s.add(a[i-1])

    ans = []
    for i in range(1, n+1):
        if i not in s:
            ans.append(i)
    print(len(ans))
    ans = " ".join([str(x) for x in ans])
    print(ans)


def C():
    from itertools import product
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 0 
    for bits in product([0, 1], repeat=h-1+w-1):
        cur = [0, 0]
        root = []
        root.append(a[cur[0]][cur[1]])
        ok = True
        for b in bits:
            if b==0 and cur[0]+1<h: #0なら下
                cur[0] += 1
            elif b==1 and cur[1]+1<w: #1なら右
                cur[1] += 1
            else:
                ok = False
                break
            root.append(a[cur[0]][cur[1]])
        
        if ok and cur[0]==h-1 and cur[1]==w-1:
            if len(root)==len(set(root)):
                ans += 1
    print(ans)


def C_ans():
    import sys
    sys.setrecursionlimit(10**9)
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    s = set() #今の経路上の値を記録
    ans = [0]

    def dfs(i, j, s):
        if a[i][j] in s:#重複していたらreturn
            return
        if i==h-1 and j==w-1:#右下についたらreturn
            ans[0] += 1
            return
        s.add(a[i][j])
        if j+1<w: #右にいく
            dfs(i, j+1, s)
        if i+1<h: #下にいく
            dfs(i+1, j, s)
        s.remove(a[i][j])

    dfs(0, 0, s)
    print(ans[0])


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
    x = 0 #サイクルの個数
    for i in range(m):
        s = list(input().split())
        a = int(s[0])-1
        b = s[1]
        c = int(s[2])-1
        d = s[3]
        if uf.same(a, c):
            x += 1
        else:
            uf.unite(a, c)
    y = n-m #サイクルでないものの個数 
    print(x, y)
