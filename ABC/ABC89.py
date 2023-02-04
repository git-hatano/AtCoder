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
    from collections import defaultdict
    from itertools import combinations
    n = int(input())
    s = [input() for i in range(n)]
    d = defaultdict(int)
    for c in s:
        if c[0] in ["M", "A", "R", "C", "H"]:
            d[c[0]] += 1

    ans = 0
    if len(d.keys())>=3:
        for c in combinations(d.keys(), 3):
            ans += d[c[0]] * d[c[1]] * d[c[2]]
    print(ans)


# def D():

