class Day:
    def __init__(self, date: int, name=""):
        self.date = date
        if self.date > 0:
            self.name = name
            self.isEmpty = False
        elif self.date < 0:
            raise ValueError("Date cannot be less than 0")
        else:
            self.isEmpty = True

    def __str__(self):
        if self.isEmpty:
            return "   "
        else:
            if self.date > 10:
                return f"{self.date} "
            return f" {self.date} "

    def __int__(self):
        return int(self.date)

    def __repr__(self):
        if not self.isEmpty:
            return f"Date object: {self.name} the {self.date}"
        else:
            return "Empty date object"
