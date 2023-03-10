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

# def A():



def B():
    import numpy as np
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())

    bom_map = np.zeros((H, W)).astype("int")
    # bom map作成
    for h in range(H):
        for w in range(W):
            if S[h][w]=="#":
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if h+y>=0 and h+y<H and w+x>=0 and w+x<W:
                            bom_map[h+y, x+w] += 1
    # 表示用作成
    for h in range(H):
        buf = ""
        for w in range(W):
            if S[h][w]=="#":
                buf += "#"
            else:
                buf += str(bom_map[h, w])
        print(buf)


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

def C_ans():
    n, m = map(int, input().split())
    a = [None]*m
    b = [None]*m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1

    ans = 0
    for i in range(m): #切断するエッジ
        uf = UnionFind_simple(n)
        for j in range(m): #他のエッジは連結
            if i!=j:
                uf.unite(a[j], b[j])
        #親の数をカウント
        cnt_root = 0
        for i in range(n):
            if uf.par[i]==-1:
                cnt_root += 1
        #切断したことで親の数が増えてたら橋
        if cnt_root>1:
            ans += 1
    print(ans)


# def D():

