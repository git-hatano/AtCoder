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
    t = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if t[i+1]-t[i]>=m:
            ans += m
        else:
            ans += t[i+1]-t[i]
    ans += m
    print(ans)


# def D():

