import pandas as pd
# Import pandas as a package

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

property_prices = property_prices.set_index(['Year', 'County'])
prices_2010 = property_prices.loc[2010]
prices_2019 = property_prices.loc[2019]
avg_property_prices_2010 = prices_2010.groupby('County', as_index=True)['Price Value'].mean()
avg_property_prices_2019 = prices_2019.groupby('County', as_index=True)['Price Value'].mean()
highest_avg_price_2010 = avg_property_prices_2010.sort_values(ascending=False).round(0)
highest_avg_price_2019 = avg_property_prices_2019.sort_values(ascending=False).round(0)
print(highest_avg_price_2010.round(0))
print(highest_avg_price_2019.round(0))
# Setting county and year columns as the indices of the dataframe and slicing for the year 2010 and 2019.
# Showing the average house prices per counties for 2010 and 2019 in ascending order

price_dif1 = avg_property_prices_2019.loc['Dublin'] - avg_property_prices_2019.loc['Westmeath']
price_dif1.astype(int)
print('The difference between Dublin and Westmeath average house prices in 2019 is', price_dif1.round(0), 'euros.')
# Comparing Dublin and Westmeath counties average house prices in 2019.
# Dublin houses are a lot more expensive than Westmeath houses

full_time_annual_earnings = annual_earnings[annual_earnings['Type of Employment'].str.contains("Full-time")]
full_time_annual_earnings1 = full_time_annual_earnings.set_index(['Year' ,'NACE Rev 2 Economic Sector'])
earnings_2010 = full_time_annual_earnings1.loc[2010]
earnings_2019 = full_time_annual_earnings1.loc[2019]
avg_earnings_per_sector_2010 = earnings_2010.groupby('NACE Rev 2 Economic Sector', as_index=True)['VALUE'].mean()
avg_earnings_per_sector_2019 = earnings_2019.groupby('NACE Rev 2 Economic Sector', as_index=True)['VALUE'].mean()
# Filtering for full time workers average earnings
# Setting economic sector and year as the index of the dataframe and slicing for the year 2010 and 2019.
# Showing the average earnings for full time workers per economic sector for 2010 and 2019

avg_earnings_per_sector_2010['Mortgage_value'] = avg_earnings_per_sector_2010 * 1.259 * 2.5
avg_earnings_per_sector_2019['Mortgage_value'] = avg_earnings_per_sector_2019 * 1.259 * 2.5
print(avg_earnings_per_sector_2010['Mortgage_value'].round(0))
print(avg_earnings_per_sector_2019['Mortgage_value'].round(0))
# Add a gross income col and multiply by 2.5 times to see what mortgage one can afford based on average wage for 2010 and 2019
# To get a gross income figure, add 25.9% (net average tax deductions) to the average earnings (after tax) figure
# Multiply this gross income figure by 2.5 times to see what mortgages one can afford


Econ_sectors = ['Business', 'ICT', 'Education', 'Construction', 'Health']
Mortgage_afford_2010 = [175256, 166877, 164526, 130193, 153025]
Mortgage_afford_2019 = [205510, 212642, 173896, 142179, 148521]
Counties = ['Dublin', 'Wicklow', 'Cork', 'Westmeath', 'Longford']
Avg_property_prices_2010_list = [333028, 293963, 230115, 160580, 136420]
Avg_Property_Prices_2019_list = [418854, 319021, 275251, 180586,120483]
# Lists created based on data obtained from above

import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x=Econ_sectors, y=Mortgage_afford_2010, alpha=0.5)
plt.show()



















