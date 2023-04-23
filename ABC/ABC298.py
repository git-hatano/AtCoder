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
    from collections import Counter
    n = int(input())
    s = list(input())
    counter = Counter(s)

    ans = False
    if counter["o"]>0 and counter["x"]==0:
        ans = True
    print("Yes" if ans else "No")


def rot(s):
    return list(zip(*s[::-1]))

def B():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    ans = False
    for i in range(4):
        ok = True
        for i in range(n):
            for j in range(n):
                if a[i][j]==1 and b[i][j]==0:
                    ok = False
        if ok:
            ans = True
            break
        else:
            a = rot(a)
    print("Yes" if ans else "No")


# def C():
from collections import defaultdict
n = int(input())
q = int(input())

boxes = defaultdict(list)
poses = defaultdict(set)
for i in range(q):
    query = list(map(int, input().split()))
    i = query[1]
    if query[0]==1:
        j = query[2]
        boxes[j].append(i)
        poses[i].add(j)
    elif query[0]==2:
        print(" ".join([str(x) for x in boxes[i]]))
    else:
        for p in poses[i]:
            print(" ".join([str(x) for x in boxes[p]]))


# def D():

