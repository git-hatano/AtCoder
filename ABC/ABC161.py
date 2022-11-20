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
    a = list(map(int, input().split()))
    a[0], a[1] = a[1], a[0]
    a[0], a[2] = a[2], a[0]
    ans = " ".join([str(x) for x in a])
    print(ans)


def B():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    thresh = sum(a)/(4*m)
    for i in range(n):
        if a[i] >= thresh:
            cnt += 1
    print("Yes" if cnt>=m else "No")


def C():
    n, k = map(int, input().split())
    if n>=k:
        n %= k
    ans = min(n, abs(n-k))
    print(ans)


# def D():

