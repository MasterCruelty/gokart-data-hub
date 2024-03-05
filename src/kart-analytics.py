import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.dates as mdates

# Read csv file
df = pd.read_csv(r'kart-data-example.csv', na_values=['', 'NA', 'N/A', 'NaN'])

# Convert date to datetime format preparing to sort
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

#convert best-time and avg-time to float 
df['best-time'] = df['best-time'].str.replace(',', '.').astype(float)
df['avg-time'] = df['avg-time'].str.replace(',', '.').astype(float)
# Sort dates
df = df.sort_values(by='date')

# Filter track-type
indoor_df = df[df['track-type'] == 'indoor']
outdoor_df = df[df['track-type'] == 'outdoor']


# Function to plot best-time in indoor tracks
def plot_best_time_indoor():
    indoor_df['date_numeric'] = mdates.date2num(indoor_df['date'])
    ax = sns.regplot(data=indoor_df, x="date_numeric", y="best-time")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    

# Function to plot best-time in outdoor tracks
def plot_best_time_outdoor():
    plt.figure(figsize=(12, 6))
    plt.plot(outdoor_df['date'], outdoor_df['best-time'], label='Outdoor', marker='o')
    plt.title('Best time lap in outdoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Best time lap')
    plt.legend()
    plt.savefig('best_time_plot_outdoor.pdf')  # Save as PDF
    plt.show()


# Function to plot avg-time in indoor tracks
def plot_avg_time_indoor():
    plt.figure(figsize=(12, 6))
    plt.plot(indoor_df['date'], indoor_df['avg-time'], label='Indoor', marker='o')
    plt.title('Average time lap in indoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Average time lap')
    plt.legend()
    plt.savefig('avg_time_plot_indoor.pdf')  # Save as PDF
    plt.show()

# Function to plot avg-time in outdoor tracks
def plot_avg_time_outdoor():
    plt.figure(figsize=(12, 6))
    plt.plot(outdoor_df['date'], outdoor_df['avg-time'], label='Outdoor', marker='o')
    plt.title('Average time lap in outdoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Average time lap')
    plt.legend()
    plt.savefig('avg_time_plot_outdoor.pdf')  # Save as PDF
    plt.show()


# Function to plot best and avg time for every track location
def plot_best_avg_track_names():
    track_names = df['track-name'].unique()
    for track_name in track_names:
        track_best = df[df['track-name'] == track_name]
        track_avg = df[df['track-name'] == track_name]
        plt.figure(figsize=(12, 6))
        plt.plot(track_best['date'], track_best['best-time'], label='Best Time', marker='o')
        plt.plot(track_avg['date'], track_avg['avg-time'], label='Average Time', marker='o')
        plt.title(f'Best and Average time lap in {track_name}')
        plt.xlabel('Date')
        plt.ylabel('Time')
        plt.legend()
        plt.savefig(f'{track_name}_time_plot.pdf')  # Save as PDF
        plt.show()


# Function to plot avg speed
def plot_avg_speed():
    plt.figure(figsize=(12, 6))
    indoor_speed = indoor_df[indoor_df['avg-speed'] != 0]
    outdoor_speed = outdoor_df[outdoor_df['avg-speed'] != 0]
    plt.plot(indoor_speed['date'], indoor_speed['avg-speed'], label='Indoor', marker='o')
    plt.plot(outdoor_speed['date'], outdoor_speed['avg-speed'], label='Outdoor', marker='o')
    plt.title('Average speed in indoor and outdoor tracks.')
    plt.xlabel('Date')
    plt.ylabel('Average speed')
    plt.legend()
    plt.savefig('avg_speed_plot.pdf')  # Save as PDF
    plt.show()

# Function to plot avg speed for every track location
def plot_avg_speed_track_names():
    track_names = df['track-name'].unique()
    for track_name in track_names:
        track_df = df[df['track-name'] == track_name]
        if (track_df['avg-speed'] == 0).any():
            continue
        plt.figure(figsize=(10, 6))
        plt.plot(track_df['date'], track_df['avg-speed'], label='Average Speed', marker='o')
        plt.title(f'Average Speed in {track_name}')
        plt.xlabel('Date')
        plt.ylabel('Time')
        plt.legend()
        plt.savefig(f'{track_name}_speed_plot.pdf')  # Save as PDF
        plt.show()

def all_best_time():
    idx_miglior_tempo = df.groupby('track-name')['best-time'].idxmin()
    print("#####################################")
    for idx in idx_miglior_tempo:
        print(df.loc[idx])
        print("#####################################")

# Main loop for textual menu
while True:
    print("Menu:")
    print("1) Plot best-time indoor/outdoor tracks.")
    print("2) Plot avg-time indoor/outdoor tracks.")
    print("3) Plot avg-speed in indoor/outdoor tracks.")
    print("4) Plot best-time and avg time for every track-name")
    print("5) Plot avg-speed for every track-name")
    print("6) Show your best-time of all time for every track location.")
    print("7) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        #slope,intercept = perform_linear_regression(indoor_df)
        plot_best_time_indoor()
        plot_best_time_outdoor()
    elif choice == '2':
        plot_avg_time_indoor()
        plot_avg_time_outdoor()
    elif choice == '3':
        plot_avg_speed()
    elif choice == '4':
        plot_best_avg_track_names()
    elif choice == '5':
        plot_avg_speed_track_names()
    elif choice == '6':
        all_best_time()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
