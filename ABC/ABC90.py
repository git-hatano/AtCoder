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
    n, m = map(int, input().split())
    if n>m:
        n, m = m, n
    ans = 0
    if n==1:
        if m==1:
            ans = 1
        else:
            ans = m-2
    else:
        ans = (n-2)*(m-2) #内側が全て裏になる
    print(ans)


# def D():

