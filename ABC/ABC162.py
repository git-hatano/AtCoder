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
    if "7" in s:
        ans =True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i%3==0:
            continue
        elif i%5==0:
            continue
        else:
            ans += i
    print(ans)


def C():
    import math
    k = int(input())
    ans = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                ans += math.gcd(a, math.gcd(b, c))
    print(ans)


# def D():

