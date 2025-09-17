from datetime import datetime
from calendar import day_name

def dayname(time):
    """Return the name of the day in a week."""
    return day_name[time.weekday()]
