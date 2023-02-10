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
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    mod = 10**9 +7
    ok = True
    if n%2==1:
        for i in range(n):
            if i==0 and i in counter and counter[i]==1:
                continue
            elif i%2==0 and i in counter and counter[i]==2:
                continue
            elif i%2==1 and i not in counter:
                continue
            ok = False
            break
    elif n%2==0:
        for i in range(n):
            if i%2==1 and i in counter and counter[i]==2:
                continue
            elif i%2==0 and i not in counter:
                continue
            ok = False
            break
    if ok:
        ans = 1
        for i in range(n//2):
            ans *= 2
            ans %= mod
    else:
        ans = 0
    print(ans)


# def D():

