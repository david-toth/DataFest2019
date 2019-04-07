import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import matplotlib as mpl
import warnings
warnings.filterwarnings("ignore")

data_dir = "data/"

# Create dataframes from each .csv file
wellness_df = pd.read_csv(data_dir + "wellness.csv")
rpe_df = pd.read_csv(data_dir + "rpe.csv")

# Check the structure of each dataframe (df)
print(wellness_df)
print(rpe_df)

# We are only interested in Date, PlayerID, DailyLoad, and Fatigue
# We also want to remove NaN values if they exist
wellness_df = wellness_df[['Date', 'PlayerID', 'Fatigue']].copy()
rpe_df = rpe_df[['Date', 'PlayerID', 'DailyLoad']].copy()

# Remove NaN values in rpe_df
rpe_df = rpe_df.dropna()

# Make the Date column values in datetime format
wellness_df['Date'] = pd.to_datetime(wellness_df['Date'])
rpe_df['Date'] = pd.to_datetime(rpe_df['Date'])

# Check the previous dataframe cleaning-up
print(wellness_df)
print(rpe_df)

# Now, let's sort by both date and the playerID
wellness_df = wellness_df.sort_values(by=['Date', 'PlayerID'])
rpe_df = rpe_df.sort_values(by=['Date', 'PlayerID'])

# Check one more time to make sure the dataframes are looking clean
print(wellness_df)
print(rpe_df)

# Merge dataframes... fdl = 'Fatigue daily load'
fdl = rpe_df.merge(wellness_df, how = 'inner', on = ['PlayerID', 'Date'])

# Check fdl
print(fdl)

#  Drop Date column, sort by playerID
fdl = fdl.drop(['Date'], 1)
fdl = fdl.sort_values(by='PlayerID')
fdl = fdl.set_index('PlayerID')

# Create a dictionary with keys = playerID and values = 2 np arrays (daily load, fatigue)
data_dict = {}
for key in range(1,18):
    value = [fdl.get_value(key,'DailyLoad'), fdl.get_value(key, 'Fatigue')]
    data_dict[key] = data_dict.get(key, value)

# Create dictionary of dataframes
master_dict = {}
player_id_list = [i for i in range(1,18)]
for i in player_id_list:
    master_dict[i] = pd.DataFrame()

# Fill in data for each dataframe
for player_id, df in master_dict.items():
    df['DailyLoad'] = data_dict[player_id][0]
    df['Fatigue'] = data_dict[player_id][1]

# Check that master_dict contains a dataframe with the appropriate data
# for each playerID
print(master_dict)

# Sort each dataframe by the DailyLoad values
for i in range(1,18):
    master_dict[i] = master_dict[i].sort_values(by='DailyLoad')

# Calculate moving average to smooth fatigue vs. daily load lines
# Then, find the ratio between average fatigue and daily load
for i in range(1,18):
    master_dict[i]['MovingAvg'] = master_dict[i]['Fatigue'].rolling(window=30).mean()
    master_dict[i]['FDLRatio'] = master_dict[i]['MovingAvg'] / master_dict[i]['DailyLoad']

# Create master plot
mpl.style.use('dark_background')
fig, axs = plt.subplots(3,6, figsize=(30,10))
fig.subplots_adjust(hspace = .5, wspace=.25)
axs = axs.ravel()
for i in range(1,18):
    axs[i].plot(master_dict[i]['DailyLoad'], master_dict[i]['MovingAvg'], '-o')
    axs[i].set_title('PlayerID' + ' ' + str(i))

plt.savefig('fatigue_vs_daily_load.png')
