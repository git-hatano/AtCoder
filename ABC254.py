'''
C問題まで考える

# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]
'''
def test1():
    # 文字列を受け取る場合
    S = input() 
    print(S[-2:])

def test2():
    # 1つの整数を入力
    N = int(input())
    arr = []

    for i in range(N):
        buf = [0]*(i+1)

        for j in range(i+1):
            if j==0 or j==i:
                buf[j] = 1
            else:
                buf[j] = arr[i-1][j-1] + arr[i-1][j]

        arr.append(buf)
        print(" ".join([str(x) for x in arr[i]]))
    

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


N, K = map(int, input().split())
a = list(map(int, input().split()))
b = [[] for _ in range(K)]

for i in range(N):
    b[i%K].append(a[i])

for i in range(K):
    # b[i] = sorted(b[i])
    # b[i].sort()
    b[i] = merge_sort(b[i])

# a = sorted(a)
# a.sort()
a = merge_sort(a)

na = []
for i in range(N):
    na.append(b[i%K][0])
    b[i%K].pop(0)

if a == na:
    print("Yes")
else:
    print("No")


