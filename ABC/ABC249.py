
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



