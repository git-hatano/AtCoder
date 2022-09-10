'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]

# 2次元配列
dp = [[0]*(K) for i in range(N)]
'''

def A():
    n = int(input())
    mod = n%4

    if mod == 0:
        print(n+2)
    if mod == 1:
        print(n+1)
    if mod == 2:
        print(n)
    if mod == 3:
        print(n+3)



# def B():
n, m = map(int, input().split())
a = [[0]*(n) for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u][v] = 1
    a[v][u] = 1
# グラフを作るとことまではOK、三角形の探し方が分からん

# 答え：全探索、マジか
# 対角線的に対称だから、探索範囲を狭めて行ってもいい
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i][j] and a[j][k] and a[k][i]:
                ans += 1
print(ans)



def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    # TLEにするところまではOK、TLEの回避法が分からん
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if i!=j and min(a[i], a[j])==i+1 and max(a[i], a[j])==j+1:
                cnt += 1
    print(cnt)


def C():
    n = int(input())
    a = list(map(int, input().split()))

    # a[i]を0始まりにする
    for i in range(n):
        a[i] -= 1

    same = 0
    for i in range(n):
        if i == a[i]:
            same += 1
    ans = same * (same-1) //2

    for i in range(n):
        if i < a[i] and a[a[i]]==i:
            ans += 1

    print(ans)


# def D():



