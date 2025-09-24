# 5. Compound Interest Calculator Inputs: Principal, Rate, Time, Compounds per Year. Output: Final Amount using formula A = P(1+R/n)^(nT).
from gooey import Gooey, GooeyParser

@Gooey(program_name="Compound Interest Calculator")
def main():
    parser = GooeyParser(description="Calculate compound interest.")
    parser.add_argument("--principal", type=float, help="Enter the principal amount", widget="DecimalField", gooey_options={"min": 0})
    parser.add_argument("--rate", type=float, help="Enter the annual interest rate (in %)", widget="DecimalField", gooey_options={"min": 0})
    parser.add_argument("--time", type=float, help="Enter the time (in years)", widget="DecimalField", gooey_options={"min": 0})
    parser.add_argument("--compounds_per_year", type=int, help="Enter the number of times interest is compounded per year", widget="IntegerField", gooey_options={"min": 1})

    args = parser.parse_args()

    if args.principal and args.rate and args.time and args.compounds_per_year:
        P = args.principal
        R = args.rate / 100
        T = args.time
        n = args.compounds_per_year

        A = P * (1 + R/n)**(n*T)
        print(f"Final Amount: {A:.2f}")

if __name__ == "__main__":
    main()
