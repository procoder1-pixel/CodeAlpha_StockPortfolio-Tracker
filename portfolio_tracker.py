import csv

def stock_portfolio():
    # Hardcoded stock prices per CodeAlpha scope
    prices = {"AAPL": 180.0, "TSLA": 250.0, "GOOG": 135.0, "AMZN": 140.0, "MSFT": 420.0}
    portfolio = {}

    print("📊 Stock Portfolio Tracker (CodeAlpha Task 2)")
    print("Available symbols:", ", ".join(sorted(prices)))

    while True:
        sym = input("Enter stock symbol (or 'done'): ").upper().strip()
        if sym == "DONE":
            break
        if sym not in prices:
            print("❌ Unknown symbol. Choose from the list above.")
            continue
        try:
            qty = int(input(f"Enter quantity of {sym}: ").strip())
            if qty <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Please enter a whole number for quantity.")
            continue
        portfolio[sym] = portfolio.get(sym, 0) + qty

    if not portfolio:
        print("No positions entered.")
        return

    total = 0.0
    rows = []
    print("\n💼 Portfolio Summary")
    for sym, qty in portfolio.items():
        price = prices[sym]
        value = qty * price
        total += value
        rows.append([sym, qty, f"{price:.2f}", f"{value:.2f}"])
        print(f"{sym}: {qty} × ${price:.2f} = ${value:.2f}")
    print(f"\n📈 Total Portfolio Value = ${total:.2f}")

    save = input("Save summary to CSV? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            writer.writerows(rows)
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
        print("✅ Saved to portfolio_summary.csv")

if __name__ == "__main__":
    stock_portfolio()
