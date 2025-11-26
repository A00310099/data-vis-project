#%% 
import altair as alt
import pandas as pd

#Import data from tables
df = pd.read_csv('../data/povertyData.csv')
df2 = pd.read_csv('../data/PurchasingPowerParities.csv')

alt.data_transformers.disable_max_rows()
#%% Display first 5 rows (default) of table 1
df.head()

#%% Display first 10 rows of table 2
df2.head(10)

# %%

# make the chart for PovertyData
chart1 = alt.Chart(df).mark_circle().encode(
    x='geo',
    y='OBS_VALUE',
    color= alt.Color('sex', legend=alt.Legend(title='Gender'), scale=alt.Scale(range=['grey', 'maroon'])),
    tooltip=['TIME_PERIOD', 'sex', 'OBS_VALUE', 'geo']
).interactive()

# make the chart for PurchasingPowerParities
chart2 = alt.Chart(df2).mark_circle().encode(
    x='geo',
    y='OBS_VALUE',
    color= alt.Color('ppp_cat', legend=alt.Legend(title='Food Catagory')),
    tooltip=['TIME_PERIOD', 'ppp_cat', 'OBS_VALUE', 'geo']
    
).interactive()

#%%
#Scatter Plot graph for PovertyData and PurchasingPowerParities in seperate graphs side by side
#Where X axis is the Country, Y axis is the obs values as a persentage and the colours represent 
#the gender in the poverty dataset and the catagories in the PurchasingPowerParities dataset.
combined_chart = alt.hconcat(
    chart1,
    chart2
).resolve_scale(
    color='independent'  # Ensure that the color scales are independent
)
combined_chart
# %%
#Scatter Plot graph for PovertyData and PurchasingPowerParities combined
#Where X axis is the Country, Y axis is the obs values as a persentage and the colours represent 
#the gender in the poverty dataset and the catagories in the PurchasingPowerParities dataset.
(chart1 + chart2).resolve_scale(color='independent')
# %%
#Scatter Plot graph for PovertyData
#Where X axis is the Country, Y axis is the obs values as a persentage and the colours represent 
#the gender in the poverty dataset.
chart1
#%%
#Scatter Plot graph for PurchasingPowerParities
#Where X axis is the Country, Y axis is the obs values as a persentage and the colours represent 
#the catagories in the PurchasingPowerParities dataset.
chart2
# %%
source = df
source2 = df2
brush = alt.selection_interval(resolve='global')

base = alt.Chart(source).mark_bar().encode(
    y='OBS_VALUE',
    x='sex',
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
    x='ppp_cat',
    color=alt.Color("ppp_cat", legend=alt.Legend(title='Food Category')), 
    tooltip=['TIME_PERIOD', 'ppp_cat', 'OBS_VALUE', 'geo']
).add_params(
    brush
).properties(
    width=250,
    height=250
)

#%%
#Scatter Bar Chart for PovertyData and PurchasingPowerParities in two seperate graphs side by side
#Where X axis is the the gender in the poverty dataset and the catagories in the PurchasingPowerParities dataset
#and Y axis is the obs values as a persentage.

combined_chart = alt.hconcat(
    base,
    base2
).resolve_scale(
    color='independent'  # Ensure that the color scales are independent
)
combined_chart
# %%
