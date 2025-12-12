tupleList1 = [
    ("parent", "Hasib", "Rakib"),
    ("parent", "Rakib", "Sohel"),
    ("parent", "Rakib", "Rebeka"),
    ("parent", "Rashid", "Hasib"),
    ("parent", "Rebeka", "Ayesha"),
    ("parent", "Sohel", "Fatima"),
]

maleList = ["Hasib", "Rakib", "Sohel", "Rashid"]


# Functions


def findGp():
    X = str(input("Grandchild: "))
    print("Grandparent: ", end=" ")
    i = 0
    while i <= 5:
        if (tupleList1[i][0] == "parent") & (tupleList1[i][2] == X):
            for j in range(6):
                if (tupleList1[j][0] == "parent") & (
                    tupleList1[i][1] == tupleList1[j][2]
                ):
                    print(tupleList1[j][1], end=" ")
        i = i + 1


def findBrother():
    X = str(input("Sibling: "))
    print("Brother: ", end=" ")
    i = 0
    while i <= 5:
        if (tupleList1[i][0] == "parent") & (tupleList1[i][2] == X):
            for j in range(6):
                if (
                    (tupleList1[j][0] == "parent")
                    & (tupleList1[i][1] == tupleList1[j][1])
                    & (tupleList1[i][2] != tupleList1[j][2])
                    & (tupleList1[j][2] in maleList)
                ):
                    print(tupleList1[j][2], end=" ")
        i = i + 1


def findSister():
    X = str(input("Sibling: "))
    print("Sister: ", end=" ")
    i = 0
    while i <= 5:
        if (tupleList1[i][0] == "parent") & (tupleList1[i][2] == X):
            for j in range(6):
                if (
                    (tupleList1[j][0] == "parent")
                    & (tupleList1[i][1] == tupleList1[j][1])
                    & (tupleList1[i][2] != tupleList1[j][2])
                    & (tupleList1[j][2] not in maleList)
                ):
                    print(tupleList1[j][2], end=" ")
        i = i + 1


def findUncle():
    X = str(input("Niece/Nephew: "))
    print("Uncle: ", end=" ")
    i = 0
    while i <= 5:
        if (tupleList1[i][0] == "parent") & (tupleList1[i][2] == X):
            for j in range(6):
                if (tupleList1[j][0] == "parent") & (
                    tupleList1[i][1] == tupleList1[j][2]
                ):
                    for k in range(6):
                        if (
                            (tupleList1[k][0] == "parent")
                            & (tupleList1[j][1] == tupleList1[k][1])
                            & (tupleList1[j][2] != tupleList1[k][2])
                            & (tupleList1[k][2] in maleList)
                        ):
                            print(tupleList1[k][2], end=" ")
        i = i + 1


def findAunt():
    X = str(input("Niece/Nephew: "))
    print("Aunt: ", end=" ")
    i = 0
    while i <= 5:
        if (tupleList1[i][0] == "parent") & (tupleList1[i][2] == X):
            for j in range(6):
                if (tupleList1[j][0] == "parent") & (
                    tupleList1[i][1] == tupleList1[j][2]
                ):
                    for k in range(6):
                        if (
                            (tupleList1[k][0] == "parent")
                            & (tupleList1[j][1] == tupleList1[k][1])
                            & (tupleList1[j][2] != tupleList1[k][2])
                            & (tupleList1[k][2] not in maleList)
                        ):
                            print(tupleList1[k][2], end=" ")
        i = i + 1


switch = {
    "findGp": findGp,
    "findBrother": findBrother,
    "findSister": findSister,
    "findUncle": findUncle,
    "findAunt": findAunt,
}

# Main

func = str(input("?- "))
if func in switch:
    switch[func]()
else:
    print("Invalid function")
