
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


