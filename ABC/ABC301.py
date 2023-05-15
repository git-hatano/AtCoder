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

def A():
    from collections import Counter
    n = int(input())
    s = list(input())
    cnt = Counter(s)

    if cnt["T"] > cnt["A"]:
        ans = "T"
    elif cnt["A"] > cnt["T"]:
        ans = "A"
    else:
        t = 0
        a = 0
        for i in range(n):
            if s[i]=="T":
                t += 1
            else:
                a += 1
            
            if t==cnt["T"]:
                ans = "T"
                break
            if a==cnt["A"]:
                ans = "A"
                break
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n-1):
        diff = a[i+1] - a[i]
        if abs(diff)==1:
            ans.append(a[i])
        else:
            ans.append(a[i])
            step = int(diff/abs(diff))
            if step>0:
                for i in range(a[i]+1, a[i+1], step):
                    ans.append(i)
            else:
                for i in range(a[i]-1, a[i+1], step):
                    ans.append(i)
    ans.append(a[-1])
    print(" ".join([str(x) for x in ans]))


def C():
    import sys
    from collections import Counter
    s = list(input())
    t = list(input())
    cnt_s = Counter(s)
    cnt_t = Counter(t)

    for c in "atcoder":
        m = max(cnt_s[c], cnt_t[c])
        if cnt_s["@"]<m-cnt_s[c] or cnt_t["@"]<m-cnt_t[c]:
            print("No")
            sys.exit()
        
        cnt_s["@"] -= m-cnt_s[c]
        cnt_s[c] = m
        cnt_t["@"] -= m-cnt_t[c]
        cnt_t[c] = m
    print("Yes" if cnt_s==cnt_t else "No")


# def D():

