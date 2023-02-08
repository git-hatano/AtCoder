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
全bit探索
"""
def C():
    s = input()
    n = len(s)
    res = []
    for i in range(2 ** (n-1)):#bitのパターン
        cur = 0 # 現在の合計値
        num = ""
        for j in range(n):
            wari = (2 ** j)
            num += s[j]
            if (i // wari) % 2 == 1:#bitが1の要素を抽出して計算
                cur += int(num)
                num = ""
        if num!="":
            cur += int(num)
        res.append(cur)
    ans = sum(res)
    print(ans)


# def D():

