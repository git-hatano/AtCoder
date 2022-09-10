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
    n = int(input())
    if n>0 and n%100==0:
        print("Yes")
    else:
        print("No")


def B():
    s = list(input())
    n = len(s)

    # 最小の文字とその場所
    c_min = sorted(s)[0]
    c_min_pos = [i for i, x in enumerate(s) if x==c_min]
    # 最大の文字とその場所
    c_max = sorted(s, reverse=True)[0]
    c_max_pos = [i for i, x in enumerate(s) if x==c_max]

    s_min = s
    for i in c_min_pos:
        tmp = s[i:n] + s[:i]
        
        for j in range(n):
            if s_min[j]!=tmp[j]:
                if ord(s_min[j]) > ord(tmp[j]):
                    s_min = tmp
                break
    s_max = s
    for i in c_max_pos:
        tmp = s[i:n] + s[:i]
        
        for j in range(n):
            if s_max[j]!=tmp[j]:
                if ord(s_max[j]) < ord(tmp[j]):
                    s_max = tmp
                break
            
    print("".join(s_min))
    print("".join(s_max))


def B_ans():
    s = input()
    n = len(s)
    v = []
    for k in range(0, n):
        v.append(s[k:n] + s[0:k])
    print(min(v))
    print(max(v))


def C():
    n = int(input())

    A = []
    B = []
    total_time = 0
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        total_time += a/b

    half_time = total_time/2
    s_time = 0
    ans = 0
    for i in range(n):
        if s_time+A[i]/B[i] < half_time:
            s_time += A[i]/B[i]
            ans += A[i]
        else:
            ans += B[i]*(half_time-s_time)
            break
        
    print(ans)


# def D():

