# def func(n):
#     if n==0:
#         return 0
#     else:
#         return n + func(n-1)


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m%n)

# print(gcd(51, 15)) # 3が出力される
# print(gcd(15, 51)) # 3が出力される


def fibo_recurve(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    return fibo_recurve(n-1) + fibo_recurve(n-2)

# print(fibo(6)) # 8が出力される


def fibo2():
    n = 6
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    print(f[n]) # 8が出力される


class Fib_memo:
    def __init__(self):
        self.fib_memo = {}

    def cal_fib(self, n):
        if n == 0:
            self.fib_memo[n] = 0
            return 0
        
        elif n == 1:
            self.fib_memo[n] = 1
            return 1

        #既に計算した項なら保存した情報を使う
        if n in self.fib_memo.keys():
            return self.fib_memo[n]

        self.fib_memo[n] = self.cal_fib(n-1) + self.cal_fib(n-2)
        return self.fib_memo[n]

# n = 6
# fib_memo = Fib_memo()
# ans = fib_memo.cal_fib(n)
# print(ans) # 8が出力される





def func(i, w, a):
    # ベースケース
    if i==0:
        if w==0:
            return True
        else:
            return False
    
    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        return True

    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        return True

    # どちらもFalseの場合
    return False

n = 4
w = 14
a = [3, 2, 6, 5]

if func(n, w, a):
    print("Yes")
else:
    print("No")

