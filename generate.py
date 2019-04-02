def abc():

    yield  1
    yield  22
    yield  43
    yield  42
    yield  25

collection = abc()
for i in collection:
    print(i)


def cube():
    for i in range(1,11):
        yield i**3


cb_list = cube()
for i in cb_list:
    print(i)
