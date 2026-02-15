#!/usr/bin/env python3
"""
computeSales.py

Computa el total de ventas usando un catálogo de precios y un registro de ventas en JSON.
"""

import sys
import json
import time


def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' contiene JSON inválido.")
        return None


def build_price_dictionary(price_catalogue):
    prices = {}
    for item in price_catalogue:
        try:
            product = item["product"]
            price = float(item["price"])
            prices[product] = price
        except (KeyError, ValueError, TypeError):
            print(f"Entrada inválida de producto: {item}")
    return prices


def compute_total_sales(prices, sales_record):
    total_cost = 0.0
    for sale in sales_record:
        try:
            product = sale["product"]
            quantity = int(sale["quantity"])
            if product not in prices:
                print(f"Advertencia: Producto '{product}' no encontrado en catálogo.")
                continue
            total_cost += prices[product] * quantity
        except (KeyError, ValueError, TypeError):
            print(f"Entrada inválida de venta: {sale}")
    return total_cost


def save_results(total_cost, elapsed_time):
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write("===== SALES SUMMARY =====\n")
        file.write(f"Total Sales Amount: ${total_cost:.2f}\n")
        file.write(f"Execution Time (seconds): {elapsed_time:.6f}\n")


def main():
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py ProductList.json Sales.json")
        sys.exit(1)

    start_time = time.time()
    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    price_catalogue = load_json_file(price_file)
    sales_record = load_json_file(sales_file)

    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    prices = build_price_dictionary(price_catalogue)
    total_cost = compute_total_sales(prices, sales_record)
    elapsed_time = time.time() - start_time

    print("\n===== SALES SUMMARY =====")
    print(f"Total Sales Amount: ${total_cost:.2f}")
    print(f"Execution Time (seconds): {elapsed_time:.6f}")

    save_results(total_cost, elapsed_time)


if __name__ == "__main__":
    main()
