# 2. Currency Converter Inputs: Amount, From Currency (INR/USD/EUR), To Currency (INR/USD/EUR). Output the converted value (use fixed rates).
from gooey import Gooey, GooeyParser

@Gooey(program_name="Currency Converter")
def main():
    parser = GooeyParser(description="Convert currency between INR, USD, and EUR.")

    parser.add_argument("--amount", type=float, help="Enter the amount to convert",
                        widget="DecimalField", gooey_options={"min": 0},)
    parser.add_argument("--from_currency", choices=["INR", "USD", "EUR"], help="Select the currency to convert from",
                        widget="Dropdown",)
    parser.add_argument("--to_currency", choices=["INR", "USD", "EUR"], help="Select the currency to convert to",
                        widget="Dropdown",)

    args = parser.parse_args()

    # Fixed conversion rates
    rates = {
        ("INR", "USD"): 0.012,
        ("USD", "INR"): 83.33,
        ("INR", "EUR"): 0.010,
        ("EUR", "INR"): 100.00,
        ("USD", "EUR"): 0.85,
        ("EUR", "USD"): 1.18
    }

    if args.from_currency == args.to_currency:
        converted_amount = args.amount
    else:
        converted_amount = args.amount * rates[(args.from_currency, args.to_currency)]

    print(f"Converted Amount: {converted_amount:.2f} {args.to_currency}")

if __name__ == "__main__":
    main()
