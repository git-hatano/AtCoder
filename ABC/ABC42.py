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
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d = set(d)
    for i in range(n, 10**5+1):
        si = str(i)
        ok = True
        for c in si:
            c = int(c)
            if c in d:
                ok = False
                break
        if ok:
            ans = i 
            break
    print(ans)


# def D():

