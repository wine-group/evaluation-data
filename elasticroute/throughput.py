# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd

# # Set the style to a cleaner, more modern look
# sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.6)

# # Data
# scenarios = ['Fixed-Power\nFixed-Capacity', 'Mixed-Power\nFixed-Capacity', 'Fixed-Power\nMixed-Capacity', 'Mixed-Power\nMixed-Capacity']

# # Energy savings data (mean values)
# formal_model = [64.58, 78.50, 55.47, 68.99]
# embfd = [64.58, 78.5, 55.47, 67.47]
# ffd = [64.58, 56.53, 51.56, 41.62]

# # Execution time data (list of measurements for each scenario)
# formal_model_times = [
#     [2.6515, 1.7279, 1.7657, 1.7148, 1.8331],  # Fixed-Power Fixed-Capacity
#     [1.6581, 1.6246, 1.6583, 1.6828, 1.7037],  # Mixed-Power Fixed-Capacity
#     [2.2143, 1.83, 1.862, 1.8281, 1.8453],   # Fixed-Power Mixed-Capacity
#     [2.5611, 1.9109, 2.2033, 1.8859, 1.8359]   # Mixed-Power Mixed-Capacity
# ]

# embfd_times = [
#     [0.0634, 0.0654, 0.0645, 0.0654, 0.0649], # Fixed-Power Fixed-Capacity
#     [0.0643, 0.0638, 0.0646, 0.0647, 0.0641], # Mixed-Power Fixed-Capacity
#     [0.0656, 0.0647, 0.0645, 0.0644, 0.065], # Fixed-Power Mixed-Capacity
#     [0.0666, 0.0645, 0.0649, 0.0636, 0.0639]  # Mixed-Power Mixed-Capacity
# ]

# ffd_times = [
#     [0.0584, 0.0578, 0.0577, 0.0579, 0.0575], # Fixed-Power Fixed-Capacity
#     [0.0582, 0.0575, 0.0572, 0.0583, 0.0576], # Mixed-Power Fixed-Capacity
#     [0.0582, 0.057, 0.0583, 0.0575, 0.0587], # Fixed-Power Mixed-Capacity
#     [0.0577, 0.0579, 0.0576, 0.0574, 0.0582]  # Mixed-Power Mixed-Capacity
# ]

# # Function to calculate mean and standard deviation
# def calc_stats(data):
#     return np.mean(data), np.std(data)

# # Calculate statistics
# formal_model_stats = [calc_stats(times) for times in formal_model_times]
# embfd_stats = [calc_stats(times) for times in embfd_times]
# ffd_stats = [calc_stats(times) for times in ffd_times]

# # Create DataFrames
# df_energy = pd.DataFrame({
#     'Scenario': scenarios * 3,
#     'Algorithm': ['Formal Model'] * 4 + ['EMBFD'] * 4 + ['FFD'] * 4,
#     'Energy Savings (%)': formal_model + embfd + ffd
# })

# df_time = pd.DataFrame({
#     'Scenario': scenarios * 3,
#     'Algorithm': ['Formal Model'] * 4 + ['EMBFD'] * 4 + ['FFD'] * 4,
#     'Execution Time (s)': [stat[0] for stat in formal_model_stats + embfd_stats + ffd_stats],
#     'Std Dev': [stat[1] for stat in formal_model_stats + embfd_stats + ffd_stats]
# })

# # Set up the bar charts
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))  # Increased figure width

# # # Energy Savings Plot
# # sns.barplot(x='Scenario', y='Energy Savings (%)', hue='Algorithm', data=df_energy, ax=ax1)
# # ax1.set_ylim(0, 100)

# # # Add value labels on top of each bar for energy savings
# # for container in ax1.containers:
# #     ax1.bar_label(container, fmt='%.2f%%', padding=3, rotation=90)

# # # Move legend outside the plot
# # ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# # Execution Time Plot
# sns.barplot(x='Scenario', y='Execution Time (s)', hue='Algorithm', data=df_time, ax=ax2)

# # Add error bars to the execution time plot
# x_coords = np.arange(len(scenarios))
# width = 0.8 / 3  # Adjust based on the number of algorithms
# for i, alg in enumerate(['Formal Model', 'EMBFD', 'FFD']):
#     data = df_time[df_time['Algorithm'] == alg]
#     ax2.errorbar(x_coords + (i - 1) * width, data['Execution Time (s)'], 
#                  yerr=data['Std Dev'], fmt='none', capsize=5, 
#                  ecolor='black', elinewidth=1.5)

# # Move legend outside the plot
# ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)



# # Adjust layout and save
# plt.tight_layout()
# plt.savefig('throughput.eps', bbox_inches='tight')
# plt.show()





# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd

# # Set the style to a cleaner, more modern look
# sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.6)

# # Data
# scenarios = ['Single Path\nNetfilter', 'Multi-Path\nNetfilter', 
#             'Single Path\nXDP', 'Multi-Path\nXDP']

# # Throughput data
# netfilter_single = [94.5, 95.6, 95.5, 95.6, 95.6]
# netfilter_multi = [94.5, 95.6, 95.5, 95.6, 95.5]
# xdp_single = [95.5, 95.6, 95.6, 95.6, 95.6]
# xdp_multi = [137.8, 145.0, 144.6, 144.6, 138.6]

# # Calculate statistics
# def calc_stats(data):
#     return np.mean(data), np.std(data)

# # Calculate mean and standard deviation for each scenario
# netfilter_single_stats = calc_stats(netfilter_single)
# netfilter_multi_stats = calc_stats(netfilter_multi)
# xdp_single_stats = calc_stats(xdp_single)
# xdp_multi_stats = calc_stats(xdp_multi)

# # Create DataFrame
# df = pd.DataFrame({
#     'Scenario': scenarios,
#     'Throughput (Mbps)': [netfilter_single_stats[0], netfilter_multi_stats[0],
#                          xdp_single_stats[0], xdp_multi_stats[0]],
#     'Std Dev': [netfilter_single_stats[1], netfilter_multi_stats[1],
#                 xdp_single_stats[1], xdp_multi_stats[1]]
# })

# # Set up the bar chart
# plt.figure(figsize=(12, 8))
# ax = sns.barplot(x='Scenario', y='Throughput (Mbps)', data=df)

# # Add error bars
# x_coords = np.arange(len(scenarios))
# plt.errorbar(x_coords, df['Throughput (Mbps)'], 
#             yerr=df['Std Dev'], fmt='none', capsize=5,
#             ecolor='black', elinewidth=1.5)

# # Add value labels on top of each bar
# for i, v in enumerate(df['Throughput (Mbps)']):
#     ax.text(i, v + 1, f'{v:.1f}', ha='center', va='bottom')

# # Customize the plot
# plt.ylim(0, 160)  # Set y-axis limit to accommodate all values plus some padding
# plt.ylabel('Average TCP Throughput (Mbps)')
# plt.title('TCP Throughput Comparison: Single Path vs Multi-Path\nNetfilter vs XDP Implementation')

# # Add a horizontal line at 150 Mbps to indicate max path bandwidth
# plt.axhline(y=150, color='r', linestyle='--', alpha=0.5)
# plt.text(3.1, 151, 'Max Path Bandwidth (150 Mbps)', color='r', alpha=0.7)

# # Adjust layout and save
# plt.tight_layout()
# plt.savefig('tcp_throughput_comparison.eps', bbox_inches='tight', dpi=300)
# plt.show()







# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd

# # Set the style to a cleaner, more modern look
# sns.set_style("whitegrid")
# sns.set_context("paper", font_scale=1.6)

# # Set color palette to match original graph
# colors = sns.color_palette("deep")

# # # Data
# # scenarios = ['Single Path\nNetfilter', 'Unequal Cost Multipath\nNetfilter', 
# #             'Single Path\nXDP', 'Unequal Cost Multipath\nXDP']

# # Data
# scenarios = ['Single Path\n(OSPF)', 
#             'Single Path\n(ElasticRoute)', 'Unequal Cost Multipath\n(ElasticRoute)']

# # Throughput data
# netfilter_single = [94.5, 95.6, 95.5, 95.6, 95.6]
# # netfilter_multi = [94.5, 95.6, 95.5, 95.6, 95.5]
# xdp_single = [95.5, 95.6, 95.6, 95.6, 95.6]
# xdp_multi = [137.8, 145.0, 144.6, 144.6, 138.6]

# # Calculate statistics
# def calc_stats(data):
#     return np.mean(data), np.std(data)

# # Calculate mean and standard deviation for each scenario
# netfilter_single_stats = calc_stats(netfilter_single)
# # netfilter_multi_stats = calc_stats(netfilter_multi)
# xdp_single_stats = calc_stats(xdp_single)
# xdp_multi_stats = calc_stats(xdp_multi)


# # Exclude multi-path Netfilter data, as it doesn't really make sense to have it (since it doesn't do UCMP).
# # # Create DataFrame
# # df = pd.DataFrame({
# #     'Scenario': scenarios,
# #     'Throughput (Mbps)': [netfilter_single_stats[0], netfilter_multi_stats[0],
# #                          xdp_single_stats[0], xdp_multi_stats[0]],
# #     'Std Dev': [netfilter_single_stats[1], netfilter_multi_stats[1],
# #                 xdp_single_stats[1], xdp_multi_stats[1]]
# # })

# # Create DataFrame
# df = pd.DataFrame({
#     'Scenario': scenarios,
#     'Throughput (Mbps)': [netfilter_single_stats[0],
#                          xdp_single_stats[0], xdp_multi_stats[0]],
#     'Std Dev': [netfilter_single_stats[1],
#                 xdp_single_stats[1], xdp_multi_stats[1]]
# })

# # Set up the bar chart
# plt.figure(figsize=(12, 6)) # Was 12, 8
# ax = sns.barplot(x='Scenario', y='Throughput (Mbps)', data=df, color=colors[0])

# # Add error bars
# x_coords = np.arange(len(scenarios))
# plt.errorbar(x_coords, df['Throughput (Mbps)'], 
#             yerr=df['Std Dev'], fmt='none', capsize=5,
#             ecolor='black', elinewidth=1.5)

# # Add value labels on top of each bar with increased padding
# padding = df['Std Dev'].max() * 2.2  # Adjust this multiplier to control label spacing
# for i, v in enumerate(df['Throughput (Mbps)']):
#     ax.text(i, v + padding, f'{v:.1f}', ha='center', va='bottom')

# # Customize the plot
# plt.ylim(0, 160)  # Set y-axis limit to accommodate all values plus some padding
# plt.ylabel('Average TCP Throughput (Mbps)')
# # plt.title('TCP Throughput Comparison: Single Path vs Multipath\nNetfilter vs XDP Implementation')

# # Add a horizontal line at 150 Mbps to indicate max path bandwidth
# plt.axhline(y=150, color='r', linestyle='--', alpha=0.5)
# # Move the bandwidth label to a better position
# plt.text(-0.2, 153, 'Max Multipath Bandwidth (150 Mbps)', color='r', alpha=0.7)

# # Adjust layout and save
# plt.tight_layout()
# plt.savefig('tcp_throughput_comparison.eps', bbox_inches='tight', dpi=300)
# plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set the style to a cleaner, more modern look
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.6)

# Set color palette to match original graph
colors = sns.color_palette("deep")

# Data
scenarios = ['Single Path\n(OSPF)', 
            'Single Path\n(ElasticRoute)', 'Unequal Cost Multipath\n(ElasticRoute)']

# Throughput data
netfilter_single = [94.5, 95.6, 95.5, 95.6, 95.6]
xdp_single = [95.5, 95.6, 95.6, 95.6, 95.6]
xdp_multi = [137.8, 145.0, 144.6, 144.6, 138.6]

# Calculate statistics
def calc_stats(data):
    return np.mean(data), np.std(data)

# Calculate mean and standard deviation for each scenario
netfilter_single_stats = calc_stats(netfilter_single)
xdp_single_stats = calc_stats(xdp_single)
xdp_multi_stats = calc_stats(xdp_multi)

# Create DataFrame
df = pd.DataFrame({
    'Scenario': scenarios,
    'Throughput (Mbps)': [netfilter_single_stats[0],
                         xdp_single_stats[0], xdp_multi_stats[0]],
    'Std Dev': [netfilter_single_stats[1],
                xdp_single_stats[1], xdp_multi_stats[1]]
})

# Set up the bar chart
plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Scenario', y='Throughput (Mbps)', data=df, color=colors[0])

# Remove x-axis label
ax.set_xlabel(None)  # This removes the "Scenario" label

# Add error bars
x_coords = np.arange(len(scenarios))
plt.errorbar(x_coords, df['Throughput (Mbps)'], 
            yerr=df['Std Dev'], fmt='none', capsize=5,
            ecolor='black', elinewidth=1.5)

# Add value labels on top of each bar with increased padding
padding = df['Std Dev'].max() * 2.2
for i, v in enumerate(df['Throughput (Mbps)']):
    ax.text(i, v + padding, f'{v:.1f}', ha='center', va='bottom')

# Customize the plot
plt.ylim(0, 160)
plt.ylabel('Average TCP Throughput (Mbps)')

# Add a horizontal line at 150 Mbps to indicate max path bandwidth
plt.axhline(y=150, color='r', linestyle='--', alpha=0.5)
plt.text(-0.2, 153, 'Max Multipath Bandwidth (150 Mbps)', color='r', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.savefig('tcp_throughput_comparison.eps', bbox_inches='tight', dpi=300)
plt.show()