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
    n, k = map(int, input().split())
    s = list(input())
    s[k-1] = s[k-1].lower()
    ans = "".join([str(x) for x in s])
    print(ans)


def B():
    s = input()
    s1 = int(s[:2])
    s2 = int(s[2:])
    ans = "NA"
    if 1<=s1<=12 and 1<=s2<=12:
        ans = "AMBIGUOUS"
    elif 1<=s1<=12:
        ans = "MMYY"
    elif 1<=s2<=12:
        ans = "YYMM"
    print(ans)


"""
小数問題でlogは使わない方が安全
"""
def C_WA():
    import math
    n, k = map(int, input().split())
    s = 0
    for i in reversed(range(1, n+1)):
        if n>=k:
            s += 1
        else:
            p = math.ceil(math.log2(k/i))
            s += 0.5**p
    ans = s/n
    print(ans)

"""
愚直に解けばAC
"""
def C_ans():
    n, k = map(int, input().split())
    ans = 0
    for i in reversed(range(1, n+1)):
        j = i
        q = 1/n
        while j<k:
            j *= 2
            q /= 2
        ans += q
    print(ans)


# def D():

