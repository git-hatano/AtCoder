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
    n, a, b = map(int, input().split())
    ans = n-a+b
    print(ans)


def B():
    import math
    n = int(input())
    xs = list(map(int, input().split()))

    m = sum([abs(x) for x in xs])
    u = math.sqrt(sum([abs(x)**2 for x in xs]))
    t = max([abs(x) for x in xs])

    print(m)
    print(u)
    print(t)


def C_TLE():
    n = int(input())
    for i in range(1, n//2+1):
        if n%i==0:
            print(i)
    print(n)


def C():
    n = int(input())
    nums = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            nums.append(i)
            nums.append(n//i)

    nums = list(set(nums)) #n=9=3*3 のような重複を消す
    nums = sorted(nums)

    for i in nums:
        print(i)


def D():
    x, y, a, b = map(int, input().split())
    ans = 0
    #過去問ジムに行けるだけ行く
    while True:
        if x*a >= y:
            break
        if x*a > x+b: # if x*a > b: #ここの条件怪しかったかも
            break
        x *= a
        ans += 1
    #残りの分で行けるだけAtCoderジムに行く  
    cnt_b = (y-x)//b
    x += b*cnt_b
    ans += cnt_b
    if x >= y:
        x -= b
        ans -= 1
    print(ans)
