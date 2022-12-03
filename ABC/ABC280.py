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

def A():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(list(input()))
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j]=="#":
                ans +=1
    print(ans)


def B():
    n = int(input())
    s = list(map(int, input().split()))
    a = []
    for i in reversed(range(1, n)):
        a.append(s[i]-s[i-1])

    a.append(s[0])
    a = a[::-1]
    ans = " ".join([str(x) for x in a])
    print(ans)


def C():
    s = input() 
    t = input()
    ans = len(t)
    for i in range(len(s)):
        if s[i]!=t[i]:
            ans = i+1
            break
    print(ans)


"""
素数判定
素因数分解
"""
def D_TLE():
    import math
    def is_prime(n):
        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, sqrt_n+1):
            if n % i == 0:
                return False
        return True

    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])
        if temp!=1:
            arr.append([temp, 1])
        if arr==[]:
            arr.append([n, 1])
        return arr

    k = int(input())
    if is_prime(k):
        ans = k
    else:
        x = factorization(k)
        x.sort(reverse=True)
        n = x[0][0]
        tmp = math.factorial(n)
        if tmp%k != 0:
            while tmp%k != 0:
                n += 1
                tmp = math.factorial(n)
        ans = n
    print(ans)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

print(factorization(121))