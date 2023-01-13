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
    n, x = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(x)
    xs.sort()

    ans = 0
    for i in range(n):
        d = xs[i+1] - xs[i]
        ans = math.gcd(ans, d)
    print(ans)


# def D():

