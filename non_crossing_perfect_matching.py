def c(v):
    if len(v) < 2 or len(v) % 2 != 0:
        return 1
    if v == "GC" or v == "CG" or v == "AU" or v == "UA":
        return 1
    ans = 0
    for i in range(1, len(v), 2):
        if v[0] == 'C' and v[i] == 'G' or \
                v[0] == 'G' and v[i] == 'C' or \
                v[0] == 'A' and v[i] == 'U' or \
                v[0] == 'U' and v[i] == 'A':
            ans += c(v[1:i]) * c(v[i + 1:])

    return ans


print(c("CGUAAUUACGGCAUUAGCAU"))