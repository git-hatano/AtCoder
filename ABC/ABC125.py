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
    a, b, t = map(int, input().split())
    n = int((t+0.5)//a)
    print(b*n)


def B():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(v[i] - c[i])

    ans = 0
    for i in range(2**n):
        s = 0
        for j in range(n):
            wari = (2 ** j)
            if (i // wari) % 2 == 1:
                s += d[j]
        ans = max(ans, s)
    print(ans)


"""
素因数分解をして因数が一番少ないものを一番大きなものに置き換え
最大公約数が19などの素数の場合にWAになってしまう
"""
def C_WA_TLE():
    import math
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

    def factorization_1d(n):
        facts = factorization(n)
        nums = []
        for f in facts:
            for i in range(f[1]):
                nums.append(f[0])
        return nums

    n = int(input())
    a = list(map(int, input().split()))
    l = []
    for i in range(n):
        nums = factorization_1d(a[i])
        l.append([len(nums), i])
    l.sort()
    a[l[0][1]] = a[l[-1][1]]
    x = a[0]
    for i in range(1, n):
        x = math.gcd(x, a[i])
    print(x)


"""
O(n**2) でTLE
選ばない数字を一意に決める方法はないか（1つ目のループをなくせないか）
予めgcdを計算しておいて再利用できないか（2つ目のループをなくせないか）
    →回答例はここをセグメント木で管理した
"""
def C_TLE():
    import math
    n = int(input())
    a = list(map(int, input().split()))

    #どれか1つを都合の良い数字で置き換える＝どれか1つの数字を選ばない
    ans = 0
    for i in range(n):#選ばない数字を決める
        if i==0:
            g = a[1]
        else:
            g = a[0]
        for j in range(n):#その時のgcdを求める
            if i!=j:
                g = math.gcd(g, a[j])
        ans = max(ans, g)
    print(ans)


import math
class segtree:
    # 要素 dat の初期化を行う（最初は全部ゼロ）
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [ 0 ] * (self.size * 2)

    # クエリ 1 に対する処理
    def update(self, pos, x):
        pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = math.gcd(self.dat[pos * 2], self.dat[pos * 2 + 1]) # 8.8 節から変更した部分

    # クエリ 2 に対する処理
    # u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return 0 # 8.8 節から変更した部分
        if l <= a and b <= r:
            return self.dat[u]
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return math.gcd(answerl, answerr) # 8.8 節から変更した部分


def C_ans():
    n = int(input())
    a = list(map(int, input().split()))
    #セグメント木を使ってある区間のgcdを保持しておく
    seg = segtree(n)
    for i in range(n):
        seg.update(i, a[i])

    #どれか1つを都合の良い数字で置き換える＝どれか1つの数字を選ばない
    ans = 0
    for i in range(n):#選ばない数字を決める
        g = 0
        #区間[0, i)のgcd
        g = math.gcd(g, seg.query(0, i, 0, seg.size, 1))
        #区間[i+1, n)のgcd
        g = math.gcd(g, seg.query(i+1, n, 0, seg.size, 1))
        ans = max(ans, g)
    print(ans)



