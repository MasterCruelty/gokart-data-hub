import pandas as pd
import matplotlib.pyplot as plt

# Rea csv file
df = pd.read_csv(r'kart-data-example.csv', na_values=['', 'NA', 'N/A', 'NaN'])


# Convert date to datetime format preparing to sort
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Sort dates
df = df.sort_values(by='date')

# Filter track-type
indoor_df = df[df['track-type'] == 'indoor']
outdoor_df = df[df['track-type'] == 'outdoor']

# Plot best-time
plt.figure(figsize=(10, 6))
plt.plot(indoor_df['date'], indoor_df['best-time'], label='Indoor', marker='o')
plt.plot(outdoor_df['date'], outdoor_df['best-time'], label='Outdoor', marker='o')
plt.title('Best time lap in indoor and outdoor tracks.')
plt.xlabel('Date')
plt.ylabel('Best time lap')
plt.legend()
plt.savefig('best_time_plot.pdf')  # Save as PDF
plt.show()

# Plot avg-time
plt.figure(figsize=(10, 6))
plt.plot(indoor_df['date'], indoor_df['avg-time'], label='Indoor', marker='o')
plt.plot(outdoor_df['date'], outdoor_df['avg-time'], label='Outdoor', marker='o')
plt.title('Average time lap in indoor and outdoor tracks.')
plt.xlabel('Date')
plt.ylabel('Average time lap')
plt.legend()
plt.savefig('avg_time_plot.pdf')  # Save as PDF
plt.show()

# Plot avg speed
plt.figure(figsize=(10, 6))
plt.plot(indoor_df['date'], indoor_df['avg-speed'], label='Indoor', marker='o')
plt.plot(outdoor_df['date'], outdoor_df['avg-speed'], label='Outdoor', marker='o')
plt.title('Average speed in indoor and outdoor tracks.')
plt.xlabel('Date')
plt.ylabel('Average speed')
plt.legend()
plt.savefig('avg_speed_plot.pdf')  # Save as PDF
plt.show()
