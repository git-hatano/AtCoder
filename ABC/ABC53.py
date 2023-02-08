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
    ans = 0
    ans += n//11 *2 #ひたすら5,6を繰り返す
    n %= 11
    ans += n//6
    n %= 6
    if n>0:
        ans += 1
    print(ans)


# def D():

