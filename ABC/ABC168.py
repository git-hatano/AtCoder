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
    n = input() 
    if n[-1] == "3":
        print("bon")
    elif n[-1] in ["0", "1", "6", "8"]:
        print("pon")
    else:
        print("hon")


def B():
    k = int(input())
    s = input() 
    if len(s) <= k:
        print(s)
    else:
        print(s[:k]+"...")


def C():
    import numpy as np
    import math
    # deg=Trueならば度数単位で角度を指定
    def rotation(u, t, deg=True):
        if deg:
            t = np.deg2rad(t)
        # 回転行列
        R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t),  np.cos(t)]])
        return  np.dot(R, u)

    a, b, h, m = map(int, input().split())
    h %= 12
    m %= 60
    vec_a = np.array([0, a])
    vec_b = np.array([0, b])

    vec_a = rotation(vec_a, -0.5*(60*h+m))
    vec_b = rotation(vec_b, -6*m)

    ans = math.sqrt((vec_a[0]-vec_b[0])**2 + (vec_a[1]-vec_b[1])**2)
    print(ans)


"""BFSの典型問題"""
def D():
    from collections import defaultdict, deque
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    cur = 0
    que = deque([])
    que.append(cur)
    inf = 10**9
    dist = [inf]*n
    dist[cur] = 0
    par = [None]*n
    par[cur] = -1

    while len(que)>0:
        cur = que.popleft()
        for v in g[cur]:
            if dist[v]==inf:
                dist[v] = dist[cur]+1
                par[v] = cur
                que.append(v)

    ok = True
    for i in range(1, n):
        if par[i]==-1:
            ok = False
    if ok:
        print("Yes")
        for i in range(1, n):
            print(par[i]+1)
    else:
        print("No")
