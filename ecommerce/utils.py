import datetime

def get_year_string(joining_date):
    now = datetime.datetime.now()
    curr_year = now.year
    if now.month <= 6:
        curr_year = curr_year - 1
    if curr_year - joining_date.year == 0:
        return 'FE'
    elif curr_year - joining_date.year == 1:
        return 'SE'
    elif curr_year - joining_date.year == 2:
        return 'TE'
    elif curr_year - joining_date.year == 3:
        return 'BE'
    else:
        return None

def get_joining_date(year_string):
    now = datetime.datetime.now()
    year_delta = 0
    if(now.month <= 6):
        year_delta = -1
    else:
        year_delta = 0
    if year_string == 'FE':
        year_delta = year_delta-0
    elif year_string == 'SE':
        year_delta = year_delta-1
    elif year_string == 'TE':
        year_delta = year_delta-2
    elif year_string == 'BE':
        year_delta = year_delta-3
    else:
        return None
    return datetime.datetime(now.year-year_delta, 7, 1)
