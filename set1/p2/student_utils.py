passingAverage = 75


def calculateAverage(grades):
    return sum(grades) / len(grades)


def getStatus(grades):
    if calculateAverage(grades) >= passingAverage:
        return "Passed"
    return "Failed"


def getHighest(grades):
    return max(grades)


def getLowest(grades):
    return min(grades)