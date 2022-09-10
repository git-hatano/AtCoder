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
if ans:
    print("Yes")
else:
    print("No")
'''


def A():
    def f(x):
        return x**2 + 2*x + 3

    t = int(input())
    ans = f(f(f(t) + t) + f(f(t)))
    print(ans)


def B():
    n = int(input())

    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    import itertools
    comb = list(itertools.combinations(points, 2))

    import math
    max_l = -1
    for t in comb:
        l = math.sqrt((t[1][0] - t[0][0])**2 + (t[1][1] - t[0][1])**2)
        if l > max_l:
            max_l = l

    print(max_l)


def C_TLE():
    k = int(input())

    i = 1
    cnt = 0
    while True:
        if set(list(str(i)))=={"2"} or set(list(str(i)))=={"0", "2"}:
            cnt += 1
            if k==cnt:
                break
        i += 1

    print(i)


def C():
    k = int(input())

    # 2進数表示に変換
    k_bin = bin(k)[2:]

    ans = ""
    for b in k_bin:
        if b=="1":
            ans += "2"
        else:
            ans += "0"

    print(int(ans))


def D_TLE():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    k -= 1
    buf = []
    for i in range(n):
        buf.append(p[i])

        if i >= k:
            buf = sorted(buf, reverse=True)
            print(buf[k])
    
    
def D_TLE2():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    buf = p[:k]
    buf = sorted(buf, reverse=True)
    print(buf[-1])

    for i in range(k, n):

        # bufで管理する個数をk個に絞ったら、少し早くなる
        # しかし、ｋが大きすぎるとダメ
        if p[i] > buf[-1]:
            del buf[-1]
            buf.append(p[i])
            buf = sorted(buf, reverse=True)

        print(buf[-1])


"""
優先度付きキュー
"""
def D():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    que = p[:k]
    print(min(que))

    import heapq
    heapq.heapify(que)

    for i in range(k, n):
        # queの中身を更新
        minima = heapq.heappop(que)
        minima = max(minima, p[i])
        heapq.heappush(que, minima)
        # queの最小値を表示
        ans = heapq.heappop(que)
        print(ans)
        heapq.heappush(que, ans)



