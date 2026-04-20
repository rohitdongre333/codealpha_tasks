# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

# User input
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

# Calculate investment
if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment =", total)

else:
    print("Stock not found")