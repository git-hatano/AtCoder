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
    a, b, c, x, y = map(int, input().split())
    ans = float('inf')
    #普通に買う
    ans = min(ans, a*x+b*y)
    #ABも使う
    z = min(x, y)*2
    ans = min(ans, c*z + a*(x-z//2) + b*(y-z//2))
    #ABのみ使う
    z = max(x, y)*2
    ans = min(ans, c*z)
    print(ans)


# def D():

