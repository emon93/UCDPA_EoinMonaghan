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

property_prices = property_prices.set_index('Year')
# Set Index to year on property prices register - Indexing

print(property_prices.head(-5))
# Property prices last 5 lines printed

avg_property_prices = property_prices.groupby(['Year', 'County'])['Price (€)'].mean()
print(avg_property_prices)
# Average house prices grouped by county and sorted by ascending and descending order
