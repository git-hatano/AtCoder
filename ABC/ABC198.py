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
    n = int(input())
    if n%2==1:
        ans = (n//2)*2
    else:
        ans = ((n-1)//2)*2 +1
    print(ans)


def B():
    s = input()
    ans = False
    cnt_zero = 0
    for c in s[::-1]:
        if c=="0":
            cnt_zero += 1
        else:
            break
    new_s = "0"*cnt_zero + s

    if new_s==new_s[::-1]:
        ans = True
    print("Yes" if ans else "No")


def C():
    import math
    r, x, y = map(int, input().split())
    dist = math.sqrt(x**2 + y**2)
    ans = 0

    if dist>=r:
        ans += dist//r
        if dist%r>0:
            ans += 1
    else:
        ans = 2

    print(int(ans))


# def D():

