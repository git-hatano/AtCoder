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
    n, m = map(int, input().split())
    ans = (n==m)
    print("Yes" if ans else "No")


def B():
    a, b = map(int, input().split())
    s = sorted([str(a)*b, str(b)*a])
    ans = s[0]
    print(ans)


def C():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_old = p[0]
    for i in range(n):
        if p[i] <= min_old:
            ans += 1
        min_old = min(min_old, p[i])

    print(ans)




# def D():

