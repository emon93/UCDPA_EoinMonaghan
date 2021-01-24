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

property_prices = property_prices.set_index(['Year','County'])
# Set indexes to year and county on property prices register - Indexing

print(property_prices.head(-5))
# Property prices last 5 lines printed

property_prices['Price Value'] = (property_prices['Price (€)'].replace( '[\€,)]','', regex=True )
               .replace( '[(]','-',   regex=True ).astype(float))
property_prices['Price Value'].round(decimals=1)
print(property_prices['Price Value'].head(5))
# Add column which includes converted Currency column to float and round figures

avg_property_prices = property_prices.groupby('County', as_index=True)['Price Value'].mean()
# Average house prices grouped by county between 2010 and 2019

avg_dif_price = avg_property_prices.loc['Dublin'] - avg_property_prices.loc['Westmeath']
avg_dif_price.astype(int)
print(avg_dif_price.round(0))
# Comparing Dublin and Westmeath counties average house prices over the last 10 years (using loc)
# Dublin houses are on average c.241k more expensive



