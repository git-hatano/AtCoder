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
if ans:
    print("Yes")
else:
    print("No")
'''

import turtle


def A():
    s = input() 
    a = int(s.split("x")[0])
    b = int(s.split("x")[1])
    print(a*b)


def B():
    s = list(input())
    t = list(input())

    diffs = []
    ans = True
    for i in range(len(s)):
        s_i = ord(s[i]) -ord("a")
        t_i = ord(t[i]) -ord("a")
        
        diff = (t_i - s_i)%26
        diffs.append(diff)

        if i>0 and diffs[i]!=diffs[i-1]:
            ans = False
            break

    if ans:
        print("Yes")
    else:
        print("No")

        
def C():
    n, m = map(int, input().split())

    ga = [[0]*n for i in range(n)]
    gb = [[0]*n for i in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ga[a][b] = 1
        ga[b][a] = 1

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        gb[a][b] = 1
        gb[b][a] = 1

    """
    青木のグラフ構造はそのままで、ボールの番号を全通り置き換えて、
    高橋のグラフ構造に一致するかを見ている

    ボールの置き換え方をpで作成して、
    元のインデックスi,jを、p[i], p[j]で置き換えている
    """
    import itertools
    ans = False
    for p in itertools.permutations(range(n)):
        ok = True
        # print(p)

        for i in range(n):
            for j in range(n):
                # print(i, j)
                # print(p[i], p[j])
                if ga[i][j] != gb[p[i]][p[j]]:
                    ok = False
        if ok:
            ans = True

    print("Yes" if ans else "No")



"""
深さ優先探索
"""
def D_TLE():
    h, w = map(int, input().split())

    c = []
    for i in range(h):
        c.append(list(input()))

    step_map = [[0]*w for i in range(h)]

    def dfs(i, j):
        # ベースケース
        if i==h or j==w:
            return False

        if i+1<h and c[i+1][j]==".":
            step_map[i+1][j] = step_map[i][j] +1
            dfs(i+1, j)
        
        if j+1<w and c[i][j+1]==".":
            step_map[i][j+1] = step_map[i][j] +1
            dfs(i, j+1)

    dfs(0, 0)

    max_step = 0
    for i in range(h):
        for j in range(w):
            max_step = max(max_step, step_map[i][j])
    print(max_step+1)


"""
深さ優先探索＋メモ化もどき
TLEは消えたが、WAが2つでてしまった
"""
def D_WA():
    h, w = map(int, input().split())

    c = []
    for i in range(h):
        c.append(list(input()))

    step_map = [[0]*w for i in range(h)]

    def dfs(i, j):
        # ベースケース
        if i==h or j==w:
            return False


        if i+1<h and c[i+1][j]==".":
            #memo化もどき
            if step_map[i+1][j]>0:
                return step_map[i+1][j]

            step_map[i+1][j] = step_map[i][j] +1
            dfs(i+1, j)
        
        if j+1<w and c[i][j+1]==".":
            #memo化もどき
            if step_map[i][j+1]>0:
                return step_map[i][j+1]

            step_map[i][j+1] = step_map[i][j] +1
            dfs(i, j+1)

    dfs(0, 0)

    max_step = 0
    for i in range(h):
        for j in range(w):
            max_step = max(max_step, step_map[i][j])
    print(max_step+1)


"""
dp 動的計画法
再帰関数での探索は重たい？
dpの方が記述がすっきりしていて良い感じに見える
"""
def D():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(list(input()))

    dp = [[0]*w for i in range(h)]

    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if s[i][j]=="#":
                continue

            dp[i][j] = 1
            if i+1 < h:
                dp[i][j] = max(dp[i][j], dp[i+1][j]+1)
            
            if j+1 < w:
                dp[i][j] = max(dp[i][j], dp[i][j+1]+1)

    print(dp[0][0])


