# 4. Email Generator Inputs: Name, Domain (gmail.com, yahoo.com, outlook.com). Output: Full email address.
from gooey import Gooey, GooeyParser

@Gooey(program_name="Email Generator")
def main():
    parser = GooeyParser(description="Generate a full email address.")
    parser.add_argument("--name", help="Enter your name", widget="TextField")
    parser.add_argument("--domain", choices=["gmail.com", "yahoo.com", "outlook.com"], help="Select your email domain", widget="Dropdown")
    args = parser.parse_args()

    if args.name and args.domain:
        email = f"{args.name}@{args.domain}"
        print(f"Generated Email Address: {email}")

if __name__ == "__main__":
    main()
