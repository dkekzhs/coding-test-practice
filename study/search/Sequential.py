data = ["apple","graph","tomato","pear"]
find = "tomato"


def Seq(da,fi):
    for i in range(len(da)):
        if da[i] == fi:
            return i+1

print(Seq(data,find))
