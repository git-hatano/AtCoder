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
    s = [input() for _ in range(n)]
    s.reverse()
    for i in range(n):
        print(s[i])


def B():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = 0
        for j in range(n):
            if a[j]%2==1:
                ans += 1
        print(ans)


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

    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        uf.unite(u, v)

    ans = 0
    for i in range(n):
        if uf.par[i]==-1:
            ans += 1
    print(ans)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

"""
クエリ数が減らせないので、高速に素因数分解しないけない
or メモしておく？
"""
def D():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = factorization(n)
        a.sort(key=lambda x: -x[1])
        print(f"{a[0][0]} {a[1][0]}")


t = int(input())
for i in range(t):
    n = int(input())

