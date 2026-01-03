def term(n):
    return 100 + (n - 1) * 5


def seriesSum(n):
    if n == 1:
        return 100
    else:
        return term(n) + seriesSum(n - 1)


# Main

n = int(input("Enter number of terms: "))
value = seriesSum(n)
print("Sum of series =", value)
