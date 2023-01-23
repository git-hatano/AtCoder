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
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)

    n = int(input())
    a = list(map(int, input().split()))
    #最小公倍数
    m = 0
    for i in range(n):
        m = lcm(m, a[i])
    ans = 0
    for i in range(n):
        ans += (m-1) % a[i]
    print(ans)


# def D():

