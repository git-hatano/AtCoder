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
    a = format(a, '08b')
    b = format(b, '08b')

    c = ""
    n = 8
    for i in range(n):
        if a[i]=="1" and b[i]=="1":
            c += "0"
        elif a[i]=="1" and b[i]=="0":
            c += "1"
        elif a[i]=="0" and b[i]=="1":
            c += "1"
        elif a[i]=="0" and b[i]=="0":
            c += "0"
    print(int(c, 2))


def B():
    n = int(input())
    a = list(map(int, input().split()))

    x = []
    for i in range(n):
        x.append([a[i], i])

    x = sorted(x)
    print(x[n-2][1]+1)


def C():
    h, w, n = map(int, input().split())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ab.append([a,b])

    ab_s = sorted(ab)
    row = {}
    cnt = 0
    for i in range(n):
        if ab_s[i][0] not in row:
            row[ab_s[i][0]] = cnt
            cnt += 1

    ab_s = sorted(ab, key=lambda x: x[1])
    col = {}
    cnt = 0
    for i in range(n):
        if ab_s[i][1] not in col:
            col[ab_s[i][1]] = cnt
            cnt += 1

    for i in range(n):
        c = row[ab[i][0]]+1
        d = col[ab[i][1]]+1
        print(f"{c} {d}")


"""
DFSに気づいたのはよかった
return が要らなかった
"""
def D_WA():
    import sys
    from collections import defaultdict
    n = int(input())
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    #小さい順に
    for e in g:
        g[e].sort()

    visit = set()
    path = []
    def dfs(cur, pre):
        if cur==0 and len(visit)==n:
            path.append(cur)
            ans = " ".join([ str(x+1) for x in path ])
            print(ans)
            sys.exit()
        if cur!=0 and cur in visit:
            return
        visit.add(cur)
        path.append(cur)
        for nex in g[cur]:
            if nex!=pre:
                dfs(nex, cur)

    cur = 0
    pre = -1
    dfs(cur, pre)


"""
DFSわかんねえ
"""
def D_ans():
    import sys
    sys.setrecursionlimit(300000)
    from collections import defaultdict
    n = int(input())
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    #小さい順に
    for e in g:
        g[e].sort()

    path = []
    def dfs(cur, pre): #returnを無駄に書いて合わなくなっていた
        path.append(cur)
        for nex in g[cur]:
            if nex!=pre:
                dfs(nex, cur)
                path.append(cur)

    cur = 0
    pre = -1
    dfs(cur, pre)
    print(" ".join([str(x+1) for x in path]))

