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


"""
(a+b)%K=0になるためには、
a%K=b%K=c%K=0
a%K=b%K=c%K=K/2 : Kが偶数のみ
"""
def C_ans():
    n, k = map(int, input().split())
    ans = 0
    #a%K=b%K=c%K=0
    cnt = 0
    for i in range(1, n+1):
        if i%k==0:
            cnt += 1
    ans = cnt*cnt*cnt
    #a%K=b%K=c%K=K/2
    if k%2==0:
        cnt = 0
        for i in range(1, n+1):
            if i%k==k//2:
                cnt += 1
        ans += cnt*cnt*cnt
    print(ans)


# def D():

