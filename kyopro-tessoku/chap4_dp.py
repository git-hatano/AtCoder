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

def A16():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+a[i-1]
        else:
            dp[i] = min(dp[i-1]+a[i-1], dp[i-2]+b[i-2])
    print(dp[n-1])


def B16():
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+abs(h[i]-h[i-1])
        else:
            dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
    print(dp[n-1])


def A17():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #ゴールまでの最短時間
    dp = [None]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+a[i-1]
        else:
            dp[i] = min(dp[i-1]+a[i-1], dp[i-2]+b[i-2])

    #ゴールからの最短経路
    pos = []
    i = n-1
    pos.append(i)
    while True:
        if dp[i] == dp[i-1]+a[i-1]:
            i -= 1
        elif dp[i] == dp[i-2]+b[i-2]:
            i -= 2
        pos.append(i)

        if i==0:
            break

    ans = " ".join([str(x+1) for x in pos[::-1]])
    print(len(pos))
    print(ans)


def B17():
    n = int(input())
    h = list(map(int, input().split()))

    #ゴールまでの最小コスト
    dp = [None]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+abs(h[i]-h[i-1])
        else:
            dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))

    #最小コストである経路
    pos = []
    i = n-1
    pos.append(i)
    while True:
        if i==0:
            break
        
        if dp[i] == dp[i-1]+abs(h[i]-h[i-1]):
            i -= 1
        else:
            i -= 2
        pos.append(i)

    ans = " ".join([str(x+1) for x in pos[::-1]])
    print(len(pos))
    print(ans)


"""
部分和の問題

dp[i][j]
カード1~iまでの中から何枚かを選び、
合計がjにすることは可能か
"""
def A18(): #配るDP
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                #方法A
                dp[i+1][j] = True
                #方法B
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = True

    print("Yes" if dp[n][s] else "No")


def A18_ans(): #もらうDP
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        for j in range(s+1):
            if dp[i-1][j] == True:
                dp[i][j] = True
            if 0 <= j-a[i-1] < s+1 and dp[i-1][j-a[i-1]] == True:
                dp[i][j] = True

    print("Yes" if dp[n][s] else "No")


def B18():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    #sになる組み合わせはあるか探索
    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    #配るDP
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]==True:
                dp[i+1][j] = True
            if dp[i][j]==True and j+a[i] <= s:
                dp[i+1][j+a[i]] = True

    if dp[n][s] == False:
        print(-1)
    else:
        #sになる組み合わせを復元
        dp2 = [[False]*(s+1) for i in range(n+1)]
        dp2[n][s] = True
        ans = []
        #配るDP
        for i in reversed(range(n+1)):
            for j in range(s+1):
                if dp2[i][j]:
                    if dp[i-1][j]:
                        dp2[i-1][j] = True
                    elif 0<=j-a[i-1] and dp[i-1][j-a[i-1]]:
                        dp2[i-1][j-a[i-1]] = True
                        ans.append(i)
        #output
        ans.reverse()
        print(len(ans))
        ans = " ".join([str(x) for x in ans])
        print(ans)


def B18_ans():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    #sになる組み合わせはあるか探索
    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    #配るDP
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]==True:
                dp[i+1][j] = True
            if dp[i][j]==True and j+a[i] <= s:
                dp[i+1][j+a[i]] = True

    if dp[n][s] == False:
        print(-1)
    else:
        #sになる組み合わせを復元
        place = s
        ans = []
        #配るDP
        for i in reversed(range(1, n+1)):
            if dp[i-1][place] == True:#カードiを選ばない
                place = place-0
            else:
                place = place - a[i-1]#カードiを選ぶ
                ans.append(i)
        #output
        ans.reverse()
        print(len(ans))
        ans = " ".join([str(x) for x in ans])
        print(ans)


def A19():
    n, w = map(int, input().split())
    ws = []
    vs = []
    for i in range(n):
        wi, vi = map(int, input().split())
        ws.append(wi)
        vs.append(vi)
    """
    dp[i][j]
    ものiまでを選んだ重量がjで、その時の価値がdp[i][j]
    """
    dp = [[-1]*(w+1) for i in range(n+1)]
    dp[0][0] = 0
    #配るDP
    for i in range(n):
        for j in range(w+1):
            if dp[i][j] >= 0:#ものiを選ばない
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            
            if j+ws[i]<=w and dp[i][j]>=0:#ものiを選ぶ
                dp[i+1][j+ws[i]] = max(dp[i+1][j+ws[i]], dp[i][j]+vs[i])
    #output
    ans = 0
    for j in range(w+1):
        ans = max(ans, dp[n][j])
    print(ans)


def B19():
    n, w = map(int, input().split())
    ws = []
    vs = []
    for i in range(n):
        wi, vi = map(int, input().split())
        ws.append(wi)
        vs.append(vi)

    dp = [[10**15]*(100001) for i in range(n+1)]
    dp[0][0] = 0
    #配るDP
    for i in range(n):
        for j in range(100001):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j+vs[i] < 100001:#もらうDPを使うとここが要らない?
                dp[i+1][j+vs[i]] = min(dp[i+1][j+vs[i]], dp[i][j]+ws[i])
    #output
    ans = 0
    for j in range(100001):
        if dp[n][j] <= w:
            ans = max(ans, j)
    print(ans)


def A20():
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    dp = [[0]*(m+1) for i in range(n+1)]
    dp[0][0] = 0
    #もらうDP
    for i in range(n+1):
        for j in range(m+1):
            if i>=1 and j>=1 and s[i-1]==t[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            elif i>=1 and j>=1:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            elif i>=1:
                dp[i][j] = dp[i-1][j]
            elif j>=1:
                dp[i][j] = dp[i][j-1]

    print(dp[n][m])


"""
dp[i][j]
文字列sのi文字目、文字列tのj文字目まで並べた時、
その時点での合計コストの最小値はいくつか
"""
def B20_ans():
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    dp = [[0]*(m+1) for i in range(n+1)]
    dp[0][0] = 0
    #もらうDP
    for i in range(n+1):
        for j in range(m+1):
            if i>=1 and j>=1 and s[i-1]==t[j-1]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            elif i>=1 and j>=1:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
            elif i>=1:
                dp[i][j] = dp[i-1][j]+1
            elif j>=1:
                dp[i][j] = dp[i][j-1]+1
    print(dp[n][m])


"""
dp[l][r]
lからr番目までのブロックが残っている状態を考える。
この状態になるまでに最大で何点稼ぐことができるか
"""
def A21_ans():
    n = int(input())
    p = [0]*(n+1)
    a = [0]*(n+1)
    for i in range(1, n+1):
        p[i], a[i] = map(int, input().split())

    dp = [[None]*(n+1) for i in range(n+1)]
    dp[1][n] = 0
    for LEN in reversed(range(0, n-1)):
        for l in range(1, n-LEN+1):
            r = l + LEN
            
            #score1の値（l-1番目のブロックを取り除く時の得点）を求める
            score1 = 0
            if l>=2 and l<=p[l-1] and p[l-1]<=r:
                score1 = a[l-1]
            
            #score2の値（r+1番目のブロックを取り除く時の得点）を求める
            score2 = 0
            if r<=n-1 and l<=p[r+1] and p[r+1]<=r:
                score2 = a[r+1]
            
            #dp[l][r]を求める
            if l==1:
                dp[l][r] = dp[l][r+1] + score2
            elif r==n:
                dp[l][r] = dp[l-1][r] + score1
            else:
                dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)
    #output
    ans = 0
    for i in range(1, n+1):
        ans = max(ans, dp[i][i])
    print(ans)


"""
dp[l][r]
文字列sのl文字目からr文字目までの部分における最長回文の長さ
"""
def B21():
    n = int(input())
    s = input()

    #DP 初期状態
    dp = [[0]*(n) for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    #DP 状態遷移
    for LEN in range(2, n):
        for l in range(n-LEN):
            r = l+LEN
            if s[l]==s[r]:
                dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1]+2)
            else:
                dp[l][r] = max(dp[l][r-1], dp[l+1][r])
    print(dp[0][n-1])


"""
初期化は丁寧にやる
"""
def A22():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #dp = [-1]*n #WA
    dp = [-(10**9)]*n #AC
    dp[0] = 0
    #配るDP
    for i in range(n-1):
        #A
        dp[a[i]-1] = max(dp[a[i]-1], dp[i]+100)
        #B
        dp[b[i]-1] = max(dp[b[i]-1], dp[i]+150)
    print(dp[n-1])


def A16_2():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #配るDP
    dp = [10**9]*(n+1)
    dp[1] = 0
    for i in range(1, n):
        if i+1 <= n:
            dp[i+1] = min(dp[i+1], dp[i]+a[i-1])
        if i+2 <= n:
            dp[i+2] = min(dp[i+2], dp[i]+b[i-1])
    print(dp[n])


"""
ビットDP
"""
def A23():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))

    dp = [[10**9]*(2**n) for i in range(m+1)]
    dp[0][0] = 0
    for i in range(1, m+1):
        for j in range(2**n):
            #already[k]=1 の時、品物kは既に無料になっている
            already = [None]*n
            for k in range(n):
                if (j // (2**k)) %2 == 0:
                    already[k] = 0
                else:
                    already[k] = 1
            #クーポン券iを選んだ時の整数表現vを計算
            v = 0
            for k in range(n):
                if already[k]==1 or a[i-1][k]==1:
                    v += 2**k
            #遷移を使う
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            dp[i][v] = min(dp[i][v], dp[i-1][j]+1)
    #出力
    if dp[m][2**n-1]==10**9:
        print(-1)
    else:
        print(dp[m][2**n-1])


def A24():
    import bisect
    n = int(input())
    a = list(map(int, input().split()))

    #DPの準備
    LEN = 0 #LENはLの長さ
    L = []
    dp = [None]*n

    for i in range(n):
        pos = bisect.bisect_left(L, a[i])
        dp[i] = pos
        #配列Lを更新
        if dp[i] >= LEN:
            L.append(a[i])
            LEN += 1
        else:
            L[dp[i]] = a[i]
    print(LEN)


def A25():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))

    dp = [[0]*(w) for i in range(h)]
    dp[0][0] = 1
    #もらうDP
    for i in range(h):
        for j in range(w):
            if j>0 and c[i][j]==".":
                dp[i][j] += dp[i][j-1]
            if i>0  and c[i][j]==".":
                dp[i][j] += dp[i-1][j]

    print(dp[h-1][w-1])
