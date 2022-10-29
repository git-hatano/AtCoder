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
    s = input()

    if s[-1]=="s":
        s += "es"
    else:
        s += "s"
    print(s)


def B():
    n = int(input())
    cnt = 0
    ans = False
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1==d2:
            cnt += 1
        else:
            cnt = 0
        if cnt==3:
            ans = True
            break
    print("Yes" if ans else "No")


def C():
    n = int(input())
    ans = 0

    for a in range(1, n):
        ans += (n-1)//a
    print(ans)


# def D():

