# Simple profit margin calculator

revenue = float(input("Enter revenue in EUR: "))
costs = float(input("Enter costs in EUR: "))

profit = revenue - costs
if revenue != 0:
    margin = profit / revenue * 100
else:
    margin = 0.0

print(f"Profit: {profit:.2f} EUR")
print(f"Profit margin: {margin:.2f}%")
