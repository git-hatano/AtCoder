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
    a, b = map(int, input().split())
    ans = (1-b/a)*100
    print(ans)


def B():
    n = int(input())
    ans = 10**10
    for i in range(n):
        a, p, x = map(int, input().split())
        if x-a > 0:
            ans = min(ans, p)
    if ans==10**10:
        print(-1)
    else:
        print(ans)


def C():
    import math
    n = int(input())

    pow_list = set([])
    for a in range(2, int(math.sqrt(n))+1):
        for b in range(2, int(math.log2(n))+1):
            if a**b <=n:
                pow_list.add(a**b)
            else:
                break

    ans = n - len(pow_list)
    print(ans)


# def D():

