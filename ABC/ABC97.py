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



def C_TLE():
    s = input()
    n = len(s)
    k = int(input())
    k -= 1
    subs = set()
    for i in range(n):
        for j in range(i, n):
            subs.add(s[i:j+1])
    subs = sorted(list(subs))
    print(subs[k])


def C():
    from collections import defaultdict
    s = input()
    n = len(s)
    k = int(input())
    k -= 1
    d = defaultdict(list)
    for i in range(n):
        d[s[i]].append(i)
    d_keys = sorted(list(d.keys()))

    subs = set()
    for key in d_keys:
        for i in d[key]:
            cnt = 0
            for j in range(i, n):
                subs.add(s[i:j+1])
                cnt += 1
                if cnt==10:
                    break
        if len(subs)>k:
            break
    subs = sorted(list(subs))
    print(subs[k])


# def D():

