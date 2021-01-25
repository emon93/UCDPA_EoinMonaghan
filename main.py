import pandas as pd
# Import pandas as a package

property_prices = pd.read_csv('/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Property_Price_Register_Ireland-05-04-2019 2.csv')
# Import a CSV file into a Pandas DataFrame

annual_earnings = pd.read_csv('/Users/eoinmonaghan/PycharmProjects/UCDRubricProject/Average Total Earnings .csv')
# Import a second CSV file into a Pandas DataFrame

print(property_prices.head(5))
print(annual_earnings.head(5))
# Check data is readable

property_prices['Year'] = pd.DatetimeIndex(property_prices['Date of Sale (dd/mm/yyyy)']).year
# Add a year only column to property price register by converting an orginal dates column

print(property_prices[['Year', 'Price (€)']].head(5))
# Show year and price column (list included above)

property_prices = property_prices.set_index(['Year'])
# Set indexes to year and county on property prices register - Indexing

print(property_prices.head(-5))
# Property prices last 5 lines printed

property_prices['Price Value'] = (property_prices['Price (€)'].replace( '[\€,)]','', regex=True )
               .replace( '[(]','-',   regex=True ).astype(float))
property_prices['Price Value'].round(decimals=1)
print(property_prices['Price Value'].head(5))
# Add column which includes converted Currency column to float and round figures

avg_property_prices = property_prices.groupby('County', as_index=True)['Price Value'].mean()
highest_avg_price = avg_property_prices.sort_values(ascending=False).round(0)
print(highest_avg_price)
# Average house prices grouped by county between 2010 and 2019 and sorted in descending order in terms of average prices
# Dublin and the commuter counties are at the top of the list showing the demand to be close to the city

price_dif1 = avg_property_prices.loc['Dublin'] - avg_property_prices.loc['Westmeath']
price_dif1.astype(int)
print(price_dif1.round(0))
# Comparing Dublin and Westmeath counties average house prices over the last 10 years (using loc)
# Dublin houses are on average c.241k more expensive than Athlone houses

print(highest_avg_price.iloc[0] - highest_avg_price.iloc[-1])
# Comparing highest and lowest average house prices over the last 10 years (using iloc)
# The highest is Dublin abd lowest is Longford as noted from the sorted list previously



# Filtering for full time workers average earnings




