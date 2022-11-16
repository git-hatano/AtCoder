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
    k = int(input())
    a, b = map(int, input().split())
    ans = False

    if (a - a%k + k) <= b or a%k==0 or b%k==0:
        ans = True
    print("OK" if ans else "NG")


"""
小数の誤差でWAが1つでる
"""
def B_WA():
    x = int(input())
    s = 100
    ans = 0

    while x > s:
        s += int(s/100)
        ans += 1
    print(ans)


def B_ans():
    x = int(input())
    s = 100
    ans = 0

    while x > s:
        s *= 101
        s //= 100
        ans += 1
    print(ans)


# def C():



# def D():

