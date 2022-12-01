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

def A06():
    from itertools import accumulate
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] + list(accumulate(a))
    for j in range(q):
        l, r = map(int, input().split())
        ans = s[r] - s[l-1]
        print(ans)


def B06():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))

    s = [0] + list(accumulate(a))
    m = [0] + list(accumulate([x^1 for x in a]))

    q = int(input())
    for j in range(q):
        l, r = map(int, input().split())
        strike = s[r] - s[l-1]
        miss = m[r] - m[l-1]
        
        if strike > miss:
            print("win")
        elif miss > strike:
            print("lose")
        else:
            print("draw")


