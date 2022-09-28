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
    a, b, c = map(int, input().split())
    ans = 21 -a -b -c
    print(ans)


def B():
    s = input()
    s = s[::-1]

    ans = ""
    for c in s:
        if c=="6":
            ans += "9"
        elif c=="9":
            ans += "6"
        else:
            ans += c

    print(ans)


def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    from collections import Counter
    counter = Counter(c)

    ans = 0
    for key in counter.keys():
        for i in range(n):
            if b[key-1] == a[i]:
                ans += counter[key]

    print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        d[b[c[i]-1]] += 1

    from collections import Counter
    a_counter = Counter(a)

    ans = 0
    for key in a_counter.keys():
        if key in d:
            ans += a_counter[key]*d[key]
        
    print(ans)


# def D():

