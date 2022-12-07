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
