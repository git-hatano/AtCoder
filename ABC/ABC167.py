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
ans = False
print("Yes" if ans else "No")
'''

def A():
    s = input()
    t = input()
    ans = (s==t[:-1])
    print("Yes" if ans else "No")


def B():
    a, b, c, k = map(int, input().split())
    ans = 0
    if k>0 and a>0:
        n = min(k, a)
        ans += n
        k -= n

    if k>0 and b>0:
        n = min(k, b)
        k -= n

    if k>0 and c>0:
        n = min(k, c)
        ans -= n
        k -= n

    print(ans)


"""
12!を全探索は流石に間に合わない
"""
def C_TLE():
    from itertools import permutations
    n, m, x = map(int, input().split())
    ca = [list(map(int, input().split())) for _ in range(n)]
    cost = 10**9

    for p in permutations(ca, n):
        cost_tmp = 0
        a = [0]*m
        for l in p:
            #ある本を読んだときのコストと理解度を加算
            cost_tmp += l[0]
            for i in range(m):
                a[i] += l[i+1]
            #理解度がx以上になったか確認
            flag = True
            for i in range(m):
                if x > a[i]:
                    flag = False
                    break
            #理解度がx以上になっていればコストを更新, 次の組み合わせへ
            if flag:
                cost = min(cost, cost_tmp)
                break

    if cost==10**9:
        print(-1)
    else:
        print(cost)


"""
この問題の計算量なら全bit探索で間に合う
O(2**n)
"""
def C():
    n, m, x = map(int, input().split())
    ca = [list(map(int, input().split())) for _ in range(n)]
    cost = 10**9

    #どの本を読むかを全bit探索
    for bit in range(2**n):
        bit = bin(bit)[2:].zfill(n)
        cost_tmp = 0
        a = [0]*m
        #読んだ本のコストと理解度を集計
        for i, b in enumerate(bit):
            if b=="1":
                cost_tmp += ca[i][0]
                for j in range(m):
                    a[j] += ca[i][j+1]
        #理解度がx以上になったか確認
        flag = True
        for i in range(m):
            if x > a[i]:
                flag = False
                break
        #理解度がx以上になっていればコストを更新
        if flag:
            cost = min(cost, cost_tmp)

    if cost==10**9:
        print(-1)
    else:
        print(cost)


# def D():

