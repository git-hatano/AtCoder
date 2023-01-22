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
    if b-a>0:
        print(b-a+1)
    else:
        print(0)


def B():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    price = 0
    for i in range(n):
        if (i+1)%2==0:
            price += (a[i]-1)
        else:
            price += a[i]

    if x>=price:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def C_WA():
    n = int(input())
    c = list(map(int, input().split()))
    mod = (10**9)+7
    ans = 1
    for i in range(n):
        ans = ans * (c[i]-i)
    ans %= mod
    print(ans)

def C_ans():
    n = int(input())
    c = list(map(int, input().split()))
    mod = (10**9)+7
    #昇順に並び替える必要
    c = sorted(c)

    ans = 1
    for i in range(n):
        #掛け算する際にmodを使う必要
        ans = ans * max(0, c[i]-i) % mod 
    print(ans)


"""
BFSを思いついて距離の考え方は良かったが、
距離の数え上げと先に計算しておくのが上手く実装できなかった
"""
def D_TLE_WA():
    from collections import defaultdict, deque
    n, q = map(int, input().split())
    g = defaultdict(list)
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        #BFS
        que = deque()
        que.append((c, 0))
        s = {c}
        while que:
            v, dist = que.popleft()
            dist += 1
            for j in g[v]:
                if j==d:
                    break
                if not j in s:
                    que.append((j, dist))
                    s.add(j)
        if dist%2==0:
            print("Town")
        else:
            print("Road")


"""
BFSで二部グラフ
予め二部グラフを作ることでTLEにならない
"""
def D_ans():
    from collections import defaultdict, deque
    n, q = map(int, input().split())
    g = defaultdict(list)
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    #各頂点を色塗り
    #頂点0から偶数の距離だと赤、奇数だと青みたいなイメージ
    color = [-1]*n
    que = deque()
    color[0] = 0
    que.append(0)
    while que:
        v = que.popleft()
        for i in g[v]:
            if color[i]==-1: #色が塗られてなかったら今の頂点と別の色で塗る
                color[i] = 1 - color[v]
                que.append(i)

    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if color[c]==color[d]:
            print("Town")
        else:
            print("Road")

