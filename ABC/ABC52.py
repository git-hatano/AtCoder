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

# def A():



# def B():



"""
分かんないし、解説ないし分かんない
"""
def C_WA():
    import math
    def sieve_of_eratosthenes(n):
        prime = [True for i in range(n+1)]
        prime[0] = False
        prime[1] = False
        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, sqrt_n):
            if prime[i]:
                for j in range(2*i, n+1, i):
                    prime[j] = False
        return prime

    # 素数の列挙
    n = int(input())
    prime = sieve_of_eratosthenes(n)
    mod = 10**9 +7
    np = math.factorial(n)

    ans = 1
    for i in range(len(prime)):
        if prime[i]:
            ans *= np//i + 1
            ans %= mod
    print(ans)


# def D():

