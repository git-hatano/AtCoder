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
    n = int(input())
    if n%2==0:
        ans = (n/2)/n
    else:
        ans = ((n-1)/2+1)/n
    print(ans)


def B():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i]>=k:
            ans += 1
    print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    a_i = []
    for i in range(n):
        a_i.append([a[i], i])

    a_i.sort()
    ans = []
    for i in range(n):
        ans.append(a_i[i][1])
    ans = " ".join([str(x+1) for x in ans])
    print(ans)


def D():
    import math
    def is_prime(n):
        if n == 1: 
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def divisor_list(num):
        divisors = []
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                divisors.append(i)  
                if i**2 == num:
                    continue
                divisors.append(int(num/i))
        return sorted(divisors)

    a, b = map(int, input().split())
    #それぞれの公約数を計算
    da = divisor_list(a)
    db = divisor_list(b)
    #共通の公約数を集約
    d = set(da) & set(db)
    #残った公約数が素数か判定
    s = set()
    s.add(1)
    for i in d:
        if is_prime(i):#公約数が意外と少ないから計算量が足りる
            s.add(i)
    ans = len(s)
    print(ans)
