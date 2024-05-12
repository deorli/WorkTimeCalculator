import os 
import datetime
from common import * 

# ############################# USER CONFIG START #############################
SETTLEMENT_DAY = 1
SETTLEMENT_MONTH = 4
# ############################# USER CONFIG STOP ##############################

# date in yyyy/mm/dd format
CURRENT_DATE = datetime.date.today()
TODAY = datetime.datetime(CURRENT_DATE.year,
                          CURRENT_DATE.month,
                          CURRENT_DATE.day)
ANNUAL_SETTLEMENT_DATE = datetime.datetime(CURRENT_DATE.year,
                                           SETTLEMENT_MONTH,
                                           SETTLEMENT_DAY)

MONTH_NAMES_DAYS = {
    1: ['January', 31],
    2: ['February', getHowDaysInLeapYear(TODAY.year)],
    3: ['March', 31],
    4: ['April', 30],
    5: ['May', 31],
    6: ['June', 30],
    7: ['July', 31],
    8: ['August', 31],
    9: ['September', 30],
    10: ['October', 31],
    11: ['November', 30],
    12: ['December', 31]
}