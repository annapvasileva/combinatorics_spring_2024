used = [False] * 5
perm = []

ans = 0


def permutation():
    global ans
    if len(perm) == 5:
        if not(perm[0] < perm[1] < perm[2] or perm[1] < perm[2] < perm[3] or \
               perm[2] < perm[3] < perm[4] or perm[0] > perm[1] > perm[2] or \
               perm[1] > perm[2] > perm[3] or perm[2] > perm[3] > perm[4]):
            ans += 1
        return
    for i in range(5):
        if used[i]:
            continue
        perm.append(i)
        used[i] = True
        permutation()
        perm.remove(i)
        used[i] = False

permutation()
print(ans)
