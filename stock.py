# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0
portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        value = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += value

        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

    except ValueError:
        print("Please enter a valid quantity.")

# Display portfolio
print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares = ${value}")

print("-----------------------------")
print(f"Total Investment: ${total_investment}")

# Optional: Save result to text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== STOCK PORTFOLIO =====\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares = ${value}\n"
            )

        file.write("-----------------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved successfully to portfolio.txt")
else:
    print("Portfolio not saved.")