
"""
Implements three functions:
    1. price_at(x) that finds the price on a given day x.
    2. max_price(a, b) that finds the maximum price from day a to day b.
    3. min_price(a, b) that finds the minimum price from day a to day b.

The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).
"""
stock_prices = [
    34.68, 36.09, 34.94, 33.97, 34.68,
    35.82, 43.41, 44.29, 44.65, 53.56,
    49.85, 48.71, 48.71, 49.94, 48.53,
    47.03, 46.59, 48.62, 44.21, 47.21
]

def price_at(day):
    if not 1 <= day <= 20:
        return "Invalid day"
    return stock_prices[day - 1]


def max_price(a, b):
    if not (1 <= a <= 20 and 1 <= b <= 20) or a > b:
        return "Invalid range"

    prices = stock_prices[a - 1 : b]
    max_val = prices[0]

    for price in prices:
        if price > max_val:
            max_val = price

    return max_val


def min_price(a, b):
    if not (1 <= a <= 20 and 1 <= b <= 20) or a > b:
        return "Invalid range"

    prices = stock_prices[a - 1 : b]
    min_val = prices[0]

    for price in prices:
        if price < min_val:
            min_val = price

    return min_val


# -------- TESTING --------
print("Price at day 5:", price_at(5))
print("Max price (1–4):", max_price(1, 4))
print("Min price (1–4):", min_price(1, 4))
