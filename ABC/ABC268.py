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
print("Yes" if ans else "No")
'''

def A():
    a = list(map(int, input().split()))
    print(len(set(a)))

def B():
    s = input()
    t = input()

    ans = True
    if len(t)<len(s):
        ans = False
    else:
        for i in range(len(s)):
            if s[i]!=t[i]:
                ans = False
                break
            
    print("Yes" if ans else "No")


def C_TLE():
    n = int(input())
    p = list(map(int, input().split()))

    goods = []
    for i in range(n):
        goods.append([(i-1)%n, i, (i+1)%n])

    ans = 0
    for i in range(n):
        tmp = []
        for j in range(i, i+n):
            tmp.append(p[j%n])
        
        cnt = 0
        for i in range(n):
            if tmp[i] in goods[i]:
                cnt += 1
        ans = max(ans, cnt)

    print(ans)


"""
n回転試して、毎回n人のうち何人喜ぶかを確認すると、o(n**2)になってしまう

喜ぶ条件は決まっていて、そこから人iが喜ぶまでに必要な回転数がわかるので、
回転数ごとに喜ぶ人数を数えると、o(3*n) -> o(n) でいける
"""
def C():
    n = int(input())
    p = list(map(int, input().split()))

    # j回転したときに喜ぶ人数
    cnt = [0]*n

    for i in range(n):
        # 料理p[i]が、人p[i]の前に移動するまでの回転量
        j = (p[i] -i)%n
        
        # 人p[i]が喜ぶ置かれ方
        # 料理p[i]が、人(p[i]-1)%n, 人p[i], 人(p[i]+1)%n,の前に来るとき
        # つまり、j or j±1回転すれば、人p[i]は喜ぶ
        for k in range(-1, 2):
            #k: -1, 0, 1
            cnt[(j+k)%n] += 1

    ans = max(cnt)
    print(ans)

