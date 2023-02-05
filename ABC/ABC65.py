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

# def A():



# def B():



def C():
    import math
    n, m = map(int, input().split())
    ans = 0
    mod = 10**9 +7
    if abs(n-m)<=1:
        tmp = math.factorial(n)%mod
        tmp *=  math.factorial(m)%mod
        tmp %= mod
        if n==m:
            tmp *= 2
            tmp %= mod
        ans = tmp
    print(ans)


# def D():

