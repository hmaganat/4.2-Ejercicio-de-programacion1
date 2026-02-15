"""
computeSales.py

Computes total sales cost using a price catalogue
and a sales record file (JSON format).
"""

import sys
import json
import time


def load_json_file(filename):
    """Load JSON file safely."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contains invalid JSON.")
        return None


def build_price_dictionary(price_catalogue):
    """Build dictionary of product prices."""
    prices = {}

    for item in price_catalogue:
        try:
            product = item["product"]
            price = float(item["price"])
            prices[product] = price
        except (KeyError, ValueError, TypeError):
            print(f"Invalid product entry detected: {item}")

    return prices


def compute_total_sales(prices, sales_record):
    """Compute total cost of all sales."""
    total_cost = 0.0

    for sale in sales_record:
        try:
            product = sale["product"]
            quantity = int(sale["quantity"])

            if product not in prices:
                print(f"Warning: Product '{product}' not found in catalogue.")
                continue

            total_cost += prices[product] * quantity

        except (KeyError, ValueError, TypeError):
            print(f"Invalid sale entry detected: {sale}")

    return total_cost


def save_results(total_cost, elapsed_time):
    """Save results to file."""
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write("===== SALES SUMMARY =====\n")
        file.write(f"Total Sales Amount: ${total_cost:.2f}\n")
        file.write(f"Execution Time (seconds): {elapsed_time:.6f}\n")


def main():
    """Main execution function."""
    if len(sys.argv) != 3:
        print("Usage:")
        print("python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    prices = build_price_dictionary(price_catalogue)
    total_cost = compute_total_sales(prices, sales_record)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n===== SALES SUMMARY =====")
    print(f"Total Sales Amount: ${total_cost:.2f}")
    print(f"Execution Time (seconds): {elapsed_time:.6f}")

    save_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()

