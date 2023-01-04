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
    a, b = map(int, input().split())
    if a-2*b < 0:
        print(0)
    else:
        print(a-2*b)


def B():
    from itertools import combinations
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for c in combinations(d, 2):
        ans += c[0]*c[1]
    print(ans)


def C():
    n = int(input())
    s = input()
    ans = []
    for i in range(n):
        if i==0:
            ans.append(s[i])
        elif ans[-1] != s[i]:
            ans.append(s[i])
    print(len(ans))

"""
3重ループは間に合わない
"""
def D_TLE():
    from itertools import combinations
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for c in combinations(l, 3):
        if c[0]<c[1]+c[2] and c[1]<c[2]+c[0] and c[2]<c[0]+c[1]:
            ans += 1
    print(ans)


"""
2重ループ+残りの辺を二分探索まで思いついたのは良かった
が、実装できなかった
https://drken1215.hatenablog.com/entry/2019/10/20/032700
"""
def D_ans():
    from bisect import bisect_left
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            k = bisect_left(l, l[i]+l[j])#短い2辺を固定
            ans += max(k-(j+1), 0)
            
    print(ans)
