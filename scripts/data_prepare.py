# This script acquires and tidies the datasets that will be used.

import pandas as pd

# State_Code
# Acquire the data via github URL
# This dataset helps us match each state with a state id, 
# which allows us to plot state data on the US map
url = 'https://raw.githubusercontent.com/GovLab/opencorporatesd3/refs/heads/master/us-state-names.tsv'
state_code = pd.read_csv(url, sep='\t')
state_code.to_csv('data/state_code.csv', index=False)


# PCE data
# Basic cleaning
PCE = pd.read_excel('data/Table.xlsx',header=5)
PCE = PCE[:-3]
PCE.to_csv('data/interim_data/PCE_clean.csv', index=False)


# IPEDs data
ipeds = pd.read_csv("data/AcademicLibrary.csv")
# Simplify column names
ipeds.columns = ipeds.columns.str.replace("HD2022.", "")
ipeds.columns = ipeds.columns.str.replace("AL2022_RV.", "")
ipeds.drop('institution name.1', axis=1, inplace=True)

# Select only interested columns to make the dataframe smaller
ipeds = ipeds[['unitid','institution name', 'ZIP code',
               'State abbreviation','Librarians FTE staff',
               'Total library FTE staff',
               'Total salaries and wages from the library budget']].copy()
# Select only universities that have a number of librarians above average
# because a lot of small universities only have a handful of librarians 
# these are not valuable as our reference
ipeds = ipeds[ipeds['Librarians FTE staff'] > ipeds['Librarians FTE staff'].mean()]

# Calculate average the salary of library staff
ipeds['Avg_Salary'] = ipeds['Total salaries and wages from the library budget'] / ipeds['Total library FTE staff']
ipedsbyState = ipeds.groupby('State abbreviation')['Avg_Salary'].mean().reset_index(name='Avg_Salary')


ipeds.to_csv('data/interim_data/IPED_clean.csv', index=False)
ipedsbyState.to_csv('data/interim_data/IPED_by_State.csv', index=False)
