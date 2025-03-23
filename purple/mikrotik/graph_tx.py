#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from datetime import datetime

def load_wireless_stats(filepath, window_size=10):
    """Load and process wireless statistics from CSV"""
    # Read CSV with timezone awareness
    df = pd.read_csv(filepath)
    
    # Convert timestamp string to datetime with NZ timezone
    df['Timestamp'] = pd.to_datetime(df['Timestamp']).dt.tz_localize('Pacific/Auckland')
    
    # Calculate throughput in Mbps from bps values
    df['TX Throughput (Mbps)'] = df['TX bps'] / 1e6
    df['RX Throughput (Mbps)'] = df['RX bps'] / 1e6
    
    # Calculate moving averages
    df['TX Rate MA'] = df['TX Rate (Mbps)'].rolling(window=window_size).mean()
    df['TX Throughput MA'] = df['TX Throughput (Mbps)'].rolling(window=window_size).mean()
    df['RX Rate MA'] = df['RX Rate (Mbps)'].rolling(window=window_size).mean()
    df['RX Throughput MA'] = df['RX Throughput (Mbps)'].rolling(window=window_size).mean()
    
    return df

def plot_tx_rx_analysis(df, output_prefix):
    """Create visualization of TX and RX rates vs throughput with moving averages"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot TX data on top subplot
    ax1.plot(df['Timestamp'], df['TX Rate (Mbps)'], 
             label='TX Rate', color='blue', alpha=0.2)
    ax1.plot(df['Timestamp'], df['TX Throughput (Mbps)'],
             label='TX Throughput', color='red', alpha=0.2)
    ax1.plot(df['Timestamp'], df['TX Rate MA'],
             label='TX Rate (Moving Avg)', color='blue', alpha=0.8)
    ax1.plot(df['Timestamp'], df['TX Throughput MA'],
             label='TX Throughput (Moving Avg)', color='red', alpha=0.8)
    
    ax1.set_ylabel('Mbps')
    ax1.set_title('TX Rate vs Throughput')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot RX data on bottom subplot
    ax2.plot(df['Timestamp'], df['RX Rate (Mbps)'], 
             label='RX Rate', color='blue', alpha=0.2)
    ax2.plot(df['Timestamp'], df['RX Throughput (Mbps)'],
             label='RX Throughput', color='red', alpha=0.2)
    ax2.plot(df['Timestamp'], df['RX Rate MA'],
             label='RX Rate (Moving Avg)', color='blue', alpha=0.8)
    ax2.plot(df['Timestamp'], df['RX Throughput MA'],
             label='RX Throughput (Moving Avg)', color='red', alpha=0.8)
    
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Mbps')
    ax2.set_title('RX Rate vs Throughput')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Rotate x-axis labels for better readability
    plt.setp(ax1.get_xticklabels(), rotation=45)
    plt.setp(ax2.get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_tx_rx_analysis.eps')
    plt.close()

def main():
    parser = argparse.ArgumentParser(
        description='TX/RX Rate vs Throughput Analysis')
    parser.add_argument('stats_file', help='CSV file with wireless statistics')
    parser.add_argument('--output', help='Output prefix for plot files',
                       default='wireless_link')
    parser.add_argument('--window', type=int, default=10,
                       help='Window size for moving average (default: 10)')
    
    args = parser.parse_args()
    
    try:
        # Load wireless stats
        print("Loading wireless statistics...")
        wireless_stats = load_wireless_stats(args.stats_file, args.window)
        
        # Create visualization
        print("Creating visualization...")
        plot_tx_rx_analysis(wireless_stats, args.output)
        
        print(f"Plot saved as {args.output}_tx_rx_analysis.png")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())