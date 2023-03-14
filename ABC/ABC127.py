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
    a, b = map(int, input().split())
    if a>=13:
        print(b)
    elif 6<=a<=12:
        print(b//2)
    else:
        print(0)


def B():
    r, d, x = map(int, input().split())
    for i in range(10):
        x = r*x -d
        print(x)


def C():
    n, m = map(int, input().split())
    l = [None]*m
    r = [None]*m
    for i in range(m):
        l[i], r[i] = map(int, input().split())

    ans = max(0, min(r) - max(l) +1)
    print(ans)


def D():
    from collections import defaultdict
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    #変換先の数字をカウント
    cnter = defaultdict(int)
    for i in range(m):
        k = bc[i][1] #c
        v = bc[i][0] #b
        cnter[k] += v
    #変換先の数字を管理
    keys = list(cnter.keys())
    ki = 0
    #a[i]の小さい方から変換
    for i in range(n):
        if ki<len(keys):
            key = keys[ki]
            if key>a[i]:
                a[i] = key
                cnter[key] -= 1
                if cnter[key]==0:
                    del cnter[key]
                    ki += 1
    ans = sum(a)
    print(ans)
