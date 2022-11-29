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
    h, a = map(int, input().split())
    ans = h//a
    if h%a > 0:
        ans += 1
    print(ans)


def B():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))

    ans = False
    if sum(a) >= h:
        ans = True
    print("Yes" if ans else "No")


def C():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0
    if len(h) > k:
        h.sort(reverse=True)
        for i in range(k, n):
            ans += h[i]

    print(ans)


def D():
    h = int(input())
    #攻撃回数
    cnt = 0
    #モンスター数
    num = 1
    #1モンスターの体力
    x = h

    while x>1:
        cnt += num
        num *= 2
        x //= 2

    ans = cnt + num
    print(ans)
