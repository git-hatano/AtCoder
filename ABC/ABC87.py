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



# def B():



def C():
    n = int(input())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))

    su = [[0]*(n) for i in range(2)]
    su[0][0] = a[0][0]
    for j in range(1, n):
        su[0][j] = su[0][j-1] + a[0][j]

    for j in range(n):
        if j==0:
            su[1][j] = su[0][j] + a[1][j]
        else:
            su[1][j] = max(su[0][j], su[1][j-1]) + a[1][j]
    print(su[1][n-1])


# def D():

