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
print("Yes" if ans else "No")
'''

def A():
    n, k, a = map(int, input().split())
    for i in range(1, k):
        a += 1
        if a>n:
            a = 1
    print(a)


def B():
    n = int(input())
    s = list(map(int, input().split()))

    #ありうる面積を全探索
    max_s = 1000+1
    x = []
    for a in range(1, max_s):
        for b in range(1, max_s):
            t = 4*a*b + 3*a + 3*b
            if t <= 1000:
                x.append(t)
    x = set(x)
    ans = 0
    for i in range(n):
        if s[i] not in x:
            ans += 1
    print(ans)
            

"""
全探索ver
n回 for を回す時点でTLEになってしまう
"""
def C_TLE():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if a*b*c <= n:
                    ans += 1
    print(ans)


def C():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        if a*a*a>n:
            break
        
        for b in range(a, n+1):
            if a*b*b>n:
                break
            
            max_c = n//(a*b)
            ans += max_c -b +1

    print(ans)

# def D():

