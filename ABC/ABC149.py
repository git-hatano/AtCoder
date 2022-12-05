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
    s, t = input().split()
    print(t+s)


def B():
    a, b, k = map(int, input().split())
    ans_a = a
    ans_b = b
    if k>0:
        ans_a = max(0, a-k)
        k -= (a - ans_a)
    if k>0:
        ans_b =  max(0, b-k)
    print(ans_a, ans_b)


"""
min() で考えた方がコードがすっきり
"""
def B_ans():
    a, b, k = map(int, input().split())
    eat = min(a, k)
    a -= eat
    k -= eat

    eat = min(b, k)
    b -= eat
    k -= eat
    print(a, b)


def C():
    import math
    def is_prime(n):
        if n == 1: 
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    x = int(input())
    ans = -1
    for i in range(x, 10**6):
        if is_prime(i):
            ans = i
            break
    print(ans)


# def D():

