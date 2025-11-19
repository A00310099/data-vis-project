#%% 
import altair as alt
#%%
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
# load a sample dataset as a pandas DataFrame
#from altair.datasets import data
#cars = data.cars()

# make the chart
alt.Chart(df).mark_point().encode(
    x='geo',
    y='OBS_VALUE',
    color='sex',
).interactive()

# %%
