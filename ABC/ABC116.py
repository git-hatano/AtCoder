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
    h = list(map(int, input().split()))
    h = [0] +h
    d = []
    for i in range(n):
        d.append(h[i+1]-h[i])

    ans = 0
    for i in range(n):
        if d[i]>0:
            ans += d[i]
    print(ans)


# def D():
