Month = ["January", "February", "March"]
TotalSales = [52000.00, 51000.00, 48000.00]
Costs = [46800.00, 45900.00, 43200.00]

for sales, costs, month in list(zip(TotalSales, Costs, Month)):
    profit = sales - costs
    print("", month, "=", profit)
