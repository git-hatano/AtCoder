'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
'''

def A():
    # 文字列を受け取る場合
    S = input() 

    s_list = []
    for s in S:
        s_list.append(int(s))

    for n in range(10):
        if n not in s_list:
            print(n)


def B():
    # 複数の整数を入力
    A, B, K = map(int, input().split())

    cnt = 0
    while True:
        if A >= B:
            print(cnt)
            break
        else:
            A = A*K
            cnt += 1


def C_WA():
    N, M, K = map(int, input().split())
    A_list = [1]*N

    cnt = 0
    for n in range(N):
        for m in range(M):
            A_list[n] = m+1

            if sum(A_list) <= K:
                cnt+=1


def C():
    N, M, K = map(int, input().split())
    mod = 998244353

    dp = [[0]*(K+1) for i in range(N+1)]
    dp[0][0] = 1

    for x in range(1, N+1):
        for y in range(0, K+1):
            now = 0
            for i in range(1, M+1):
                if y-i >= 0:
                    now += dp[x-1][y-i]
                    now %= mod
            
            dp[x][y] = now

    ans = 0
    for y in range(0, K+1):
        ans += dp[N][y]
        ans %= mod
    print(ans)


"""
TLEが2つ出る
"""
def D_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(list)
    for i in range(n):
        d[a[i]].append(i)

    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        l -= 1
        r -= 1
        ans = 0
        if x in d:
            for v in d[x]:#このforがネック
                if l <= v <= r:
                    ans += 1
        print(ans)


"""
与えられた配列の中にLからRの数は何個あるか
これを計算するには二分探索が使える。
参考: https://blog.hamayanhamayan.com/entry/2022/04/16/230012
"""
def C_ans():
    from collections import defaultdict
    from bisect import bisect_left, bisect_right

    n = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(list)
    for i in range(n):
        d[a[i]].append(i)#ここまではOK

    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        l -= 1
        r -= 1
        st = bisect_left(d[x], l) #L以上の数が初めて現れる場所
        gl = bisect_right(d[x], r) #Rより大きい数が初めて現れる場所
        ans = gl - st
        print(ans)

