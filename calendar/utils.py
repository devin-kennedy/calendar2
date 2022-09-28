def isLeapYear(year: int):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    return False


def getStartingDay(y: int, m: int):
    d = 1
    key = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + int(y / 4) - int(y / 100) + int(y / 400) + key[m - 1] + d) % 7


def getDay(ind):
    dayKey = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return dayKey[ind]


def getMonth(ind):
    monthKey = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return monthKey[ind]


def getDayCount(month: int, year: int):
    has30 = [4, 6, 9, 11]

    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        if month in has30:
            return 30
        else:
            return 31
