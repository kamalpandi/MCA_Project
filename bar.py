import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('india_state_data.csv')

# Filter data to only include India
#df = df[df['Country/Region'] == 'India']

# Group data by state and sum the confirmed cases
state_cases = df.groupby(['Province/State'])['Confirmed'].sum()

# Create bar chart
plt.bar(state_cases.index, state_cases.values)
plt.xlabel('State')
plt.ylabel('Confirmed Cases')
plt.title('State-wise Confirmed Cases in India')
plt.xticks(rotation=90)
plt.show()