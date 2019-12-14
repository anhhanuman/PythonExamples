# https://www.tutorialspoint.com/python/python_classes_objects.htm


class Employee:
    empCount = 0


def __init__(self, name, salary):
    self.myName = name
    self.mySalary = salary
    Employee.empCount += 1


def displayCount(self):
    print("Total employee %d : " % Employee.empCount)
