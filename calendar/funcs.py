import calendar


def parseDate(date: str):
    parsed = date.split("-")
    if len(parsed) != 3:
        raise ValueError("Incorrect date passed, must be in the format mm-dd-yyyy (do not include leading 0s)")
    try:
        monthCode = int(parsed[0])
        date = int(parsed[1])
        yearInt = int(parsed[2])
    except ValueError:
        raise ValueError("Incorrect date passed")
    year = calendar.Year(yearInt)
    return (calendar.Day(5, calendar.getDay(calendar.getDayWeek(yearInt, monthCode, date))),
            year[monthCode-1],
            year
            )
