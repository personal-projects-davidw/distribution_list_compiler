""" Program to generate an email distribution list from excel spreadsheet where
a blank value represented as a string ' ' in column 'Last Login' denotes a user
not registered and therefore requires email adding to distribution list.  Email
address extracted from column 'Email' and concatenated into string for cut and
paste into an actual email."""

import pandas as pd
import numpy as np

# Read spreadsheet into dataframe and check
df = pd.read_excel('ENTER_SPREADSHEET_NAME_HERE.xls')
df.head()
df.shape

# Conditional drop rows of values ' ' in selected column and check
df = df[df['Last Login'] == ' ']
df.head()
df.shape

# Construct distribution list by iterating over email addresses & adding to str
dist_list = ''
for index, row in df.iterrows():
    email = (row['Email'])
    dist_list = dist_list + '; ' + email

# Display completed distribution list
print(dist_list)
