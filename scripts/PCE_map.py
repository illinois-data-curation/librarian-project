import pandas as pd
import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, 'states')
df_total = pd.read_csv('data/interim_data/PCE_total.csv')
df_sub = pd.read_csv('data/interim_data/PCE_sub.csv')

selection = alt.selection_point(fields=['GeoName'])

map1 = alt.Chart(states).mark_geoshape( # Background gray
    fill='gray',
    stroke='white'
).properties(
    width=600,
    height=400
).project('albersUsa')

map2 = alt.Chart(states).mark_geoshape(
    stroke='white'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(df_total, 'id', list(df_total.columns))
).encode(
    color=alt.Color(
        '2023:Q',
        scale=alt.Scale(scheme='greenblue'),
        legend=alt.Legend(title="PCE in 2023",
                          labelFontSize=12,
                          titleFontSize=14,
                          titlePadding=10)),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    tooltip=['GeoName:N', '2023:Q']
).add_params(
    selection
).properties(
    width=600,
    height=400
).project(
    type='albersUsa'
)

bar = alt.Chart(df_sub).mark_bar().encode(
    alt.X('2023:Q', title='Expenditures in 2023',
          axis=alt.Axis(titleFontSize=16, titlePadding=20)),
    alt.Y('Description:N',
          title='Category',
          sort=alt.EncodingSortField(field='2023', op='sum', order='descending'),
          axis=alt.Axis(titleFontSize=16, titlePadding=20)),
    tooltip=['2023:Q']
).transform_filter(
    selection
).properties(
    width=700
)

map = alt.layer(map1, map2)
PCE_map = map & bar

PCE_map.save('results/PCE_map.html')