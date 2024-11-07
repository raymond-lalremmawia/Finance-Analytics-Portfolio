import yfinance as yf
import matplotlib.pyplot as plt

aapl = yf.Ticker ("aapl")

stockinfo = aapl.info

for key, value in stockinfo.items():
    print(key, ":", value)

financials_data = aapl.financials

print("\nFinancial Statement Data:")
print(financials_data)

# Get quarterly financial data for more recent revenue data
quarterly_financials = aapl.quarterly_financials
quarterly_revenue = quarterly_financials.loc['Total Revenue']

# Plot Quarterly Revenue as a bar chart
plt.figure(figsize=(12, 6))
plt.bar(quarterly_revenue.index, quarterly_revenue.values, color='skyblue')

# Add plot titles and labels
plt.title("Apple's Quarterly Revenue (Recent Quarters)")
plt.xlabel("Date")
plt.ylabel("Revenue (USD in billions)")
plt.grid(True)
plt.show()
