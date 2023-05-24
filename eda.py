import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Load the data into a pandas DataFrame
data = pd.read_csv('new.csv')
data.dropna(inplace=True)


data['FIPS'] = pd.to_datetime(data['FIPS'])
data['FIPS']



# Sort the data by FIPS
sortedVal = pd.to_datetime(data['FIPS'], format="%Y%m%d").sort_values()
sortedVal


# filter the tamilnadu values 

some_value ='Tamil Nadu'

# print(data.head())
# print(data.dtypes)
#sortedDateValue =  data.sort_values(by='FIPS', inplace = True)

data = data.loc[data['Province_State'] == some_value]
data.describe()


x = data['FIPS'].astype(str)
y = data['Active'].astype(str)
plt.scatter(data['FIPS'], data['Active'])
plt.xticks(np.arange(min(data['FIPS']), max(data['FIPS'])+1, 1.0))
plt.xlabel('FIPS')
plt.ylabel('Active')
plt.show()