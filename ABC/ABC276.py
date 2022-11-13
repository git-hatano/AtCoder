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
    s = input()
    key = "a"
    ans = -1
    if key in s:
        for i in reversed(range(len(s))):
            if s[i]==key:
                ans = i+1
                break
    print(ans)


def B():
    from collections import defaultdict
    n, m = map(int, input().split())

    d = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    for i in range(n):
        d[i+1] = [len(d[i+1])] + sorted(d[i+1])
        ans = " ".join([str(x) for x in d[i+1]])
        print(ans)


def C():
    n = int(input())
    p = list(map(int, input().split()))

    for i in reversed(range(n-1)):
        if p[i] > p[i+1]:
            x = p[i]
            idx = i
            break

    buf = []
    for i in range(idx, n):
        if x > p[i]:
            buf.append([p[i], i])
    buf.sort(reverse=True)

    j = buf[0][1]
    p[idx], p[j] = p[j], p[idx]

    tmp = sorted(p[idx+1:], reverse=True)
    ans = p[:idx+1] + tmp

    ans = " ".join([str(x) for x in ans])
    print(ans)


# def D():
