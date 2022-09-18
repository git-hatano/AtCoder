
def B():
    import math
    N, K = map(int, input().split())
    A = [a-1 for a in list(map(int, input().split()))]

    XY = []
    for _ in range(N):
        X, Y = map(int, input().split())
        XY.append([X, Y])

    R_s = [2*math.sqrt(2)*10**5 for i in range(N)]
    for k in A:
        for n in range(N):
            R_tmp = math.sqrt((XY[k][0]-XY[n][0])**2 + (XY[k][1]-XY[n][1])**2)

            if R_tmp < R_s[n]:
                R_s[n] = R_tmp

    print(max(R_s))


def B_answer():
    import math
    N, K = map(int, input().split())
    A = [a-1 for a in list(map(int, input().split()))]

    XY = []
    for _ in range(N):
        X, Y = map(int, input().split())
        XY.append([X, Y])

    R = 0
    for n in range(N):
        R_tmp = 5*10**5
        for k in A:
            R_tmp = min(R_tmp, math.sqrt((XY[k][0]-XY[n][0])**2 + (XY[k][1]-XY[n][1])**2))

        R = max(R, R_tmp)

    print(R)


def A():
    r,c = map(int, input().split())
    r -= 1
    c -= 1

    a = []
    for i in range(2):
        a1, a2 = map(int, input().split())
        a.append([a1, a2])

    print(a[r][c])


def C_TLE():
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


def C():
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


def D_TLE():
    import numpy as np
    n, q = map(int, input().split())
    a = np.array(list(map(int, input().split())))

    x = []
    for _ in range(q):
        x.append(int(input()))

    for i in x:
        print(np.sum(np.abs(a-i)))


def D():
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

