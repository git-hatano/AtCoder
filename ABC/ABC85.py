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



# def C():



def D():
    n, h = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    data.sort(key=lambda x: x[0], reverse=True)
    max_a = data[0][0]

    #max_aより大きなbは使い切る
    data.sort(key=lambda x: x[1], reverse=True)###
    for i in range(n):
        b = data[i][1]
        if h>0 and b>=max_a:
            ans += 1
            h -= b
    #残りはmax_aで殴る
    if h>0:
        ans += h//max_a
        if h%max_a!=0:
            ans += 1
    print(ans)
