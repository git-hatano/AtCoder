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
    a = int(input())
    s = input() 
    if a>=3200:
        print(s)
    else:
        print("red")


def B():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += 1/a[i]
    ans = 1/s
    print(ans)


def C():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    sums = []
    for i in range(n):
        if i==0:
            sums.append(v[i])
        else:
            sums.append((sums[-1]+v[i])/2)
    print(sums[-1])


"""
どうしたら効率良く各頂点にスコアを与えられるか
BFSで予め親子関係を作っておく?
Unionfined?
Segment木?
わかんね
"""
def D_WA():
    from collections import defaultdict, deque
    n, q = map(int, input().split())
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    score = [0]*n
    par = [-1]*n
    s = set([0])
    que = deque([0])
    while len(que)>0:
        cur = que.popleft()
        for v in g[cur]:
            if v not in s:
                par[v] = cur
                que.append(v)
                s.add(v)

    print(" ".join([str(x) for x in score]))



"""
dfsで根から順番にスコアを与えていく
木上でimos法をすると言うらしい
"""
def D_ans():
    import sys
    sys.setrecursionlimit(10**9)
    from collections import defaultdict
    n, q = map(int, input().split())
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    val = [0]*n
    def dfs(cur, par=-1):
        for to in g[cur]:
            if par!=to:
                val[to] += val[cur]
                dfs(to, cur)
    #予めスコアの初期値を格納
    for i in range(q):
        p, x = map(int, input().split())
        p -= 1
        val[p] += x
    #DFSで根から子にスコアを付与していく
    dfs(0)

    print(" ".join([str(x) for x in val]))
