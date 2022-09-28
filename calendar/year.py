from calendar import utils, Month


class Year:
    def __init__(self, year: int):
        self.year = year
        self.isLeap = self.isLeapYear()
        self.months = []
        self.__generate()

    def isLeapYear(self):
        return utils.isLeapYear(self.year)

    def __generate(self):
        for m in range(1, 13):
            self.months.append(Month(self.year, m))

    def __str__(self):
        return "\n\n".join(str(m) for m in self.months)

    def __repr__(self):
        return f"Year object of the year {self.year}"
