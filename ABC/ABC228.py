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
ans = True
print("Yes" if ans else "No")
'''

def A():
    s, t, x = map(int, input().split())
    x += 0.5

    ans = False
    if s<=x and x<=t:
        ans = True
    elif s>t:
        if (s<=x and x<24) or (0<=x and x<=t):
            ans = True
        
    print("Yes" if ans else "No")


def B():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    x -= 1
    a = [x-1 for x in a]
    arr = [0]*n

    for i in range(n):
        if arr[x]==0:
            arr[x] = 1
            x = a[x]
        else:
            break

    print(sum(arr))


def C():
    n, k = map(int, input().split())
    # 1ならYes
    res = [0]*n

    # 生徒i: 3日目までの合計
    p = {}
    for i in range(n):
        p[i] = sum(list(map(int, input().split())))

    # 3日目までの合計でソート
    p_sorted = sorted(p.items(), key=lambda x:x[1], reverse=True)

    #上位k人は入賞
    for i in range(k):
        res[p_sorted[i][0]] = 1
        
    #上位k人目の点数
    min_p = p_sorted[i][1]
    #k人目の人から300点以内なら入賞できる可能性はあるはず
    for i in range(k, n):
        if min_p - p_sorted[i][1] <= 300:
            res[p_sorted[i][0]] = 1

    #output
    for i in range(n):
        if res[i]==1:
            print("Yes")
        else:
            print("No")

# def D():

