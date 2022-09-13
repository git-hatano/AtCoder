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
    s = input()
    word = "Hello,World!"

    if s==word:
        print("AC")
    else:
        print("WA")


"""
ライブラリを使ったときに、誤差が出るような入力が含まれているのでWAになる
"""
def B_WA():
    n = int(input())

    import math
    k = math.log2(n)
    print(int(k))

def B():
    k = 0
    while n>0:
        k += 1
        n = n//2
    print(k-1)


def C():
    s, k = input().split()
    k = int(k)

    x = []
    from itertools import permutations
    for p in permutations(s, len(s)):
        # print("".join(p))
        x.append("".join(p))
        
    x = sorted(list(set(x)))
    print(x[k-1])

# def D():

