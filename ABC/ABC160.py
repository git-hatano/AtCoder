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

def A():
    s = input()
    print("Yes" if (s[2]==s[3] and s[4]==s[5]) else "No")


def B():
    x = int(input())
    ans = 0
    ans += 1000*(x//500)
    x %= 500
    ans += 5*(x//5)
    print(ans)


"""
全然思いつかん...深読みしすぎた
円環の扱いを問われた問題
"""
def C_ans():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    ds = []
    #家同士の距離を求める
    for i in range(n-1):
        d = a[i+1] - a[i]
        ds.append(d)

    #円環の頂点をまたぐパターンの距離
    d = (k-a[-1]) + a[0]
    ds.append(d)

    #一番長い間隔を通らないルートが答え
    ans = k - max(ds)
    print(ans)


# def D():

