"""
DP勉強用
"""


"""
DPまとめコンテスト
https://atcoder.jp/contests/dp/tasks
"""

def A():
    n = int(input())
    h = list(map(int, input().split()))

    #初期化
    dp = [float("inf")]*n
    #初期条件
    dp[0] = 0

    for i in range(n-1):
        #配る遷移
        #1つ左から移動
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i+1]-h[i]))
        #2つ左から移動
        if i+2<n:
            dp[i+2] = min(dp[i+2], dp[i]+abs(h[i+2]-h[i]))

    print(dp[-1])


"""
アルゴ輪講本の例題
"""

