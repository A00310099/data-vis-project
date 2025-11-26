#%% 
import altair as alt
import pandas as pd

#%% Import data from tables
df = pd.read_csv('../data/povertyData.csv')
df2 = pd.read_csv('../data/PurchasingPowerParities.csv')

#%% Display first 5 rows (default) of table 1
df.head()

#%% Display first 10 rows of table 2
df2.head(10)

# %%
alt.data_transformers.disable_max_rows()

# make the chart for PovertyData
chart1 = alt.Chart(df).mark_point().encode(
    x='geo',
    y='OBS_VALUE',
    color='sex',
    tooltip=['TIME_PERIOD', 'sex', 'OBS_VALUE', 'geo']
).interactive()

# make the chart for PurchasingPowerParities
chart2 = alt.Chart(df2).mark_point().encode(
    x='geo',
    y='OBS_VALUE',
    color='ppp_cat',
    tooltip=['TIME_PERIOD', 'ppp_cat', 'OBS_VALUE', 'geo']
).interactive()

# %%
#Scatter Plot graph for PovertyData and PurchasingPowerParities
chart1 + chart2
# %%
#Scatter Plot graph for PovertyData
chart1
#%%
#Scatter Plot graph for PurchasingPowerParities
chart2
# %%
source = df
source2 = df2
brush = alt.selection_interval(resolve='global')

base = alt.Chart(source).mark_bar().encode(
    y='OBS_VALUE',
    color=alt.Color("sex", legend=alt.Legend(title='Gender')), 
    tooltip=['TIME_PERIOD', 'sex', 'OBS_VALUE', 'geo']
).add_params(
    brush
).properties(
    width=250,
    height=250
)

base2 = alt.Chart(source2).mark_bar().encode(
    y='OBS_VALUE',
    color=alt.Color("ppp_cat", legend=alt.Legend(title='Food Category')), 
    tooltip=['TIME_PERIOD', 'ppp_cat', 'OBS_VALUE', 'geo']
).add_params(
    brush
).properties(
    width=250,
    height=250
)

#base.encode(x='sex') | base2.encode(x='ppp_cat')

combined_chart = alt.hconcat(
    base,
    base2
).resolve_scale(
    color='independent'  # Ensure that the color scales are independent
)
combined_chart
# %%
