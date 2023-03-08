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

# def A():



def B():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(input()))
    b = []
    for i in range(m):
        b.append(list(input()))

    ans = False
    for i in range(n-m+1):
        for j in range(n-m+1):
            ok = True
            for k in range(m):
                for l in range(m):
                    if a[i+k][j+l]!=b[k][l]:
                        ok = False
            if ok:
                ans = True
    print("Yes" if ans else "No")


# def C():



# def D():

