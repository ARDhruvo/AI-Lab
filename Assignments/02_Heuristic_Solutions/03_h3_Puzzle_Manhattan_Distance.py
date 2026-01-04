# KB
# Goal Position gtp(piece, y, x)

gtp = {
    1: (1, 1),
    2: (1, 2),
    3: (1, 3),
    4: (2, 3),
    5: (3, 3),
    6: (3, 2),
    7: (3, 1),
    8: (2, 1),
}
gblnk = (2, 2)  # Blank (y, x)

# Current Position

tp = {
    1: (1, 2),
    2: (1, 3),
    3: (2, 1),
    4: (2, 3),
    5: (3, 3),
    6: (2, 2),
    7: (3, 2),
    8: (1, 1),
}
blnk = (3, 1)  # Blank (y, x)


def go():
    L = calcH(1, [])
    V = sumList(L)
    print(f"Heuristics: {V}")
    return V


def calcH(T, X):
    if T == 9:
        return X
    else:
        D = dist(T)
        X1 = X + [D]
        return calcH(T + 1, X1)


def dist(T):
    A, B = tp[T]
    C, D = gtp[T]
    return abs(A - C) + abs(B - D)


def sumList(L):
    if not L:
        return 0
    return L[0] + sumList(L[1:])


# Main

go()
