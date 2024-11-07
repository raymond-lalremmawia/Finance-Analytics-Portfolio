import yfinance as yf
import pandas as pd

# Define the stock symbol for Disney
symbol = 'DIS'

# Set the start and end dates for the data (16th November 2021 to 16th November 2023)
start_date = '2021-11-16'
end_date = '2023-11-16'

# Download Disney's stock data
disney_data = yf.download(symbol, start=start_date, end=end_date, interval='1mo')

# Display the first few rows of the data to check
print(disney_data.head())

# Save the data to a CSV file (optional)
disney_data.to_csv('Disney_Historical_Monthly_Prices.csv')
