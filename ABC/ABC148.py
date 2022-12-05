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
    a = int(input())
    b = int(input())

    s = set([a, b])
    for i in range(1, 4):
        if i not in s:
            print(i)
            break


def B():
    n = int(input())
    s, t = input().split()

    u = []
    for i in range(n):
        u.append(s[i])
        u.append(t[i])

    ans = "".join([str(x) for x in u])
    print(ans)


def C():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)

    a, b = map(int, input().split())
    ans = lcm(a, b)
    print(ans)


def D():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    num = 1
    cnt = 0
    for i in range(n):
        if a[i] == num:
            num += 1
        else:
            cnt += 1

    if 0 < cnt <= n-1:
        ans = cnt
    elif cnt == n:
        ans = -1

    print(ans)
