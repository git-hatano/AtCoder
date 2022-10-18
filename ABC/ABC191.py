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
    v, t, s, d= map(int, input().split())
    if v*t <= d <= v*s:
        ans = False
    else:
        ans = True
    print("Yes" if ans else "No")


def B():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(str(a[i]))
    print(" ".join(ans))


# def C():



# def D():

