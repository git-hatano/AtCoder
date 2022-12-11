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
    a, b = map(int, input().split())
    ans = max(a+b, a-b, a*b)
    print(ans)


def B():
    k, x = map(int, input().split())
    nums = [x]
    for i in range(1, k):
        nums.append(x+i)
        nums.append(x-i)
    nums.sort()
    ans = " ".join([str(x) for x in nums])
    print(ans)


def C():
    from collections import Counter
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = int(input())
    s = []
    for i in range(n):
        x = list(input())
        x.sort()
        s.append("".join(x))

    counter = Counter(s)
    ans = 0
    for key in counter:
        if counter[key]>=2:
            ans += combinations_count(counter[key], 2)

    print(ans)


# def D():

