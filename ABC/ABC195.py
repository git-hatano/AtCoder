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
    m, h = map(int, input().split())
    ans = (h%m==0)
    print("Yes" if ans else "No")


def B_TLE():
    a, b, w = map(int, input().split())
    w *= 1000
    cnt = []
    for i in range(w//a+1):
        for j in range(w//b+1):
            tmp_w = a*i + b*j
            if tmp_w == w:
                cnt.append(i+j)
            elif a < w - tmp_w < b:
                cnt.append(i+j+1)
            elif tmp_w > w:
                break

    if len(cnt)==0:
        print("UNSATISFIABLE")
    else:
        print(min(cnt), max(cnt))


def B_ans():
    a, b, w = map(int, input().split())
    m = 10**9
    M = 0
    for n in range(1, 10**6+1):
        if a*n <= 1000*w <= b*n:
            m = min(m, n)
            M = max(M, n)

    if M==0:
        print("UNSATISFIABLE")
    else:
        print(m, M)


def C():
    n = int(input())
    ans = 0
    for i in range(3, 15+1, 3):
        if 10**i <= n:
            ans += n - (10**i -1)
    print(ans)


# def D():

