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
    x = list(map(int, input().split()))
    x.sort()

    #各頂点間の距離
    dist = []
    for i in range(m-1):
        dist.append(x[i+1] - x[i])
    dist.sort()

    ans = 0
    cnt = max(0, m-n)
    for i in range(cnt):
        #距離が小さい区間を足す＝大きい区間は通らないようにできる
        ans += dist[i]
    print(ans)


# def D():

