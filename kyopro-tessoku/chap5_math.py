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

def A26():
    def prime(n):
        import math
        if n==1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

    q = int(input())
    for i in range(q):
        x = int(input())
        print("Yes" if prime(x) else "No")


"""
エラトステネスのふるい
n以下の素数を高速に判定できる
"""
def B27():
    import math
    n = int(input())
    delete = [False]*(n+1)

    for i in range(2, int(math.sqrt(n))+1):
        if delete[i]==True:
            continue
        for j in range(2*i, n+1, i):
            delete[j] = True

    for i in range(2, n+1):
        if delete[i]==False:
            print(i)


"""
最大公約数
ユーグリッドの互助法
"""
def A27():
    def gcd(x, y):
        while x>=1 and y>=1:
            if x>y:
                x = x%y
            else:
                y = y%x
        if x!=0:
            return x
        else:
            return y

    a, b = map(int, input().split())
    print(gcd(a, b))

"""
最小公倍数
"""
def B27():
    def gcd(x, y):
        while x>=1 and y>=1:
            if x>y:
                x = x%y
            else:
                y = y%x
        if x!=0:
            return x
        else:
            return y

    def lcm(x, y):
        return x*y // gcd(x,y)

    a, b = map(int, input().split())
    print(lcm(a, b))


"""
余りの扱い方
"""
def A28():
    n = int(input())
    mod = 10**4
    ans = 0
    for i in range(n):
        t, a = input().split()
        a = int(a)
        
        if t=="+":
            ans += a
        elif t=="-":
            ans -= a
        else:
            ans *= a
        
        if ans<0:
            ans += mod
        ans %= mod
        print(ans)


def B28():
    n = int(input())
    mod = 10**9 +7

    a = [0]*(n+1)
    a[1] = 1
    a[2] = 1
    for i in range(3, n+1):
        a[i] = (a[i-1] + a[i-2])%mod
    print(a[n])


"""
余り対応ありの累乗計算
全bit探索の参考にもなる
"""
def A29():#B29
    def power(a, b, m):
        p = a
        ans = 1
        for i in range(30):#bの範囲で決まる
            wari = 2**i
            if (b//wari)%2 == 1:
                ans = (ans*p)%m 
            p = (p*p)%m
        return ans

    a, b = map(int, input().split())
    mod = 10**9+7
    print(power(a, b, mod))

def power(a, b, m):
    p = a
    ans = 1
    for i in range(30):#bの範囲で決まる
        wari = 2**i
        if (b//wari)%2 == 1:
            ans = (ans*p)%m 
        p = (p*p)%m
    return ans

def division(a, b, m):
    return (a * power(b, m-2, m))%m

def combination(n, r, m):
    #分子a
    a = 1
    for i in range(1, n+1):
        a = (a*i)%m
    #分母b
    b = 1
    for i in range(1, r+1):
        b = (b*i)%m
    for i in range(1, n-r+1):
        b = (b*i)%m
    return division(a, b, m)


def A30():
    n, r = map(int, input().split())
    mod = 10**9+7
    #答えnCrを求める
    print(combination(n, r, mod))


def B30():
    h, w = map(int, input().split())
    mod = 10**9+7
    print(combination(h+w-2, h-1, mod))


def A31():
    n = int(input())
    a = n//3
    b = n//5
    c = n//(3*5)
    ans = a+b-c
    print(ans)


def B31():
    n = int(input())

    a = n//3
    b = n//5
    c = n//7

    ab = n//15
    bc = n//35
    ca = n//21
    abc = n//(3*5*7)

    ans = a+b+c-ab-bc-ca+abc
    print(ans)


def A32():
    n, a, b = map(int, input().split())
    #dp[i]=Trueが勝ちの状態
    dp = [None]*(n+1)

    for i in range(n+1):
        if i>=a and dp[i-a]==False:
            dp[i] = True #勝ちの状態
        elif i>=b and dp[i-b]==False:
            dp[i] = True #負けの状態
        else:
            dp[i] = False

    if dp[n]:
        print("First")
    else:
        print("Second")


def B32():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [None]*(n+1)
    for i in range(n+1):
        for j in range(k):
            if i<a[j] and dp[i]==None:
                dp[i] = False
            elif i>=a[j] and dp[i-a[j]]==False:
                dp[i] = True
            elif i>=a[j] and dp[i]==None:
                dp[i] = False

    if dp[n]:
        print("First")
    else:
        print("Second")


"""
ニム和
"""
def A33():
    n = int(input())
    a = list(map(int, input().split()))

    xor_sum = a[0]
    for i in range(1, n):
        xor_sum ^= a[i]

    if xor_sum != 0:#先手必勝
        print("First")
    elif xor_sum == 0:#後手必勝
        print("Second")


def B33():
    n, h, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    xor_sum = 0
    for i in range(n):
        xor_sum ^= a[i]-1

    for i in range(n):
        xor_sum ^= b[i]-1

    if xor_sum != 0:#先手必勝
        print("First")
    elif xor_sum == 0:#後手必勝
        print("Second")
