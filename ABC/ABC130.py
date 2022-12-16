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
    x, a = map(int, input().split())
    if x<a:
        print(0)
    else:
        print(10)


def B():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(1, n+1):
        if d+l[i-1]<=x:
            ans += 1
        d = d + l[i-1]
    print(ans)


"""
割り算, 小数は信用できない
WA: w//2==x and h//2==x
AC: 2*x==w and 2*y==h
"""
def C():
    w, h, x, y = map(int, input().split())
    num = 0
    s = w*h/2
    if 2*x==w and 2*y==h:
        num = 1
    print(s, num)


# def D():

