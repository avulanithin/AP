# Q4. Create a Gooey-based command-line GUI that accepts two numerical inputs and performs basic arithmetic operations (addition, subtraction, multiplication, division).
from gooey import Gooey, GooeyParser

@Gooey(program_name="Simple Arithmetic Calculator")
def main():
    parser = GooeyParser(description="Perform basic arithmetic operations")
    parser.add_argument("num1", type=float, help="Enter the first number")
    parser.add_argument("num2", type=float, help="Enter the second number")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                        help="Choose the arithmetic operation")
    args = parser.parse_args()

    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        result = args.num1 - args.num2
    elif args.operation == "multiply":
        result = args.num1 * args.num2
    elif args.operation == "divide":
        result = args.num1 / args.num2

    print(f"Result: {result}")
if __name__ == "__main__":
    main()