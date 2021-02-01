import pandas as pd
import numpy as np
# Import pandas and numpy as a package

property_prices = pd.read_csv('/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Property_Price_Register_Ireland-05-04-2019 2.csv')
# Import a CSV file into a Pandas DataFrame

annual_earnings = pd.read_csv('/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Average Total Earnings by Sector.csv')
# Import a second CSV file into a Pandas DataFrame

property_prices['Year'] = pd.DatetimeIndex(property_prices['Date of Sale (dd/mm/yyyy)']).year
property_prices['Price Value'] = (property_prices['Price (€)'].replace( '[\€,)]','', regex=True )
               .replace( '[(]','-',   regex=True ).astype(float))
property_prices['Price Value'].round(decimals=1)
# Add a year only column to property price register by converting an original dates column
# Show year and price column (list included above)
# Add column which includes converted Currency column to float and round figures

avg_property_prices = property_prices.groupby(['Year','County'], as_index=False)['Price Value'].agg(np.mean)
avg_property_prices.columns = ['Year','County', 'Price']
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
# Setting county and year columns as the indices of the dataframe and slicing for the year 2010 and 2019.
# Showing the average house prices per counties for 2010 and 2019 from largest to smallest

full_time_earnings = annual_earnings[annual_earnings['Type of Employment'].str.contains("Full-time")]
avg_wages_per_sector = full_time_earnings.groupby(['Year', 'NACE Rev 2 Economic Sector'], as_index=False)['VALUE'].agg(np.mean)
avg_wages_per_sector.columns = ['Year', 'Job Sector', 'Average Wage']
highest_wages_per_sector = avg_wages_per_sector.sort_values(by='Average Wage', ascending=False).round(0)
highest_wages_per_sector['Job Sector'] = highest_wages_per_sector['Job Sector'].str[0:6]
highest_wages_per_sector1 = highest_wages_per_sector.set_index('Year')
highest_wages_per_sector_2010 = highest_wages_per_sector1.loc[2010]
highest_wages_per_sector_2019 = highest_wages_per_sector1.loc[2019]
print(highest_wages_per_sector_2010)
print(highest_wages_per_sector_2019)
# Filtering for full time workers average earnings
# Showing the average earnings for full time workers per economic sector for 2010 and 2019 and arranging them in order of highest to lowest
# Setting index to year

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.title('Average Wage per Sector in 2010 and incremental increase to 2019')
sns.lineplot(data=highest_wages_per_sector_2010, x='Average Wage', y='Job Sector', alpha=1, label='2010')
sns.lineplot(data=highest_wages_per_sector_2019, x='Average Wage', y='Job Sector', alpha=0.5, label='2019')
fig = plt.figure(figsize=(20,3))

sns.set_theme(style="whitegrid")
plt.title('Top 10 Average Property Prices by County in 2010 and incremental increase to 2019')
plt.xlabel('Price (€)')
sns.scatterplot(data=top_10_counties_10, x='Price', y='County', hue_order=['2010'], alpha=1, label='2010')
sns.scatterplot(data=top_10_counties_19, x='Price', y='County', hue_order=['2019'], alpha=0.5, label='2019')
fig = plt.figure(figsize=(20,3))
plt.show()

highest_wages_per_sector_2019['House Value Affordability'] = (highest_wages_per_sector_2019['Average Wage'] * 1.259 * 2 * 2.5).round(0)
dublin_avg_price_2019 = 418854
westmeath_avg_price_2019 = 180586
meath_avg_price_2019 = 271888

for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= dublin_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')

for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= meath_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')


for x in highest_wages_per_sector_2019['House Value Affordability']:
    if x >= westmeath_avg_price_2019:
        print('Affordable')
    else:
        print('Not affordable')
# Check how many job sectors average wages can afford an average Dublin and Westmeath house price in 2019
# House Affordability figure calculated as gross income doubled for two income earners and by 2.5 times as general rule to afford mortgage

wage_vs_house_price = highest_wages_per_sector_2019.merge(highest_price_per_county_2019, on='Year', how='outer')
print(wage_vs_house_price.head(10))


















































