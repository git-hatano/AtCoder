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
    from itertools import product
    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]

    ans = - float('inf')
    for bits in product([0, 1], repeat=10):
        # print(bits)
        if sum(bits)>0:
            tmp = 0
            for i in range(n):
                c = 0
                for j in range(10):
                    c += bits[j]*f[i][j]
                tmp += p[i][c]
            ans = max(ans, tmp)
    print(ans)


# def D():

