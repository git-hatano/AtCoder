'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_s = s[::-1]

# 2次元配列
dp = [[0]*(k) for i in range(n)]
'''

def A():
    cards = list(map(int, input().split()))
    dic = {}
    for card in cards:
        if card not in dic:
            dic[card] = 1
        else:
            dic[card] += 1

    if len(list(dic.keys()))==2 and (dic[cards[0]]==2 or dic[cards[0]]==3):
        print("Yes")
    else:
        print("No")


def B():
    n = int(input())
    p = list(map(int, input().split()))
    p = [-1, -1] + p

    # 人nの親
    n_parent = p[n]

    ans = 0
    for i in range(n):
        if n_parent >= 0:
            n_parent = p[n_parent]
            ans += 1
        else:
            break

    print(ans)


def C():
    n, m = map(int, input().split())
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 全bit探索、Nが少なかったからできた
    combinations = []
    for bit in range(1 << 10):
        combination = [] 
        for i in range(10):
            shift_i = 1 << i
            if bit & shift_i > 0:
                combination.append(nums[i])
        
        if len(combination)==n and combination[-1]<=m:
            combinations.append(combination)

    combinations = sorted(combinations)
    for comb in combinations:
        ans = " ".join([str(x) for x in comb])
        print(ans)


# def D():

