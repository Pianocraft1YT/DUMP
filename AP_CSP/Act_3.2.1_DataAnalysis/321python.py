# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = pd.read_csv("temperature_data.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
# CODE TO ADD
plt.plot(temp_data['Year'], temp_data['Anomaly'],color='gray')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='blue')
# TODO #3: Plot LOWESS in a line graph

plt.figure()
# TODO #4: Use matplotlib to make a bar chart
# CODE TO ADD
# TODO #4: Use matplotlib to make a bar chart
plt.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.bar(temp_data['Year'], temp_data['LOWESS'], color='yellow')


# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
# CODE TO ADD
#TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0


# find the min, max and calculate the sum
for i in range(len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] < min_anomaly):
    min_anomaly = temp_data['Anomaly'][i]
    min_year = temp_data['Year'][i]
for i in range(len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] > max_anomaly):
    max_anomaly = temp_data['Anomaly'][i]
    max_year = temp_data['Year'][i]
for i in range(len(temp_data['Anomaly'])):
  sum_anomaly += temp_data['Anomaly'][i]
print(sum_anomaly)
avg_anomaly = (sum_anomaly/len(temp_data['Anomaly']))
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)

print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)

print("The average anomaly is:", avg_anomaly)
plt.figure()
def check(i):
  if ((temp_data['Average'][i] != -99.99) and (temp_data['#Days'][i] != -1)):
    return True
  else:
    return False
list_average = []
list_years = []
list_days = []
temp_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row
for i in range (len(temp_data['Average'])):
  if check(i):
    list_average.append(temp_data['Average'][i])
    list_years.append(temp_data["decimal_year"][i])
    list_days.append(temp_data['#Days'][i])
  i+=1
plt.plot(list_years, list_average)
plt.bar(list_years, list_days)
plt.xlabel("Year")
plt.ylabel("Average Co2")
plt.show()