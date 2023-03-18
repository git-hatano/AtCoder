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
    a = list(map(int, input().split()))
    #偶数、奇数の個数をカウント
    odd = 0
    even = 0
    for i in range(3):
        if a[i]%2==0:
            even += 1
        else:
            odd += 1

    ans = 0
    if odd==2:
        ans += 1
        for i in range(3):
            if a[i]%2==1:
                a[i] += 1
    elif even==2:
        ans += 1
        for i in range(3):
            if a[i]%2==0:
                a[i] += 1

    ma = max(a)
    for i in range(3):
        ans += (ma-a[i])//2
    print(ans)


# def D():

