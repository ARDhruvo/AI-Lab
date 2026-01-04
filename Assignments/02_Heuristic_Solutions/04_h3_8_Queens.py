hval = [0]

# Helper functions


def nthel(N, lst):
    return lst[N - 1]


def incr_hval():
    hval[0] += 1


def do_incr(X, Y):
    if X == Y:
        incr_hval()


def chk_incr(I, L, X):
    if I == 8:
        return
    I1 = I + 1
    Y = nthel(I1, L)
    do_incr(X, Y)
    chk_incr(I1, L, X)


def hl(I, L):
    if I == 8:
        return
    X = nthel(I, L)
    chk_incr(I, L, X)
    I1 = I + 1
    hl(I1, L)


# Diagonal Up functions


def doup_incr(X, Y, K1):
    X1 = X + K1
    if Y == X1:
        incr_hval()


def chkup_incr(I, L, X, K):
    if I == 8:
        return
    I1 = I + 1
    Y = nthel(I1, L)
    K1 = K + 1
    doup_incr(X, Y, K1)
    chkup_incr(I1, L, X, K1)


def di_up(I, L):
    if I == 8:
        return
    X = nthel(I, L)
    chkup_incr(I, L, X, 0)
    I1 = I + 1
    di_up(I1, L)


# Diagonal Down functions


def dodn_incr(X, Y, K1):
    X1 = X - K1
    if Y == X1:
        incr_hval()


def chkdn_incr(I, L, X, K):
    if I == 8:
        return
    I1 = I + 1
    Y = nthel(I1, L)
    K1 = K + 1
    dodn_incr(X, Y, K1)
    chkdn_incr(I1, L, X, K1)


def di_dn(I, L):
    if I == 8:
        return
    X = nthel(I, L)
    chkdn_incr(I, L, X, 0)
    I1 = I + 1
    di_dn(I1, L)


# Evaluation State


def evalState(L):
    hval[0] = 0
    hl(1, L)
    di_up(1, L)
    di_dn(1, L)
    V = hval[0]
    return V


# Main

result = evalState(test_board)
print(f"Heuristics value: {result}")
