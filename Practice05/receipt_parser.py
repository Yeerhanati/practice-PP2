import re

# Read receipt text
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices
prices = re.findall(r'(\d{1,3}(?: \d{3})*,00)', text)
clean_prices = [int(p.replace(' ', '').replace(',00', '')) for p in prices]

# 2. Extract product names
products = re.findall(r'\d+\.\n(.+)', text)

# 3. Calculate total
total = sum(clean_prices)

# 4. Extract date and time
datetime_match = re.search(r'Время: (\d{2}\.\d{2}\.\d{4}) (\d{2}:\d{2}:\d{2})', text)
date = datetime_match.group(1) if datetime_match else "N/A"
time = datetime_match.group(2) if datetime_match else "N/A"

# 5. Payment method
payment = "Bank Card" if "Банковская карта" in text else "Cash"

# 6. Structured output
print("=== Receipt Parsing Result ===")
print(f"Date: {date}")
print(f"Time: {time}")
print(f"Payment Method: {payment}")
print(f"Total Amount: {total}")
print("\nProducts:")
for i, (name, price) in enumerate(zip(products, clean_prices), 1):
    print(f"{i}. {name.strip()} | {price}")