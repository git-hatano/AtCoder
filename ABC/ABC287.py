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
    n = int(input())
    cnt = 0
    for i in range(n):
        s = input() 
        if s=="For":
            cnt += 1
    if cnt > n//2:
        print("Yes")
    else:
        print("No")


def B():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if s[i][-3:]==t[j]:
                cnt += 1
                break
        if cnt>0:
            ans += 1
    print(ans)


"""
パスグラフかどうかを判定
単純無向グラフ : 自己ループや多重辺を含まず、辺に向きの無いグラフ
UnionFindの方が簡単
"""
def C():
    import sys
    sys.setrecursionlimit(10**9)
    from collections import defaultdict
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    ans = [True]*n
    def dfs(cur, pre):
        if cur in s:
            ans[cur] = False
            return
        if len(s)==n:
            return
        s.add(cur)
        for nex in g[cur]:
            if nex!=pre:
                dfs(nex, cur)

    cur = 0
    pre = -1
    s = set()
    dfs(cur, pre)
    if len(s)!=n:
        ans[cur] = False

    if False in set(ans):
        print("No")
    else:
        print("Yes")


"""
答えはあっていそう
2重ループの取り方が分からん
"""
def D_TLE():
    s = list(input())
    t = input()

    for x in range(len(t)+1):
        s_tmp = s.copy()
        del s_tmp[x]
        s_tmp = "".join(s_tmp)
        
        ans = True
        for i in range(len(t)):
            if s_tmp[i]=="?" or t[i]=="?" or s_tmp[i]==t[i]:
                continue
            ans = False
            break
        print("Yes" if ans else "No")


"""
実装は簡単だけど、なんでこの確認で一致しているかを判定できるのか分からない
"""
def D_ans():
    s = list(input())
    t = list(input())
    m = len(t)

    ans = [True]*(m+1)
    for ri in range(2): #i=0:先頭から一致するか, i=1:後から一致するか
        ok = True
        for i in range(m):
            if s[i]!=t[i] and s[i]!="?" and t[i]!="?":
                ok = False
            if not ok:
                ans[i+1] = False
        
        #i=0:反転, i=1:元に戻す
        s.reverse()
        t.reverse()
        ans.reverse()

    for i in range(m+1):
        if ans[i]:
            print("Yes")
        else:
            print("No")
