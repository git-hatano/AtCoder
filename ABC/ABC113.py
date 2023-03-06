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

def A():
    x, y = map(int, input().split())
    ans = x+y//2
    print(ans)


def B():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    diff = float("inf")
    ans = -1
    for i in range(n):
        tmp = t - h[i]*0.006
        if abs(tmp - a) < diff:
            ans = i+1
            diff = abs(tmp - a)
    print(ans)


def C():
    from collections import defaultdict
    n, m = map(int, input().split())
    #key: 県の番号
    d = defaultdict(list)
    #県ごとに市を格納
    for i in range(m):
        p, q = map(int, input().split())
        d[p].append([q, i])
    #県ごとに市の番号を割り振り
    for k in d:
        d[k].sort()
        for i in range(len(d[k])):
            s = str(k).zfill(6)
            s += str(i+1).zfill(6)
            d[k][i].append(s)
    #1つに戻して出力
    res = []
    for k in d:
        for i in range(len(d[k])):
            res.append(d[k][i])
    res.sort( key=lambda x: x[1])
    for i in range(m):
        print(res[i][2])


# def D():

