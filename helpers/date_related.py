import pandas as pd
from pandas.tseries.offsets import BDay
import datetime


def last_business_day():
    """
    BDay is business day, not birthday...
    pd.datetime is an alias for datetime.datetime.
    :return: yesterday variable, which is datetime.date class.
    """
    today = pd.datetime.today()
    yesterday = today - BDay(1)
    yesterday = pd.to_datetime(yesterday).date()
    return yesterday


def previous_month():
    """
    Returning previous month with a year.
    :return: String with formated to Month_year eg. Augost_2019
    """
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    last_month_formated = last_month.strftime("%B_%Y")
    return last_month_formated
