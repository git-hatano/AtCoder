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
    a, b = map(int, input().split())
    if a*6>=b and b>=a:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    p = int(input())

    cnt = 0
    ans = 0
    while p:
        tmp = 1
        for i in range(1, 10**7):
            tmp *= i
            if tmp>p:
                break
        cnt = p//(tmp/i)
        p -= cnt*(tmp/i)
        ans += cnt

    print(int(ans))


def C():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a_i = []
    for i in range(n):
        a_i.append([a[i], i])
    a_i = sorted(a_i)

    base = k//n
    k -= base*n

    for i in range(n):
        if k:
            a_i[i].append(base+1)
            k -= 1
        else:
            a_i[i].append(base)

    a_i = sorted(a_i, key=lambda x: x[1])
    for i in range(n):
        print(a_i[i][2])


# def D():

