
def A():
    N, X = map(int, input().split())

    moji = ""

    for i in range(65, 91):
        s = chr(i)
        moji += s*N

    print(moji[X-1])

def B():
    N, K, Q = map(int, input().split())
    A = [a-1 for a in list(map(int, input().split()))]
    L = [a-1 for a in list(map(int, input().split()))]

    mas = [False]*N
    for a in A:
        mas[a] = True

    for l in L:
        if A[l]== N-1:
            continue
        else:
            if mas[A[l]+1]==False:
                mas[A[l]+1] = True
                mas[A[l]] = False
                A[l] += 1

    res = [str(a+1) for a in A]
    print(" ".join(res))


def C_TLE():
    N = int(input())
    S = [bool(int(s)) for s in input()]
    W = list(map(int, input().split()))

    lims = []
    s_W = list(set(sorted(W)))
    for i in range(len(s_W)-1):
        lims.append((s_W[i]+s_W[i+1])/2)

    lims.insert(0, min(W)-1)
    lims.append(max(W)+1)

    max_cnt = 0
    for lim in lims:
        cnt = 0
        for i in range(N):
            if W[i] > lim:
                pred = True
            else:
                pred = False
            
            if pred==S[i]:
                cnt +=1
            
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


def C_WA():
    N = int(input())
    S = [bool(int(s)) for s in input()]
    W = list(map(int, input().split()))

    ad, ad_cnt, ch, ch_cnt = 0,0,0,0
    for w,s in zip(W, S):
        if s==True:
            ad += w
            ad_cnt += 1
        else:
            ch += w
            ch_cnt += 1

    if ad_cnt>0:
        ave_ad = ad/ad_cnt
    else:
        ave_ad = 0
    if ch_cnt>0:
        ave_ch = ch/ch_cnt
    else:
        ave_ch = 0

    lim = (ave_ad + ave_ch) / 2
    lims = []
    for i in range(-1000, 1000, 10):
        lims.append(lim+i)

    max_cnt = 0
    for lim in lims:
        cnt = 0
        for i in range(N):
            if W[i] > lim:
                pred = True
            else:
                pred = False
            
            if pred==S[i]:
                cnt +=1
            
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


def C():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))

    cnt = 0
    people = []
    for w, s in zip(W, S):
        people.append([w, s])
        if s=="1":
            cnt += 1
    people = sorted(people, key=lambda x: x[0])

    ans = cnt
    for i in range(N):
        if people[i][1]=="1":
            cnt -= 1
        else:
            cnt += 1

        if i < (N-1):
            if people[i][0] != people[i+1][0]:
                ans = max(ans, cnt)
        else:
            ans = max(ans, cnt)

    print(ans)

