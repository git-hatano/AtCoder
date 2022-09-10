
def D():
    S = input().split()
    T = input().split()

    cnt = 0
    for i in range(3):
        if S[i] != T[i]:
            j = T.index(S[i])
            S[i], S[j] = S[j], S[i]

            cnt+=1

    if cnt%2==0:
        print("Yes")
    else:
        print("No")


def B():
    # [x,y]
    vec = [[1,0], [0,-1], [-1,0], [0,1]]

    n = int(input())
    t = input() 

    point = [0,0]
    v = 0
    for i in range(n):
        if t[i]=="S":
            point[0] += vec[v][0]
            point[1] += vec[v][1]

        elif t[i]=="R":
            v += 1
            v %= 4

    print(point[0], point[1])


def A():
    n = int(input())
    s = input()
    print(s[-1])



