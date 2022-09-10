def ABC253_C_TLE():
    Q = int(input())

    querys = []
    for i in range(Q):
        querys.append(input())

    S = []
    for query in querys:
        query_type = int(query[0])

        if query_type == 1:
            x = int(query.split(" ")[-1])
            S.append(x)

        elif query_type == 2:
            x = int(query.split(" ")[-2])
            c = int(query.split(" ")[-1])

            for i in range(min(c, S.count(x))):
                S.remove(x)

        elif query_type == 3:
            print(max(S)-min(S))


def ABC255_C_TLE():
    def getNearestValue(list, num):
        """
        概要: リストからある値に最も近い値を返却する関数
        @param list: データ配列
        @param num: 対象値
        @return 対象値に最も近い値
        """
        import numpy as np
        # リスト要素と対象値の差分を計算し最小値のインデックスを取得
        idx = np.abs(np.asarray(list) - num).argmin()
        return list[idx]

    X, A, D, N = map(int, input().split())
    S = [A+D*n for n in range(N)]

    process = 0
    if X not in S:
        process = abs(X - getNearestValue(S, X))

    print(process)

def ABC255_C():
    x, a, d, n = map(int, input().split())
    if d == 0:
        print(abs(a-x))
    else:
        m = a + (n-1)* d #末項
        ans = min(abs(a-x), abs(x-m))
        y = a + ( (x-a)//d ) * d

        for i in range(-2, 3):# 周辺 ±2 程度を探索
            z = y + i * d

            if a <= z <= m or m <= z <= a:# 探索している数が範囲内にあるかどうか
                ans = min(ans, abs(z-x))
            
        print(ans)


def ABC255_D_TLE():
    import numpy as np
    n, q = map(int, input().split())
    a = np.array(list(map(int, input().split())))

    x = []
    for _ in range(q):
        x.append(int(input()))

    for i in x:
        print(np.sum(np.abs(a-i)))


def ABC255_D():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    rw = [0]*(n+1)
    for i in range(n):
        rw[i+1] = rw[i] + a[i]

    for i in range(q):
        x = int(input())
        st = 0
        fi = n-1

        while(st <= fi):
            te = int((st+fi) /2)
            if a[te] < x:
                st = te +1
            else:
                fi = te -1

        res = x * st
        res -= rw[fi +1]

        res += (rw[n] - rw[st])
        res -= x*(n - st)

        print(res)


def ABC252_C_WA():
    n = int(input())
    res = []
    for _ in range(n):
        buf = [0]*10
        S = input()

        for i, s in enumerate(S):
            buf[int(s)] = i
        
        res.append(buf)

    print(res)


def ABC252_C():
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())

    cnt = [[0 for j in range(10)] for i in range(10)]
    for i in range(n):
        for j in range(10):
            cnt[int(s[i][j])][j] = cnt[int(s[i][j])][j] +1

    mx = [0 for i in range(10)]
    for i in range(10):
        for j in range(10):
            mx[i] = max(mx[i], 10 * (cnt[i][j]-1) +j)

    print(min(mx))


def ABC253_D_RE():
    N, A, B = map(int, input().split())

    import numpy as np
    nums = np.arange(1, N+1)
    nums = nums[nums%A != 0]
    nums = nums[nums%B != 0]
    print(nums.sum())


def ABC253_D_TLE():
    N, A, B = map(int, input().split())
    sum_n = 0
    for n in range(1, N+1):
        if n%A!=0 and n%B!=0:
            sum_n += n
    print(sum_n)


def ABC253_D_TLE_WA():
    n, a, b = map(int, input().split())
    total = sum(range(1, n+1))

    i_a = range(1, int(n//a)+1)
    sum_a = sum(list(map(lambda x: x*a, i_a)))

    i_b = range(1, int(n//b)+1)
    sum_b = sum(list(map(lambda x: x*b, i_b)))

    i_ab = range(1, int(n//(a*b))+1)
    sum_ab = sum(list(map(lambda x: x*a*b, i_ab)))

    print(total -sum_a -sum_b +sum_ab)


def ABC253_D():
    from math import gcd
    def f(n):
        n = int(n)
        return int(n*(n+1)//2)

    n, a, b = map(int, input().split())
    L = a*b // gcd(a, b)
    value = f(n) - a * f(n//a) - b * f(n//b) + L * f(n//L)
    print(value)


def ABC249_C_WA():
    # 問題の意味がわからん。こんなん初めてや
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    print()


def ABC249_C():
    from collections import Counter
    from itertools import product

    def solve():
        def calc(pro):
            """選び方 pro に対する答えを求める"""
            C = Counter()  # 空のカウンターを用意する
            for i in range(N):
                if pro[i]:
                    # S[i]を選ぶ場合、S[i]に含まれる文字のカウントにそれぞれ1足す C.update(S[i])なら1行
                    for ch in S[i]:
                        C[ch] += 1
            score = 0
            for ch, cnt in C.items():
                if cnt == K:  # K回"ちょうど"の種類数です
                    score += 1
            return score

        N, K = map(int, input().split())
        S = [input() for _ in range(N)]
        ans = 0
        for pro in product((True, False), repeat=N):
            ans = max(ans, calc(pro))
        return ans

    print(solve())


def ABC245_C():
    # 動的計画法
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [False]*n
    ep = [False]*n

    dp[0] = True
    ep[0] = True

    for i in range(1, n):
        if dp[i-1]:
            if abs(a[i-1] - a[i])<=k:
                dp[i] = True
            if abs(a[i-1] - b[i])<=k:
                ep[i] = True
        
        if ep[i-1]:
            if abs(b[i-1] - a[i])<=k:
                dp[i] = True
            if abs(b[i-1] - b[i])<=k:
                ep[i] = True

    if dp[n-1] or ep[n-1]:
        print("Yes")
    else:
        print("No")


def ABC243_C_TLE():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append([x, y])

    s = input()
    can = False

    if s=="R"*n or s=="L"*n:
        can = False

    else:
        for i in range(n):
            for j in range(i+1, n):
                if xy[i][1] == xy[j][1]:

                    if xy[i][0] < xy[j][0] and s[i]=="R" and s[j]=="L":
                        can = True
                    if xy[i][0] > xy[j][0] and s[i]=="L" and s[j]=="R":
                        can = True

                    if can:
                        break
            if can:
                break

    if can:
        print("Yes")
    else:
        print("No")


def ABC243_C():
    def Yes():
        print("Yes")
        exit(0)

    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()

    right_min, left_max = dict(), dict()

    for i in range(N):
        if S[i] == 'R':
            if Y[i] in left_max and X[i] < left_max[Y[i]]:
                Yes()
        else:
            if Y[i] in right_min and right_min[Y[i]] < X[i]:
                Yes()

        if S[i] == 'R':
            if Y[i] in right_min:
                right_min[Y[i]] = min(X[i], right_min[Y[i]])
            else:
                right_min[Y[i]] = X[i]
        else:
            if Y[i] in left_max:
                left_max[Y[i]] = max(X[i], left_max[Y[i]])
            else:
                left_max[Y[i]] = X[i]

    print("No")



def func(n):
    if n==0:
        return 0
    else:
        return n + func(n-1)
