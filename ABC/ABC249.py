
def B():
    S = input()

    can = False
    # 大文字、小文字両方あるか
    if not S.islower() and not S.isupper():
        if len(set(list(S)))==len(S):
            can = True

    if can:
        print("Yes")
    else:
        print("No")


def A():
    def get_runtime(runtime, breaktime, totaltime):
        time = runtime * (totaltime // (runtime+breaktime))
        if totaltime%(runtime+breaktime) >= runtime:
            time += runtime
        else:
            time += totaltime%(runtime+breaktime)
        return time

    a, b, c, d, e, f, x = map(int, input().split())

    runtime_t = get_runtime(a, c, x)
    runtime_a = get_runtime(d, f, x)

    dist_t = b*runtime_t 
    dist_a = e*runtime_a

    if dist_t > dist_a:
        print("Takahashi")
    elif dist_t < dist_a:
        print("Aoki")
    else:
        print("Draw")


def C_WA():
    # 問題の意味がわからん。こんなん初めてや
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    print()


def C():
    from collections import Counter
    from itertools import product

    def solve():
        def calc(pro):
            """選び方 pro に対する答えを求める"""
            C = Counter()  # 空のカウンターを用意する
            for i in range(N):
                if pro[i]:
                    # S[i]を選ぶ場合、S[i]に含まれる文字のカウントにそれぞれ1足す C.update(S[i])なら1行
                    for ch in S[i]:
                        C[ch] += 1
            score = 0
            for ch, cnt in C.items():
                if cnt == K:  # K回"ちょうど"の種類数です
                    score += 1
            return score

        N, K = map(int, input().split())
        S = [input() for _ in range(N)]
        ans = 0
        for pro in product((True, False), repeat=N):
            ans = max(ans, calc(pro))
        return ans

    print(solve())
