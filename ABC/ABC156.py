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
    n, r = map(int, input().split())
    if n >= 10:
        ans = r
    else:
        ans = r + 100 * (10-n)
    print(ans)


def B():
    n, k = map(int, input().split())
    ans = []
    while n >= k:
        ans.append(n%k)
        n //= k
    ans.append(n)
    print(len(ans))


def C():
    n = int(input())
    x = list(map(int, input().split()))

    ans = float("inf")
    for p in range(1, 101):
        tmp = 0
        for i in range(n):
            tmp += (x[i]-p)**2
        ans = min(ans, tmp)
    print(ans)


# def D():

