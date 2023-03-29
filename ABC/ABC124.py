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
    ans = 0
    for i in range(2):
        if a>b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1
    print(ans)


def B():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 1
    m = h[0]
    for i in range(1, n):
        if h[i] >= m:
            ans += 1
            m = h[i]
    print(ans)


def C():
    s = input()
    n = len(s)
    ans = 10**6

    for i in range(2):
        t = []
        for j in range(n):
            t.append(str((i+j)%2))
        cnt = 0
        t = "".join(t)
        for j in range(n):
            if s[j]!=t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)


# def D():
# from collections import defaultdict
# n, k = map(int, input().split())
# s = [int(x) for x in input()]

# a = [0]*(n+1)
# for i in range(n):
#     if s[i]==0:
#         a[i+1] = a[i]+1

# b = [0]*(n+1)
# for i in reversed(range(n+1)):
#     if i==n and a[i]>0:
#         b[i] = a[i]
# print()


def D_ans_TLE():
    n, k = map(int, input().split())
    s = [int(x) for x in input()]
    nums = []
    now = 1 #今見てる数
    cnt = 0 #nowがいくつ並ぶか
    for i in range(n):
        if s[i]==now:
            cnt += 1
        else:
            nums.append(cnt)
            now = 1-now #0/1を切り替える
            cnt = 1
    if cnt>0:
        nums.append(cnt)
    #1-0-1-0-1みたいな配列が欲しい
    #1-0-1-0みたいに終わってたら、適当に1つ加える
    nums.append(0)

    add = 2*k+1
    ans = 0
    for i in range(0, len(nums), 2):#1-0-1-0-1..の1から始めるので偶数番目だけを見る
        tmp = 0
        left = i
        right = min(i+add, len(nums))
        for j in range(left, right):
            tmp += nums[j]
        ans = max(ans, tmp)
    print(ans)


"""
尺取法
"""
def D_ans():
    n, k = map(int, input().split())
    s = [int(x) for x in input()]
    nums = []
    now = 1 #今見てる数
    cnt = 0 #nowがいくつ並ぶか
    for i in range(n):
        if s[i]==now:
            cnt += 1
        else:
            nums.append(cnt)
            now = 1-now #0/1を切り替える
            cnt = 1
    if cnt>0:
        nums.append(cnt)
    #1-0-1-0-1みたいな配列が欲しい
    #1-0-1-0みたいに終わってたら、適当に1つ加える
    nums.append(0)

    add = 2*k+1
    ans = 0
    left = 0
    right = 0
    tmp = 0 #[left, right)のsum
    #1-0-1-0-1..の1から始めるので偶数番目だけを見る
    for i in range(0, len(nums), 2):
        nextleft = i
        nextright = min(i+add, len(nums))
        #左端を移動させる
        while nextleft>left:
            tmp -= nums[left]
            left += 1
        #右端を移動させる
        while nextright>right:
            tmp += nums[right]
            right += 1
        ans = max(ans, tmp)
    print(ans)
