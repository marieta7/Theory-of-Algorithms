def naive_match(T, P):
    n = len(T)
    m = len(P)
    shifts = []

    for s in range(n - m + 1):
        j = 0

        while j < m and T[s + j] == P[j]:
            j += 1

        if j == m:
            shifts.append(s)

    return shifts


T = input("Enter text: ")
P = input("Enter pattern: ")

result = naive_match(T, P)

print(f"Text: {T}")
print(f"Pattern: {P}")
print(f"Pattern positions: {result}")
