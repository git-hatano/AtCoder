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
    n = int(input())
    if n%2==0:
        ans = (n/2)/n
    else:
        ans = ((n-1)/2+1)/n
    print(ans)


def B():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i]>=k:
            ans += 1
    print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    a_i = []
    for i in range(n):
        a_i.append([a[i], i])

    a_i.sort()
    ans = []
    for i in range(n):
        ans.append(a_i[i][1])
    ans = " ".join([str(x+1) for x in ans])
    print(ans)


# def D():

