
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
