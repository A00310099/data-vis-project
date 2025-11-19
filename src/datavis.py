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
