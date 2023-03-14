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



def C_ans():
    n = int(input())
    c = [None]*(n-1)
    s = [None]*(n-1)
    f = [None]*(n-1)
    for i in range(n-1):
        c[i], s[i], f[i] = list(map(int, input().split()))

    #駅iからスタート
    for i in range(n):
        ans = 0 #駅iからゴールまでかかる時間
        #駅iからゴールまで移動をシミュレーション
        for j in range(i, n-1):
            ans = max(ans, s[j]) #駅jの開通式開始前の場合は、開通式開始時刻まで待つ
            d = ans-s[j] #駅jに到着して次の出発時刻までの待ち時間を求める
            if d%f[j]>0:
                d = f[j] - d%f[j]
            else:
                d = 0
            ans += d + c[j] #待ち時間と次のj+1駅への移動時間を記録
        print(ans)


# def D():

