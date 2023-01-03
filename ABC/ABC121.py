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
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    ans = H*W - H*w - (W-w)*h
    print(ans)


def B():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        s = 0
        for j in range(m):
            s += a[j]*b[j]
        if s+c > 0:
            ans += 1
    print(ans)


def C():
    n, m = map(int, input().split())
    x = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append([a, b])
    x.sort()

    ans = 0
    for i in range(n):
        if m==0:
            break
        cnt = min(m, x[i][1])
        ans += x[i][0]*cnt
        m -= cnt
    print(ans)


# def D():

