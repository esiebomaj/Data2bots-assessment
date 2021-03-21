import pandas as pd
import datetime as dt
import json

path_to_data = './python hands-on - dataset.csv'
data = pd.read_csv(path_to_data)


ref_date = dt.datetime.strptime('2021-01-01', '%Y-%m-%d').date()


def compute_obsolete(exp_date):
    """
    takes a expiration date of and item in string 
    and computes if the item is expired/obsolete based on the ref_date

    returns TRUE if the item is expired
    returns FALSE if the item is not expired

    """
#   convert date string to datetime object
    date_obj = dt.datetime.strptime(exp_date, '%Y-%m-%d').date()

#   computes difference in days between exp_date and ref_date
    diff = date_obj - ref_date
    diff_in_days = diff.days

#   returns 'FALSE' if difference is greater than 0 (i.e item is not extpired)
#   else returns 'TRUE'
    if diff_in_days > 0:
        return 'FALSE'
    else:
        return 'TRUE'


# create a new column 'obsolete' and populate it using the function compute_obsolete
data['obsolete'] = data['date'].map(compute_obsolete)


# convert the data to json format
data.to_json('data.json')

# the data can be converted back to pandas dataframe
df = pd.read_json('data.json',)