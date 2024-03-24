import pandas as pd
from functions import *

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


# Main menu
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
        plot_best_time_indoor(indoor_df)
        plot_best_time_outdoor(outdoor_df)
    elif choice == '2':
        plot_avg_time_indoor(indoor_df)
        plot_avg_time_outdoor(outdoor_df)
    elif choice == '3':
        plot_avg_speed(indoor_df,outdoor_df)
    elif choice == '4':
        plot_best_avg_track_names(df)
    elif choice == '5':
        plot_avg_speed_track_names(df)
    elif choice == '6':
        all_best_time(df)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
