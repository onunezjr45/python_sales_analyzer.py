import csv

total_revenue = 0

revenue_per_product = {}
quantity_per_product = {}
revenue_per_day = {}


with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        product = row["product"]

        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price

        # Total revenue
        total_revenue += revenue

        # Revenue per product
        if product not in revenue_per_product:
            revenue_per_product[product] = 0

        revenue_per_product[product] += revenue

        # Quantity per product
        if product not in quantity_per_product:
            quantity_per_product[product] = 0

        quantity_per_product[product] += quantity

        # Revenue per day
        if date not in revenue_per_day:
            revenue_per_day[date] = 0

        revenue_per_day[date] += revenue


# Find the day with the highest revenue
highest_revenue_day = None
highest_daily_revenue = 0

for date, revenue in revenue_per_day.items():
    if revenue > highest_daily_revenue:
        highest_daily_revenue = revenue
        highest_revenue_day = date


# Write sales_report.txt
with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("====================\n")

    file.write(f"Total Revenue: ${total_revenue:.2f}\n\n")

    file.write("Revenue Per Product\n")

    for product, revenue in revenue_per_product.items():
        file.write(f"{product}: ${revenue:.2f}\n")

    file.write("\nTotal Quantity Sold Per Product\n")

    for product, quantity in quantity_per_product.items():
        file.write(f"{product}: {quantity}\n")

    file.write("\nHighest Revenue Day\n")
    file.write(
        f"{highest_revenue_day}: ${highest_daily_revenue:.2f}\n"
    )


# Write product_summary.csv
with open("product_summary.csv", "w", newline="") as file:
    fieldnames = [
        "product",
        "total_quantity",
        "total_revenue"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for product in revenue_per_product:
        writer.writerow({
            "product": product,
            "total_quantity": quantity_per_product[product],
            "total_revenue": f"{revenue_per_product[product]:.2f}"
        })


print("Sales analysis complete.")
print("Created sales_report.txt")
print("Created product_summary.csv")