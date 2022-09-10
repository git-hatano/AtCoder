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
print("Yes" if ans else "No")
'''

def A():
    d = int(input())
    print(d/100)


def B():
    n = int(input())

    from collections import defaultdict
    d = defaultdict(int)

    for i in range(n):
        name = input()
        d[name] += 1

    print(max(d, key=d.get))


"""
全探索
問題文の計算量から無理なのは分かってた
"""
def C_TLE():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)

    for j in range(q):
        x = int(input())
        ans = 0
        
        for i in range(n):
            if a[i] >= x:
                ans += 1
        
        print(ans)


"""
二分探索
"""
def C():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    from bisect import bisect_left

    for j in range(q):
        x = int(input())
        less_than_x_count = bisect_left(a, x)
        print(n - less_than_x_count)
    

def D_WA():
    n, m = map(int, input().split())

    #隣の数字管理用
    from collections import defaultdict
    d = defaultdict(int)#0で初期化

    for i in range(m):
        a, b = map(int, input().split())
        d[a] += 1
        d[b] += 1

    #隣り合うものが3以上ないはず
    ans = True
    for key in d:
        if d[key]>2:
            ans = False
            break

    print("Yes" if ans else "No")


"""
UnionFind??????
"""
def D():
    n, m = map(int, input().split())

    from utils import unionFind
    uf = unionFind.UnionFind(n)
    c = [0]*n #人が条件で出てくる回数をカウント

    ans = True
    for _ in range(m):
        a,b = map(int, input().split())
        a,b = a-1, b-1
        
        if uf.is_same(a, b):#閉ループがないか判定
            ans = False
        
        uf.unite(a, b)
        c[a] += 1
        c[b] += 1

    for i in range(n):
        if c[i]>=3:
            ans = False
            
    print("Yes" if ans else "No")

