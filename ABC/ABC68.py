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



# def B():



def C():
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
    #BFS
    que = deque()
    que.append(cur)
    d = [10**9]*n #距離
    d[cur] = 0
    s = set() #訪れた頂点
    while que:
        v = que.popleft()
        s.add(v)
        for i in g[v]:
            if i not in s:
                d[i] = min(d[i], d[v]+1)
                que.append(i)
    if d[n-1]==2:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

# def D():

