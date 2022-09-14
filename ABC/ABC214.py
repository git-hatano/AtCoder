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
    n = int(input())

    if 1<=n and n<=125:
        ans = 4
    elif 126<=n and n<=211:
        ans = 6
    else: 
        ans = 8
    print(ans)


def B():
    s, t = map(int, input().split())

    ans = 0
    n = 100+1
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a+b+c<=s and a*b*c<=t:
                    ans += 1
    print(ans)


def C_WA():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    #高橋にもらうのが早い順
    ti = []
    for i in range(n):
        ti.append([t[i], i])
    ti = sorted(ti)

    #初めてもらう時間
    time = [float("inf")]*n
    for i in range(n):
        if i==0:
            time[ti[i][1]] = t[ti[i][1]]
            time[(ti[i][1]+1)%n] = time[ti[i][1]] + s[ti[i][1]]
        else:
            time[ti[i][1]] = min(time[ti[i][1]], t[ti[i][1]], time[(ti[i][1]-1)%n]+s[(ti[i][1]-1)%n])
            time[(ti[i][1]+1)%n] = min(time[(ti[i][1]+1)%n], time[ti[i][1]]+s[ti[i][1]])
    #output
    for i in range(n):
        print(time[i])


"""
答えはシンプルになる
円だから2周する必要がある
"""
def C_ans():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    ans = [float("inf")]*n

    for i in range(2*n):
        ans[(i+1)%n] = min(ans[i%n]+s[i%n], t[(i+1)%n])

    for i in range(n):
        print(ans[i])


def C_WA2():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    #高橋にもらうのが早い順
    ti = []
    for i in range(n):
        ti.append([t[i], i])
    ti = sorted(ti)

    #初めてもらう時間
    time = [float("inf")]*n
    for i in range(2*n):
        if i==0:
            time[ti[i][1]] = t[ti[i][1]]
            time[(ti[i][1]+1)%n] = time[ti[i][1]] + s[ti[i][1]]
        else:
            time[ti[i%n][1]] = min(time[ti[i%n][1]], t[ti[i%n][1]], time[(ti[i%n][1]-1)%n]+s[(ti[i%n][1]-1)%n])
            time[(ti[i%n][1]+1)%n] = min(time[(ti[i%n][1]+1)%n], time[ti[i%n][1]]+s[ti[i%n][1]])
    #output
    for i in range(n):
        print(time[i])


# def D():

