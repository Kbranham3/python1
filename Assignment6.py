def currency_converter():
    exchange_rates = {
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09,
        ("USD", "GBP"): 0.78,
        ("GBP", "USD"): 1.28,
        ("EUR", "GBP"): 0.85,
        ("GBP", "EUR"): 1.18
    }

    print("Available currency pairs:")
    for (from_currency, to_currency), rate in exchange_rates.items():
        print(f"{from_currency} to {to_currency}: {rate}")

    from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()

    if (from_currency, to_currency) not in exchange_rates:
        print("Invalid currency pair. Please check the available pairs and try again.")
        return

    try:
        amount = float(input("Enter the amount to convert: "))
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return

    converted_amount = amount * exchange_rates[(from_currency, to_currency)]
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


if __name__ == "__main__":
    currency_converter()
