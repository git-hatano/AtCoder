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
    n, k = map(int, input().split())
    ans = 1
    for i in range(n):
        if i==0:
            ans *= k
        else:
            ans *= k-1
    print(ans)


# def C():



# def D():

