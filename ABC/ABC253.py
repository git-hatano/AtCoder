from math import radians

def B():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())

    points = []
    for h in range(H):
        for w in range(W):
            if S[h][w]=="o":
                points.append([h, w])

    shift = abs(points[1][0]-points[0][0]) + abs(points[1][1]-points[0][1])
    print(shift)


def A():
    a, b, c = map(int, input().split())
    tmp = [a, b, c]
    tmp = sorted(tmp)

    if tmp[1] == b:
        print("Yes")
    else:
        print("No")

def C_TLE():
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
            

def D_RE():
    N, A, B = map(int, input().split())

    import numpy as np
    nums = np.arange(1, N+1)
    nums = nums[nums%A != 0]
    nums = nums[nums%B != 0]
    print(nums.sum())


def D_TLE():
    N, A, B = map(int, input().split())
    sum_n = 0
    for n in range(1, N+1):
        if n%A!=0 and n%B!=0:
            sum_n += n
    print(sum_n)


def D_TLE_WA():
    n, a, b = map(int, input().split())
    total = sum(range(1, n+1))

    i_a = range(1, int(n//a)+1)
    sum_a = sum(list(map(lambda x: x*a, i_a)))

    i_b = range(1, int(n//b)+1)
    sum_b = sum(list(map(lambda x: x*b, i_b)))

    i_ab = range(1, int(n//(a*b))+1)
    sum_ab = sum(list(map(lambda x: x*a*b, i_ab)))

    print(total -sum_a -sum_b +sum_ab)


def D():
    from math import gcd
    def f(n):
        n = int(n)
        return int(n*(n+1)//2)

    n, a, b = map(int, input().split())
    L = a*b // gcd(a, b)
    value = f(n) - a * f(n//a) - b * f(n//b) + L * f(n//L)
    print(value)
