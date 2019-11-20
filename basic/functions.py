import random


def defineMyNumber(myNumber):
    if myNumber == 1:
        return 'ok the answer number is 1'
    elif myNumber == 2:
        return 'ok, the answer number is 2'
    elif myNumber == 3:
        return 'ok, the answer number is 3'
    elif myNumber == 4:
        return 'ok, the answer number is 4'
    elif myNumber == 5:
        return 'ok, the answer number is 5'
    elif myNumber == 6:
        return 'ok, the answer number is 6'
    elif myNumber == 'test':
        return 'NOT the expected type'
    else:
        return 'NOT Supported'


myRandomNumber = random.randint(1, 9)  # random.randint(10, 1) causes an error

print(myRandomNumber)
defineMyNumber(myRandomNumber)

print(defineMyNumber(myRandomNumber))
print(defineMyNumber(random.randint(1, 9)))


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0
    print(eggs)
    print(ham)
