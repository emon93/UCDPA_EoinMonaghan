import pandas as pd
import numpy as np
# Import pandas and numpy as packages

property_prices = pd.read_csv(
    '/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Property_Price_Register_Ireland-05-04-2019 2.csv')
# Import a CSV file into a Pandas DataFrame

annual_earnings = pd.read_csv(
    '/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Average Total Earnings by Sector.csv')
# Import a second CSV file into a Pandas DataFrame

property_prices['Year'] = pd.DatetimeIndex(property_prices['Date of Sale (dd/mm/yyyy)']).year
property_prices['Price Value'] = (property_prices['Price (€)'].replace('[\€,)]', '', regex=True)
                                  .replace('[(]', '-', regex=True).astype(float))
property_prices['Price Value'].round(decimals=1)
# Add a year only column to property price register by converting an original dates column
# Show year and price column (list included above)
# Add column which includes converted currency types to float types and round figures

avg_property_prices = property_prices.groupby(['Year', 'County'], as_index=False)['Price Value'].agg(np.mean)
avg_property_prices.columns = ['Year', 'County', 'Price']
highest_price_per_county = avg_property_prices.sort_values(by='Price', ascending=False).round(0)
highest_price_per_county1 = highest_price_per_county.set_index('Year')
highest_price_per_county_2010 = highest_price_per_county1.loc[2010]
highest_price_per_county_2019 = highest_price_per_county1.loc[2019]
print(highest_price_per_county_2010)
print(highest_price_per_county_2019)
top_10_counties_10 = highest_price_per_county_2010.iloc[0:9]
bottom_10_counties_10 = highest_price_per_county_2010.iloc[-11:-1]
top_10_counties_19 = highest_price_per_county_2019.iloc[0:9]
bottom_10_counties_19 = highest_price_per_county_2019.iloc[-11:-1]
# Showing the average house prices per counties for 2010 and 2019 sorting the values from largest to smallest
# Setting year column as the index of the dataframe and slicing for the year 2010 and 2019
# Getting the top and bottom 10 counties in terms of average prices from this list

full_time_earnings = annual_earnings[annual_earnings['Type of Employment'].str.contains("Full-time")]
avg_wages_per_sector = full_time_earnings.groupby(['Year', 'NACE Rev 2 Economic Sector'], as_index=False)['VALUE'].agg(
    np.mean)
avg_wages_per_sector.columns = ['Year', 'Job Sector', 'Average Wage']
highest_wages_per_sector = avg_wages_per_sector.sort_values(by='Average Wage', ascending=False).round(0)
highest_wages_per_sector['Job Sector'] = highest_wages_per_sector['Job Sector'].str[0:6]
highest_wages_per_sector1 = highest_wages_per_sector.set_index('Year')
highest_wages_per_sector_2010 = highest_wages_per_sector1.loc[2010]
highest_wages_per_sector_2019 = highest_wages_per_sector1.loc[2019]
print(highest_wages_per_sector_2010)
print(highest_wages_per_sector_2019)
# Filtering for full time workers average earnings, removing part time earnings etc.
# Showing the average earnings for full time workers per economic sector and arranging them in order of highest to lowest
# Setting index to year and slicing for the year 2010 and 2019

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# Import matplotlib and seaborn libraries to produce the below graphs

sns.set_theme(style="whitegrid")
plt.title('Top 10 Average Property Prices by County in 2010 and incremental increase to 2019')
plt.xlabel('Average Price in €')
plt.ylabel('County')
sns.scatterplot(data=top_10_counties_10, x='Price', y='County', alpha=1, label='2010')
sns.scatterplot(data=top_10_counties_19, x='Price', y='County', alpha=0.5, label='2019')
fig = plt.figure(figsize=(20, 3))
plt.show()
# Graph 1 relating to average property prices per the top 10 counties in 2010 and the incremental increases in average prices from 2010 to 2019

sns.set_theme(style="whitegrid")
plt.title('Average Wage per Sector in 2010 and incremental increase to 2019')
plt.xlabel("Average Wage in €")
plt.ylabel('Job Sector')
sns.scatterplot(data=highest_wages_per_sector_2010, x='Average Wage', y='Job Sector', alpha=1, label='2010')
sns.scatterplot(data=highest_wages_per_sector_2019, x='Average Wage', y='Job Sector', alpha=0.5, label='2019')
fig = plt.figure(figsize=(20, 3))
plt.show()
# Graph 2 relating to average wages per each sector in 2010 and the incremental increases in average wages from 2010 to 2019

highest_wages_per_sector_2019['House Value Affordability'] = (highest_wages_per_sector_2019['Average Wage'] * 1.259 * 2 * 2.5).round(0)
# House Affordability column created
# House affordability column values are calculated as the average wage*average net tax*2 income earners*2.5 times (general rule for affording mortgage on gross income)

wage_vs_house_price = highest_wages_per_sector_2019.merge(highest_price_per_county_2019, on='Year', how='outer')
wage_vs_house_price_2019 = wage_vs_house_price.loc[2019]
Total_house_prices_2019 = wage_vs_house_price_2019['Price'].sum()
Total_Affordability_2019 = wage_vs_house_price_2019['House Value Affordability'].sum()
print("The difference between average house prices and worker affordability is", Total_house_prices_2019 - Total_Affordability_2019)
# Merging the average wage and pandas dataframes to show a comparison between average house affordability and average house prices
# Summing total house prices and the average workers affordability - noting a big difference below

dublin_avg_price_2019 = 418854
westmeath_avg_price_2019 = 180586
meath_avg_price_2019 = 271888
# Storing average house price values into variable names from the data obtained above

def afforable():
    print("New loop")

afforable()
for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= dublin_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')

afforable()
for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= meath_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')
afforable()
for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= westmeath_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')
print('End of for loops review')
# Defining a function to mark different for loops above
# Loop argument performed to check how many job sectors average wages can afford the average Dublin, Meath and Westmeath house prices in 2019

