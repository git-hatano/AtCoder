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
    ans = 0
    ans += min(n, m//2) #先にsを使い切る
    n -= ans
    m -= 2*ans
    if m>=4: #残ったcでsccを作る
        ans += m//4
    print(ans)


# def D():

