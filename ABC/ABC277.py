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
    n, x = map(int, input().split())
    p = list(map(int, input().split()))

    for i in range(n):
        if p[i]==x:
            print(i+1)
            break


def B():
    n = int(input())
    ans = True
    p = []
    for i in range(n):
        s = input()
        p.append(s)
        if s[0] not in ["H", "D", "C", "S"]:
            ans = False
        if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            ans = False

    if len(list(set(p)))!=n:
        ans = False

    print("Yes" if ans else "No")


"""
DFS
TLEが2つ残ってしまう
"""
def C_TLE():
    #再帰回数の上限を変更
    import sys
    sys.setrecursionlimit(1000000)
    from collections import defaultdict
    n = int(input())

    d = defaultdict(list)
    for i in range(n):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    def dfs(cur_f, pre_f):
        if cur_f in root[pre_f]:
            return
        floor.add(cur_f)
        for next_f in d[cur_f]:
            root[pre_f].add(cur_f)
            dfs(next_f, cur_f)

    cur = 1
    root = defaultdict(set)
    floor = set()
    dfs(cur, -1)

    ans = max(floor)
    print(ans)


"""
解説はBFS？
データの持ち方とかはあってるのになぁ
"""
def C_ans():
    from collections import defaultdict, deque
    n = int(input())

    graph = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    que = deque()
    que.append(1)
    s = {1}

    while que:
        v = que.popleft()
        for i in graph[v]:
            if not i in s:
                que.append(i)
                s.add(i)

    print(max(s))


"""
初期値はどう決める？
被っているやつは捨てて良い？
"""
def D():
    import sys
    from collections import Counter
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    sum_a = sum(a)
    cnt_a = Counter(a)
    cnt_a = sorted(cnt_a.items(), key=lambda x: x[0])

    k = len(cnt_a)
    if k==m:
        print(0)
        sys.exit()

    p = 0
    for i in range(k):
        if cnt_a[(i+1)%k][0] != (cnt_a[i][0]+1)%m:
            p = i
            break

    s = [0]*200005
    for i in range(k):
        j = (p-i+k)%k
        s[j] = sum_a
        if cnt_a[(j+1)%k][0] == (cnt_a[j][0]+1)%m:
            s[j] = s[(j+1)%k]
        s[j] -= cnt_a[j][0] * cnt_a[j][1]

    ans = sum_a
    for i in range(k):
        ans = min(ans, s[i])
    print(ans)
