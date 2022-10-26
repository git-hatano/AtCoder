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
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = a*d -b*c
    print(ans)


def B():
    n, x = map(int, input().split())
    s = input() 

    for c in s:
        if c=="o":
            x += 1
        elif c=="x" and x>0:
            x -= 1
    print(x)


# def C():



# def D():

