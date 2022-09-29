from calendar import Week, Day, utils
import math
import numpy as np


class Month:
    def __init__(self, year: int, code: int):
        self.year = year
        self.code = code
        self.name = utils.getMonth(code)
        self.numDays = utils.getDayCount(code, year)
        self.weeks = []
        self.__generate()

    def __generate(self):
        startDay = utils.getStartingDay(self.year, self.code)
        self.weeks.append(Week([Day(0) for _ in range(startDay)]))
        daysUsed = 0
        for i in range(1, (7-startDay)+1):
            self.weeks[0].append(Day(i, utils.getDay(startDay)))
            daysUsed += 1

        for j in range(math.ceil((self.numDays - daysUsed)/7)):
            days = []
            for k in range(7):
                if daysUsed == self.numDays:
                    break
                days.append(Day(daysUsed+1))
                daysUsed += 1
            self.weeks.append(Week(days))

    def __str__(self):
        abbreviations = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        return "        " + self.name + "\n" + " ".join(abbreviations) + "\n" + "\n".join(str(week) for week in self.weeks)

    def __repr__(self):
        return f"Month object: {self.name} of year {self.year}"

    def __iter__(self):
        for week in self.weeks:
            yield week

    def __getitem__(self, item0, item1=None):
        if item1:
            return self.weeks[item0][item1]
        else:
            return self.weeks[item0]

    def toArray(self):
        return np.array([[int(str(day).strip()) if day else None for day in week] for week in self])
