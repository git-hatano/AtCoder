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

from asyncio import ensure_future


def A():
    n = int(input())
    n = hex(n)[2:].upper()
    n= n.zfill(2)
    print(n)


def B():
    n, q= map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    for i in range(q):
        s, t = map(int, input().split())
        s -= 1
        print(l[s][t])


"""
WAが7残る
"""
def C_WA():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    ans = 0
    if n==1 and a[0]==1:
        ans += 1
    elif n>1:
        left = 0
        right = n-1
        for i in range(n):
            if (i+1)==a[left]:
                ans += 1
                left += 1
            else:
                if right+1-left-2>=0:
                    ans += 1
                    right -= 2
            if left>=right:
                if left==right and a[left]==(ans+1):
                    ans += 1
                break
    print(ans)


"""
シミュレーション（考えるのは簡単、実装が難しくなることも。多分自分のパターンはこっちだった）、
2分探索（テクニックを当てはめて解くパターン）、
問題文の読替え(問題の本質を捉える考察が必要、実装は楽になることも)
など、いくつかのパターンで解ける
"""
def C():
    n = int(input())
    a = list(map(int, input().split()))
    st = set(a)

    ans = 0
    s = 0
    for i in range(1, n+1):
        # aの中に含まれていたらコスト1で読める
        if i in st:
            s += 1
        # aの中に含まれていなかったらコスト2で読める
        else:
            s += 2
        # コストがn以下であれば、i巻目までは読める
        if s > n:
            break
        ans = i
    print(ans)


# def D():

