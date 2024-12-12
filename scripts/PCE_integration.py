# PCE
import pandas as pd

PCE = pd.read_csv('data/interim_data/PCE_clean.csv')

# State Code
state_code = pd.read_csv('data/state_code.csv')

PCE_total = pd.merge(PCE[PCE['LineCode']==1.0], state_code, 
                    left_on='GeoName', 
                    right_on='name', 
                    how='inner')
 
PCE_sub = pd.merge(
    PCE[PCE['LineCode'].isin([4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 23, 24])],
    # PCE has a hierachical structure. Only thses LineCodes are the finest levels of expenditure categories
    state_code,
    left_on='GeoName',
    right_on='name',
    how='inner'
)

PCE_total.to_csv('data/interim_data/PCE_total.csv', index=False)
PCE_sub.to_csv('data/interim_data/PCE_sub.csv', index=False)
