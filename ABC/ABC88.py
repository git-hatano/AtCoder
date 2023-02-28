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
    c = [list(map(int, input().split())) for _ in range(3)]
    ans = True
    if c[0][0]-c[0][1] != c[1][0]-c[1][1]:
        ans = False
    if c[0][1]-c[0][2] != c[1][1]-c[1][2]:
        ans = False
    if c[1][0]-c[1][1] != c[2][0]-c[2][1]:
        ans = False
    if c[1][1]-c[1][2] != c[2][1]-c[2][2]:
        ans = False
    print("Yes" if ans else "No")


"""
考え方は合ってる
最短経路がうまく作れてなさそう
"""
def D_WA():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    #goalまでの最短距離
    inf = 10**9
    a = [[inf]*(w) for i in range(h)]
    a[0][0] = 0
    vec = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(h):
        for j in range(w):
            if s[i][j]==".":
                for v in vec:
                    if 0<=i+v[0]<h and 0<=j+v[1]<w and s[i+v[0]][j+v[1]]==".":
                        a[i+v[0]][j+v[1]] = min(a[i+v[0]][j+v[1]], a[i][j]+1)
    # 黒マスの数
    black = 0
    for i in range(h):
        for j in range(w):
            if s[i][j]=="#":
                black += 1
    #goalできない条件
    if a[h-1][w-1]==inf:
        ans = -1
    else:
        ans = h*w - black - (a[h-1][w-1]+1)
    print(ans)


"""
最短経路は幅優先探索
"""
def D_ans():
    from collections import deque
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    que = deque([])#幅優先探索用
    vec = [[-1, 0], [1, 0], [0, -1], [0, 1]] #移動できる方向

    dp = [[0]*(w) for i in range(h)] #距離を記録
    visit = [[0]*(w) for i in range(h)] #訪れたかを記録
    visit[0][0] = 1
    que.append([0, 0])

    #幅優先探索: 最短距離を探索
    while que:
        i, j = que.popleft()
        if i==h-1 and j==w-1:
            break
        for v in vec:
            ii = i+v[0]
            jj = j+v[1]
            if 0<=ii<h and 0<=jj<w and s[ii][jj]=="." and visit[ii][jj]==0:
                visit[ii][jj] = 1
                dp[ii][jj] = dp[i][j] +1
                que.append([ii, jj])

    if visit[h-1][w-1]==0:
        ans = -1
    else:
        # 黒マスの数
        black = 0
        for i in range(h):
            for j in range(w):
                if s[i][j]=="#":
                    black += 1
        ans = h*w - black - (dp[h-1][w-1]+1)
    print(ans)
