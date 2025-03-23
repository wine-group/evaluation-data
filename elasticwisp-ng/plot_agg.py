import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Path to the prepared CSV file
prepared_file_path = '/Users/duncam/Library/Mobile Documents/com~apple~CloudDocs/Working files/Graphs/2023-12-18_14_23_influxdb_data_cleaned.csv'

# Read the prepared CSV file
data = pd.read_csv(prepared_file_path)

# Convert _time to datetime
data['_time'] = pd.to_datetime(data['_time'])

# Set _time as the index
data.set_index('_time', inplace=True)

# Calculate the rolling mean (5-minute window)
rolling_mean = data['_value'].rolling(window='5min', center=True).mean()

# Calculate a longer-term rolling average (e.g., 1-hour window)
long_term_average = data['_value'].rolling(window='1H', center=True).mean()

# Define capacity thresholds
upper_threshold = 60  # 60% of expected maximum
lower_threshold = 20  # 20% of expected maximum

# Create a color array based on the thresholds
# colors = np.where(rolling_mean > upper_threshold, 'red',
#                   np.where(rolling_mean < lower_threshold, 'blue', 'green'))

# Plot the results
plt.figure(figsize=(7, 4))

# Plot the rolling mean with color-coding
# for i in range(1, len(rolling_mean)):
#     plt.plot(rolling_mean.index[i-1:i+1], rolling_mean.iloc[i-1:i+1], 
#              color=colors[i], linewidth=2)
    
for i in range(1, len(rolling_mean)):
    plt.plot(rolling_mean.index[i-1:i+1], rolling_mean.iloc[i-1:i+1], 
            color='turquoise', linewidth=2)

# Add threshold lines
plt.axhline(y=upper_threshold, color='orange', linestyle='--', label='Upper Threshold', zorder=2)
plt.axhline(y=lower_threshold, color='cyan', linestyle='--', label='Lower Threshold', zorder=2)

# Add long-term rolling average line with color changes
for i in range(1, len(long_term_average)):
    if long_term_average.iloc[i] > upper_threshold:
        color = 'crimson'
    elif long_term_average.iloc[i] < lower_threshold:
        color = 'royalblue'
    else:
        color = 'black'
    plt.plot(long_term_average.index[i-1:i+1], long_term_average.iloc[i-1:i+1], 
             color=color, linestyle='--', linewidth=2, zorder=3)

plt.xlabel('Time (Month-Day Hour)')
plt.ylabel('Total Throughput (Mbps)')
# plt.title('5-Minute Averaged Throughput of 4 APs Over 24 Hours')
plt.title('5-Minute Averaged Throughput, 24 Hour AS141710 Dataset')

# Create a custom legend
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='turquoise', lw=2),
                Line2D([0], [0], color='orange', linestyle='--', lw=2),
                Line2D([0], [0], color='cyan', linestyle='--', lw=2),
                Line2D([0], [0], color='black', lw=2),
                Line2D([0], [0], color='crimson', lw=2),
                Line2D([0], [0], color='royalblue', lw=2)]
plt.legend(custom_lines, ['Normal Range', 'Upper Threshold', 'Lower Threshold', '1-Hour Rolling Average (Normal)',
                          '1-Hour Rolling Average (Above Upper)', '1-Hour Rolling Average (Below Lower)'])

# Format x-axis to show labels every 3 hours
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H'))

plt.xticks(rotation=0, ha='right') # Was 45 degree rotation
plt.tight_layout()

plt.ylim(0, 100)  # Adjust as needed


plt.savefig('/Users/duncam/Library/Mobile Documents/com~apple~CloudDocs/Working files/Graphs/aggregate_throughput.eps')
plt.show()
