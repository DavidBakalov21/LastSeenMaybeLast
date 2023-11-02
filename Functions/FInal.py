import os

import pandas as pd
def ShowFirst():
    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'Final.csv')
    df = pd.read_csv(csv)
    user_dict = {}
    for index, row in df.iterrows():
        user_dict[row['Name']] = {'lastSeenDate': row['LastSeen'], 'id': row['ID']}
    return user_dict




