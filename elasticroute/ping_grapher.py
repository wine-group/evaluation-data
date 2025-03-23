import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np

# Read the CSV files
loaded_df = pd.read_csv('regular_loaded.csv', parse_dates=['Timestamp'])
unloaded_df = pd.read_csv('regular_unloaded.csv', parse_dates=['Timestamp'])

# Function to calculate statistics
def calculate_stats(data):
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'min': np.min(data),
        'max': np.max(data),
        'std': np.std(data)
    }

# Calculate statistics
loaded_stats = calculate_stats(loaded_df['Ping Time (ms)'])
unloaded_stats = calculate_stats(unloaded_df['Ping Time (ms)'])

# Create the plot with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 4), sharex=False)

# Plot unloaded data
ax1.plot(unloaded_df['Timestamp'], unloaded_df['Ping Time (ms)'], label='Unloaded', color='green', alpha=0.7)
ax1.set_ylabel('RTT (ms)')
ax1.set_title('ICMP RTT (Unloaded)')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

# Plot loaded data
ax2.plot(loaded_df['Timestamp'], loaded_df['Ping Time (ms)'], label='Loaded', color='blue', alpha=0.7)
ax2.set_xlabel('Time')
ax2.set_ylabel('RTT (ms)')
ax2.set_title('ICMP RTT (100 Mbps TCP TX Load)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

# Adjust layout and rotate x-axis labels
plt.tight_layout()
# fig.autofmt_xdate()

# Show plot
# plt.show()
plt.savefig('regular_unload_and_loaded_latency.eps')

# Print statistics
print("Unloaded Network Statistics:")
for key, value in unloaded_stats.items():
    print(f"{key.capitalize()}: {value:.2f} ms")

print("\nLoaded Network Statistics:")
for key, value in loaded_stats.items():
    print(f"{key.capitalize()}: {value:.2f} ms")