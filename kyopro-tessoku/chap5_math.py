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

n, r = map(int, input().split())
mod = 10**9+7
#答えnCrを求める
print(combination(n, r, mod))

