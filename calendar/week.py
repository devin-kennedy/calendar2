from calendar.day import Day


class Week:
    def __init__(self, days: list):
        for day in days:
            if not isinstance(day, Day):
                raise ValueError("Days list must all be Day objects")
        self.days = days
        self.numDays = len(days)

    def __str__(self):
        return " ".join([str(day) for day in self.days])

    def __repr__(self):
        return f"Week object of length {len(self.days)}"

    def append(self, day: Day):
        if self.numDays >= 7:
            raise ValueError("Weeks can be no longer than 7 days")
        self.days.append(day)
        self.numDays += 1

    def insert(self, day: Day, index):
        if self.numDays >= 7:
            raise ValueError("Weeks can be no longer than 7 days")
        self.days.insert(index, day)
        self.numDays += 1
