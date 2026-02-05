# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd
index = 0
# choose countries of interest
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# Load in the data with read_csv()

def plot_region(countriesList, regionName):
  global index
  # get a list unique countries
  
  unique_countries = df['Entity'].unique()

  # Plot the data on a line graph
  for c in unique_countries:
    if c in countriesList:
      
      # match country to one of our we want to look at and get a list of years
      years = df[df['Entity'] == c]['Year']

      # match country to one of our we want to look at and get a list of electriciy values
      sum_elec = df[df['Entity'] == c]['Access']

      plt.plot(years, sum_elec, label=c, marker="o", linestyle="-")
  plt.ylabel('Percentage of Country Population')
  plt.xlabel('Year')
  plt.title( regionName + ': % Population with Electricity Access')
  plt.legend()
  if index < 3:
    plt.figure()
    index+=1

north_south_american_countries = ["Canada", "United States", "Mexico", "Brazil", "Argentina", "Chile"]

european_countries = [
    "Albania",
    "Austria",
    "Belgium",
    "Denmark",
    "Finland",
    "Sweden"
]

asian_countries = ["China", "India", "Japan", "South Korea", "Indonesia", "Vietnam"]

african_countries = ["Nigeria", "Ethiopia", "Egypt", "South Africa", "Kenya", "Ghana"]

plot_region(north_south_american_countries, "America")
plot_region(european_countries, "Europe")
plot_region(asian_countries, "Asia")
plot_region(african_countries, "Africa")
plt.show()