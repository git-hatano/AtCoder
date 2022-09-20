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
    if b-a>0:
        print(b-a+1)
    else:
        print(0)


def B():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    price = 0
    for i in range(n):
        if (i+1)%2==0:
            price += (a[i]-1)
        else:
            price += a[i]

    if x>=price:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def C_WA():
    n = int(input())
    c = list(map(int, input().split()))
    mod = (10**9)+7

    ans = 1
    for i in range(n):
        ans = ans * (c[i]-i)

    ans %= mod
    print(ans)


n = int(input())
c = list(map(int, input().split()))
mod = (10**9)+7

#昇順に並び替える必要
c = sorted(c)

ans = 1
for i in range(n):
    #掛け算する際にmodを使う必要
    ans = ans * max(0, c[i]-i) % mod 
print(ans)


# def D():

