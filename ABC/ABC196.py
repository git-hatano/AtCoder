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
    print(b-c)


def B():
    x = input()
    if "." in x:
        x = int(x.split(".")[0])
    else:
        x = int(x)
    print(x)


def C():
    n = input()
    len_n = len(n)
    n = int(n)

    ans = 0
    if len_n>=2:
        l = len_n//2
        for i in range(1, 10**l):
            tmp = int(f"{i}{i}")
            if tmp<=n:
                ans += 1
            else:
                break
    print(ans)


# def D():

