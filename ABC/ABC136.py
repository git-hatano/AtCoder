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
    a, b, c = map(int, input().split())
    ans = max(0, c-(a-b))
    print(ans)


def B():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i))%2 == 1:
            ans += 1
    print(ans)


def C():
    n = int(input())
    h = list(map(int, input().split()))
    m = h[0]
    for i in range(1, n):
        if m < h[i]:
            h[i] -= 1
            m = max(m, h[i])
    
    ans = True
    for i in range(n-1):
        if h[i] > h[i+1]:
            ans = False
    print("Yes" if ans else "No")


# def D():

