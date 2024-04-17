import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(10, 6)})

# Function to plot best-time in indoor tracks
def plot_best_time_indoor(indoor_df):
    indoor_df.loc[:, 'date_numeric'] = mdates.date2num(indoor_df['date'])
    ax = sns.regplot(data=indoor_df, x="date_numeric", y="best-time")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('Best time lap in indoor tracks.')
    plt.xlabel("Date")
    plt.ylabel("Best Time Indoor")
    plt.show()


# Function to plot best-time in outdoor tracks
def plot_best_time_outdoor(outdoor_df):
    outdoor_df.loc[:, 'date_numeric'] = mdates.date2num(outdoor_df['date'])
    ax = sns.regplot(data=outdoor_df, x="date_numeric", y="best-time")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('Best time lap in outdoor tracks.')
    plt.xlabel("Date")
    plt.ylabel("Best Time Outdoor")
    plt.show()
    
# Function to plot avg-time in indoor tracks
def plot_avg_time_indoor(indoor_df):
    indoor_df.loc[:, 'date_numeric'] = mdates.date2num(indoor_df['date'])
    ax = sns.regplot(data=indoor_df, x="date_numeric", y="avg-time")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('Average time lap in indoor tracks.')
    plt.xlabel("Date")
    plt.ylabel("Average Time Indoor")
    plt.show()

# Function to plot avg-time in outdoor tracks
def plot_avg_time_outdoor(outdoor_df):
    outdoor_df.loc[:, 'date_numeric'] = mdates.date2num(outdoor_df['date'])
    ax = sns.regplot(data=outdoor_df, x="date_numeric", y="avg-time")
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('Average time lap in outdoor tracks.')
    plt.xlabel("Date")
    plt.ylabel("Average Time Outdoor")
    plt.show()

# Function to plot best and avg time for every track location
def plot_best_avg_track_names(df):
    track_names = df['track-name'].unique()
    for track_name in track_names:
        track_best = df[(df['track-name'] == track_name) & (df['condition'] == 'standard')]
        track_avg = df[(df['track-name'] == track_name) & (df['condition'] == 'standard')]
        plt.figure(figsize=(12, 6))
        track_best.loc[:,'date_numeric'] = mdates.date2num(track_best['date'])
        ax = sns.regplot(data=track_best, x="date_numeric", y="best-time")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.title(f'Best Time lap in {track_name}')
        plt.xlabel("Date")
        plt.ylabel("Best Time")
        plt.show()
        
        
        track_avg.loc[:,'date_numeric'] = mdates.date2num(track_avg['date'])
        ax = sns.regplot(data=track_avg, x="date_numeric", y="avg-time")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.title(f'Average Time lap in {track_name}')
        plt.xlabel("Date")
        plt.ylabel("Average Time")
        plt.show()

# Function to plot avg speed
def plot_avg_speed(indoor_df,outdoor_df):
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
def plot_avg_speed_track_names(df):
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

# Function to show all best time for every track directly on terminal
def all_best_time(df):
    idx_miglior_tempo = df.groupby('track-name')['best-time'].idxmin()
    print("#####################################")
    for idx in idx_miglior_tempo:
        print(df.loc[idx])
        print("#####################################")

