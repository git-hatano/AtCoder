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
    k = int(input())
    s = ""
    for i in range(k):
        s += chr(ord("A")+i)
    print(s)


def B():
    from itertools import combinations
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(list(input()))
    ans = 0
    for c in combinations(range(n), 2):
        flag = True
        for j in range(m):
            if s[c[0]][j]=="x" and s[c[1]][j]=="x":
                flag = False
        if flag:
            ans += 1
    print(ans)


def C():
    n = int(input())
    s = input()
    flag = False
    pos = []
    start = -1
    stop = -1
    for i in range(n):
        if s[i]=='"' and flag==False:
            start = i
            flag = True
        elif s[i]=='"' and flag==True:
            stop = i
            flag = False
            pos.append([start, stop])
    if start>=0 and stop<0:
        pos.append([start, n-1])

    p = 0
    ans = []
    for i in range(n):
        if len(pos)>0:
            if not pos[p][0]<=i<=pos[p][1] and s[i]==",":
                ans.append(".")
            else:
                ans.append(s[i])
            if i==pos[p][1] and p<len(pos)-1:
                p += 1
        else:
            if s[i]==",":
                ans.append(".")
            else:
                ans.append(s[i])

    ans = "".join([str(x) for x in ans])
    print(ans)


def C_ans():
    n = int(input())
    s = list(input())
    lef_even = True
    for i in range(n):
        if lef_even and s[i]==",":
            s[i] = "."
        if s[i]=='"':
            lef_even = not lef_even
    print("".join(s))


"""
即興で二部グラフを理解して使えたのはOK
サンプルが全て通ってしまったので詰み
"""
def D_WA():
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10**7)
    n, m = map(int, input().split())
    g = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)

    #頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
    def dfs(v,color):
        #今いる点を着色
        colors[v] = color
        #今の頂点から行けるところをチェック
        for to in g[v]:
            #同じ色が隣接してしまったらFalse
            if colors[to] == color:
                return False
            #未着色の頂点があったら反転した色を指定し、再帰的に調べる
            if colors[to] == 0 and not dfs(to, -color):
                return False
        #調べ終わったら矛盾がないのでTrue
        return True

    #2部グラフならTrue, そうでなければFalse
    def is_bipartite():
        return dfs(0,1) # 頂点0を黒(1)で塗ってDFS開始

    #n個の頂点の色を初期化。0:未着色、1:黒、-1:白
    colors = [0 for i in range(n)]
    ans = 0
    if is_bipartite():
        for key in g:
            for i in range(key, n):
                if i not in g[key]:
                    if colors[i]!=colors[key]:
                        ans += 1
    print(ans)


"""
2部グラフの応用
"""
def D_ans():
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10**9)

    def c2(n):
        return n*(n-1)//2

    n, m = map(int, input().split())
    #連結リストで格納
    g = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    #各頂点の色を格納
    c = [-1]*n

    def dfs(v, nc=0):#ncは今の色
        if c[v]!=-1:
            #もし塗られていたら今塗ろうとしている色と一致するか
            return c[v]==nc
        c[v] = nc
        cvs[nc] += 1
        for u in g[v]:
            #子を親と反対の色で塗って矛盾がないかを確認
            if not dfs(u, nc^1):
                return False    
        return True

    ans = c2(n)-m #全ての辺の選び方 - 既にある辺の数
    for i in range(n):
        #既に色が入っていたら何もしない
        if c[i]!=-1:
            continue
        #ある連結成分に白と黒がそれぞれ何個あるかを管理
        cvs = [0]*2
        if not dfs(i):
            print(0)
            sys.exit()
        #繋いじゃいけない辺（同じ連結で同じ色のペア数）を引く
        for s in cvs:
            ans -= c2(s)
    print(ans)
