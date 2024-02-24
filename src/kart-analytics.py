import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Read csv file
df = pd.read_csv(r'kart-data-example.csv', na_values=['', 'NA', 'N/A', 'NaN'])

# Convert date to datetime format preparing to sort
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Sort dates
df = df.sort_values(by='date')

# Filter track-type
indoor_df = df[df['track-type'] == 'indoor']
outdoor_df = df[df['track-type'] == 'outdoor']

# Function to plot best-time
def plot_best_time():
    indoor_sorted = indoor_df.sort_values(by='best-time',ascending=False)
    outdoor_sorted = outdoor_df.sort_values(by='best-time',ascending=False)
    plt.plot(indoor_sorted['date'], indoor_sorted['best-time'], label='Indoor', marker='o')
    plt.plot(outdoor_sorted['date'], outdoor_sorted['best-time'], label='Outdoor', marker='o')
    plt.title('Best time lap in indoor and outdoor tracks.')
    plt.xlabel('Best time lap')
    plt.ylabel('Date')
    plt.legend()
    plt.savefig('best_time_plot.pdf')  # Save as PDF
    plt.show()

# Function to plot avg-time
def plot_avg_time():
    plt.figure(figsize=(10, 6))
    indoor_sorted = indoor_df.sort_values(by='avg-time',ascending=False)
    outdoor_sorted = outdoor_df.sort_values(by='avg-time',ascending=False)
    plt.plot(indoor_sorted['date'], indoor_sorted['avg-time'], label='Indoor', marker='o')
    plt.plot(outdoor_sorted['date'], outdoor_sorted['avg-time'], label='Outdoor', marker='o')
    plt.title('Average time lap in indoor and outdoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Average time lap')
    plt.legend()
    plt.savefig('avg_time_plot.pdf')  # Save as PDF
    plt.show()

# Function to plot avg speed
def plot_avg_speed():
    plt.figure(figsize=(10, 6))
    plt.plot(indoor_df['date'], indoor_df['avg-speed'], label='Indoor', marker='o')
    plt.plot(outdoor_df['date'], outdoor_df['avg-speed'], label='Outdoor', marker='o')
    plt.title('Average speed in indoor and outdoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Average speed')
    plt.legend()
    plt.savefig('avg_speed_plot.pdf')  # Save as PDF
    plt.show()

# Function to plot best and avg time for every track location
def plot_best_avg_track_names():
    track_names = df['track-name'].unique()
    for track_name in track_names:
        track_best = df[df['track-name'] == track_name].sort_values(by='best-time',ascending=False)
        track_avg = df[df['track-name'] == track_name].sort_values(by='avg-time',ascending=False)
        plt.figure(figsize=(10, 6))
        plt.plot(track_best['date'], track_best['best-time'], label='Best Time', marker='o')
        plt.plot(track_avg['date'], track_avg['avg-time'], label='Average Time', marker='o')
        plt.title(f'Best and Average time lap in {track_name}')
        plt.xlabel('Date')
        plt.ylabel('Time')
        plt.legend()
        plt.savefig(f'{track_name}_time_plot.pdf')  # Save as PDF
        plt.show()

def plot_avg_speed_track_names():
    track_names = df['track-name'].unique()
    for track_name in track_names:
        track_df = df[df['track-name'] == track_name]
        plt.figure(figsize=(10, 6))
        plt.plot(track_df['date'], track_df['avg-speed'], label='Average Speed', marker='o')
        plt.title(f'Average Speed in {track_name}')
        plt.xlabel('Date')
        plt.ylabel('Time')
        plt.legend()
        plt.savefig(f'{track_name}_speed_plot.pdf')  # Save as PDF
        plt.show()

# Main loop for textual menu
while True:
    print("Menu:")
    print("1) Show best-time indoor/outdoor tracks.")
    print("2) Show avg-time indoor/outdoor tracks.")
    print("3) Show avg-speed in indoor/outdoor tracks.")
    print("4) Show best-time and avg time per track-name")
    print("5) Show avg-speed and avg time per track-name")
    print("6) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        plot_best_time()
    elif choice == '2':
        plot_avg_time()
    elif choice == '3':
        plot_avg_speed()
    elif choice == '4':
        plot_best_avg_track_names()
    elif choice == '5':
        plot_avg_speed_track_names()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
