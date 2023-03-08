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



def B():
    a, b, x = map(int, input().split())
    cnt_a = a//x
    cnt_b = b//x
    ans = cnt_b-cnt_a
    if a%x==0:
        ans += 1
    print(ans)


def C_WA():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i]+a[i+1]>x:
            y = a[i+1]+a[i] -x
            ans += y
            if a[i]>a[i+1]: #ここの分岐がいらなかった
                a[i] -= y
            else:
                a[i+1] -= y
    print(ans)


"""
貪欲法的な考え方
"""
def C_ans():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    if a[0]>x: #最初にa[0]をx以下にしておく
        ans += a[0]-x
        a[0] = x

    for i in range(n-1):
        if a[i]+a[i+1]>x:
            y = a[i+1]+a[i] -x
            ans += y
            a[i+1] -= y #i+1の方が次の計算も使われるのでこっちを減らす
    print(ans)


# def D():

