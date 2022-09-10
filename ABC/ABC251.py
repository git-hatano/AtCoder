
"""
安易に全bit探索しない
"""
def B_TLE():
    N, W = map(int, input().split())
    A = [a for a in list(map(int, input().split()))]

    good_n = []
    for bit in range(1 << N):
        combination = [] 
        for i in range(N):
            shift_i = 1 << i
            if bit & shift_i > 0:
                combination.append(A[i])

        good_tmp = sum(combination)
        if len(combination)>0 and len(combination)<=3 and good_tmp<=W:
            good_n.append(good_tmp)
            # print(combination, good_tmp)

    print(len(set(good_n)))


def B():
    N, W = map(int, input().split())
    A = [a for a in list(map(int, input().split()))]

    sum_l = [False]*(W+1)
    for i in range(N):
        if A[i] <= W:
            sum_l[A[i]] = True

        for j in range(i+1, N):
            if A[i]+A[j] <= W:
                sum_l[A[i]+A[j]] = True

            for k in range(j+1, N):
                if A[i]+A[j]+A[k] <= W:
                    sum_l[A[i]+A[j]+A[k]] = True

    print(sum(sum_l))


def C():
    n = int(input())
    res = {}
    for i in range(n):
        s,t = input().split()

        if s not in res:
            res[s] = [int(t), i]

    max_t = 0
    for key in res:
        if res[key][0] > max_t:
            max_t = res[key][0]
            max_i = res[key][1] + 1

    print(max_i)


def A():
    s = input()
    ans = s
    for i in range(6):
        ans += s

        if len(ans)==6:
            break

    print(ans)
