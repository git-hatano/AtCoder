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

# def A():



# def B():



def C():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)

    ans = 0
    l = 0
    s = 0
    for key in sorted(set(a), reverse=True):
        if counter[key]>=4:
            l = max(l, key)
            s = max(s, key)
            ans = max(ans, l*s)
        elif counter[key]>=2:
            if l==0:
                l = max(l, key)
            else:
                s = max(s, key)
                ans = max(ans, l*s)
    print(ans)


def C_ans():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    v = []
    for key in counter:
        if counter[key]>=4:
            v.append(key)
            v.append(key)
        elif counter[key]>=2:
            v.append(key)

    ans = 0
    if len(v)>=2:
        v.sort(reverse=True)
        ans = v[0]*v[1]
    print(ans)


# def D():

