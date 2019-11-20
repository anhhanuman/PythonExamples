def spam():
    eggs = 'spam local'
    print(eggs)


def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


def spam():
    global eggs
    eggs = 'spam'
    eggs = 'global'
    spam()
    print(eggs)


def printMe(text):
    print(text)
    return


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    mylist = [10, 20, 30]
