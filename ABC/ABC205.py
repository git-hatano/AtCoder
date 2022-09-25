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
    ans = b/100*a
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    b = [x+1 for x in range(n)]

    ans = True
    for i in range(n):
        if a[i]!=b[i]:
            ans = False
            break
    print("Yes" if ans else "No")


def C():
    a, b, c = map(int, input().split())

    if c==0:
        a = 1
        b = 1
    elif c%2==0:
        if a<0:
            a *= -1
        if b<0:
            b *= -1

    if a<b:
        print("<")
    elif a>b:
        print(">")
    else:
        print("=")


# def D():

