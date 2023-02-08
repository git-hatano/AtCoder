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
    a = list(map(int, input().split()))
    mean = sum(a)//n
    ans = 10**9
    for m in [mean, mean+1]:
        tmp = 0
        for i in range(n):
            tmp += (a[i]-m)**2
        ans = min(ans, tmp)
    print(ans)


# def D():

