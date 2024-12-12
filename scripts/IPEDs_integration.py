import pandas as pd

IPED_by_State = pd.read_csv('data/interim_data/IPED_by_State.csv')
PCE_total = pd.read_csv('data/interim_data/PCE_total.csv')

ipeds_merged = IPED_by_State.merge(
    PCE_total[['GeoName','code','2023']], 
    left_on='State abbreviation',
    right_on='GeoName', 
    how='left')
ipeds_merged.drop(columns='State abbreviation',inplace=True)
ipeds_merged.rename(columns={
    'GeoName': 'State',
    '2023': 'Expenditure'}, 
    inplace=True)

ipeds_merged.to_csv('data/interim_data/IPED_PCE.csv',index=False)