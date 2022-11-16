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
    s, w = map(int, input().split())
    ans = (w >= s)
    print("unsafe" if ans else "safe")


def B():
    a, b, c, d = map(int, input().split())

    while True:
        c -= b
        if c <= 0:
            ans = True
            break
        a -= d
        if a <= 0:
            ans = False
            break
    print("Yes" if ans else "No")


def C():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())

    ans = len(list(s))
    print(ans)


# def D():

