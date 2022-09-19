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
    n, a, x, y = map(int, input().split())
    ans = 0
    if n<a:
        ans += n*x
    else:
        ans += a*x
        ans += (n-a)*y
    print(ans)


def B():
    n = int(input())
    s = list(input()) 

    for i, x in enumerate(s):
        if x=="1":
            break

    if i%2==0:
        print("Takahashi")
    else:
        print("Aoki")


def C_TLE():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    from collections import deque
    x = deque(c[:k])
    ans = len(set(x))

    for i in range(n-k):
        x.append(c[i+k])
        x.popleft()
        ans = max(ans, len(set(x)))

    print(ans)


"""
尺取法
差分だけを管理することで再計算を省ける
"""
def C():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    from collections import Counter
    counter = Counter(c[:k])
    ans = len(counter)

    for i in range(k, n):
        left = c[i-k]
        right = c[i]
        counter[left] -= 1
        counter[right] += 1
        
        if counter[left]==0:
            del counter[left]
        ans = max(ans, len(counter))

    print(ans)


# def D():

