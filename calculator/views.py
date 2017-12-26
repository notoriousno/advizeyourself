from datetime import datetime, timedelta, date

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from numpy import fv


#---------- Views ----------

@require_http_methods(['GET'])
def calculate_retirement(request):
    user_info = {}
    interest_rate = 1

    dataset = []
    pv = -1*(user_info["currentValue"])
    i = interest_rate
    dob = datetime.strptime(user_info["dob"], '%m/%d/%Y')
    currentAge = calculate_age(dob)
    dateRetire = add_years(dob, user_info["age_at_retire"])
    companyMatch = float(100+user_info["companyMatch"])/100
    pmt = -1*(user_info["yearlyContributions"] * companyMatch)
    n = user_info["age_at_retire"] - currentAge
    for x in range(0,n):
        value = fv(i,x,pmt, pv)
        dataset.append(value)        
    return dataset


#---------- Functions ----------

def add_years(d, years):

    """
    Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).
    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
