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

def A71():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    print(ans)


"""
白の個数が多い行、列から黒く塗っていく
1WA : こういうケースが通らない
...#
..#.
.#..
.###
"""
def A72_WA():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    #各行の白の個数
    white_row = []
    for i in range(h):
        white = 0
        for j in range(w):
            if c[i][j]==".":
                white += 1
        white_row.append([white, i])
    #各列の白の個数
    white_col = []
    for j in range(w):
        white = 0
        for i in range(h):
            if c[i][j]==".":
                white += 1
        white_col.append([white, j])

    #白の個数が大きい順にソート
    white_row.sort(reverse=True)
    white_col.sort(reverse=True)
    #白の個数が大きい順に、行or列を黒で塗りつぶす: 出力時にカウントしない様にする
    mask_row = set()
    mask_col = set()
    i, j = 0, 0
    for l in range(k):
        if white_row[i][0]-j > white_col[j][0]-i:
            mask_row.add(white_row[i][1])
            i += 1
        else:
            mask_col.add(white_col[j][1])
            j += 1
    #最終的な白の個数をカウント
    white = 0
    for i in range(h):
        if i not in mask_row:
            for j in range(w):
                if j not in mask_col:
                    if c[i][j]==".":
                        white += 1
    ans = h*w-white
    print(ans)


"""
行数の制約が小さいので、行は全bit探索して
その後に余っている回数分だけ白が多い列から塗れば良かった
"""
def A72_ans():
    import itertools
    #残り回の列に対する操作で、最大何個のマスを黒くできるかを返す関数
    def paint_row(h, w, d, remaining_steps):
        #各列に対して（白マスの個数、列の番号）のタプルを記録し、大きい順にソート
        column = [ ([d[i][j] for i in range(h)].count("."), j) for j in range(w) ]
        column.sort(reverse=True)
        
        #列に対して操作を行う
        for j in range(remaining_steps):
            idx = column[j][1]
            for i in range(h):
                d[i][idx] = "#"
        #黒マスの個数を数えて返す
        return sum(map(lambda l: l.count("#"), d)) #行ごとに黒を数えて合計を返す

    h, w, k = map(int, input().split())
    c = [input() for _ in range(h)]

    #行の塗り方を全探索
    ans = 0
    for v in itertools.product([0, 1], repeat=h):
        # print(v)#(0, 1, 1, 0)
        d = [list(c[i]) for i in range(h)]
        remaining_steps = k
        for i in range(h):
            if v[i]==1:
                d[i] = ["#"]*w
                remaining_steps -= 1
        
        if remaining_steps>=0:
            subans = paint_row(h, w, d, remaining_steps)
            ans = max(ans, subans)
    print(ans)


def A73_ans():
    from collections import defaultdict
    import heapq
    n, m = map(int, input().split())
    paths = [list(map(int, input().split())) for _ in range(m)]
    g = defaultdict(list)

    for i in range(m):
        a, b, c, d = paths[i]
        a -= 1
        b -= 1
        g[a].append([b, 10000*c-d])
        g[b].append([a, 10000*c-d])

    #重み付き最短経路問題ならダイクストラ法
    kakutei = [False]*n #kakutei[i]: 頂点iの最短経路が確定したか
    cur = [10**10]*n
    #最短距離を更新
    cur[0] = 0
    que = []
    heapq.heapify(que)
    heapq.heappush(que, [cur[0], 0])

    while len(que)>0:
        #次に確定させる頂点を決める
        pos = heapq.heappop(que)[1]
        #既にposへの最短経路が確定していれば何もしない
        if kakutei[pos]:
            continue
        #cur[i]の更新
        kakutei[pos] = True
        for nex, cost in g[pos]:
            if cur[nex] > cur[pos]+cost:
                cur[nex] = cur[pos]+cost
                heapq.heappush(que, [cur[nex], nex])

    #距離: cur[n-1]//10000 の小数点以下を切り上げた値
    distance = (cur[n-1]+9999)//10000
    trees = distance*10000 - cur[n-1]
    print(f"{distance} {trees}")


def A74():
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    x = [0]*n
    y = [0]*n
    for i in range(n):
        for j in range(n):
            if p[i][j]!=0:
                x[i] = p[i][j]
                y[j] = p[i][j]
    #操作回数をバブルソートで数える
    inv_x = 0
    inv_y = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i]>x[j]:
                x[i], x[j] = x[j], x[i]
                inv_x += 1
            if y[i]>y[j]:
                y[i], y[j] = y[j], y[i]
                inv_y += 1
    ans = inv_x + inv_y
    print(ans)


def A75():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: x[1])
    """
    dp[i][j]:
    手順iが終了した時点の現在時刻がjであるとき、既に何問解答できているか
    """
    max_d = max(map(lambda p: p[1], a))#1440
    dp = [[-1]*(max_d+1) for i in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        t, d = a[i]
        for j in range(max_d+1):
            if j>d or j<t:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-t]+1)
    ans = max(dp[n])
    print(ans)


def A76():
    import bisect
    n, w, l, r = map(int, input().split())
    x = list(map(int, input().split()))
    mod = 10**9 +7

    #西岸を足場0、東岸を足場n+1とみなす
    x = [0] + x + [w]
    #dp
    dp = [0]*(n+2)
    dpsum = [0]*(n+2)
    dp[0] = 1
    dpsum[0] = 1
    for i in range(1, n+2):
        posl = bisect.bisect_left(x, x[i]-r)
        posr = bisect.bisect_left(x, x[i]-l+1)-1
        #dp[i]の値を累積和で計算
        dp[i] = (dpsum[posr] if posr>=0 else 0) - (dpsum[posl-1] if posl>=1 else 0)
        dp[i] %= mod
        #累積和dpsum[i]の値を更新
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[n+1])


def A77():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    #スコアの最大値がx以上かを判定する関数
    def check(x):
        cnt = 0 #現時点で何回切ったか
        last_kireme = 0 #最後どこで切ったか
        for i in range(n):
            if a[i]-last_kireme>=x and l-a[i]>=x:
                cnt += 1
                last_kireme = a[i]
        return cnt>=k

    #二分探索 left:現在の上限, right:現在の下限
    left, right = 1, 10**9
    while left < right:
        mid = (left+right+1)//2
        ans = check(mid)
        if ans==False:
            right = mid-1
        else:
            left = mid
    print(left)
