import pandas as pd
import altair as alt

df_merged = pd.read_csv('data/interim_data/IPED_PCE.csv')

scatter = alt.Chart(df_merged).mark_circle(size=100).encode(
    x=alt.X('Avg_Salary:Q', 
            title='Average Salary',
            scale=alt.Scale(domain=[30000, 70000]),
            
            axis=alt.Axis(titleFontSize=16, titlePadding=20)),
    y=alt.Y('Expenditure:Q',
            axis=alt.Axis(titleFontSize=16, titlePadding=20)),
    tooltip=['State:N']
).properties(
    width=600,
    height=400)

scatter.save('results/ipeds_pce_scatter.html')