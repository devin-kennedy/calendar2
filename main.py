import calendar
from calendar import Day, Week, Month, Year


def main():
    day, month, year = calendar.parseDate("4-5-2007")
    print(year)


if __name__ == "__main__":
    main()
