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
ans = True
ans = False
print("Yes" if ans else "No")
'''

def A():
    a, b, c = map(int, input().split())

    from collections import Counter
    if a==b and b==c:
        print(a)
    elif a!=b and b!=c and c!=a:
        print(0)
    else:
        c = Counter([a, b, c])
        print(c.most_common()[-1][0])


def B():
    n, k = map(int, input().split())
    ans = 0
    for i in range(n):
        for j in range(k):
            ans += int("{}0{}".format(i+1, j+1))
    print(ans)


def C_TLE():
    n, k = map(int, input().split())

    from collections import defaultdict
    d = defaultdict(int)

    for i in range(n):
        a, b = map(int, input().split())
        d[a] += b

    pos = 0
    while k>0:
        pos += 1
        k -= 1
        if pos in d:
            k += d[pos]
    print(pos)


def C():
    n, k = map(int, input().split())

    tmp = []
    for i in range(n):
        a, b = map(int, input().split())
        tmp.append([a, b])
    tmp = sorted(tmp)

    ans = k
    for i in range(n):
        if ans >= tmp[i][0]:
            ans += tmp[i][1]

    print(ans)
