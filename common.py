import datetime

from icecream import ic

def getHowDaysInLeapYear(year: int = 0) -> int:
    """
    Function to convert date in string format "YYYY-MM-DD"
    into a datetime object
    """
    assert(year > 0)
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 28
    else:
        return 29

def convertStrToDate(date: str = None) -> datetime.datetime:
    """
    Function to convert date in string format "YYYY-MM-DD"
    into a datetime object
    """
    assert(date != "")
    y, m, d = date.split(sep = "-")
    return datetime.datetime(int(y), int(m), int(d))