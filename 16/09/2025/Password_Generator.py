# 9. Password Generator Inputs: Length (slider 6–20), Checkboxes (include digits, include symbols).Output: Random password.
from gooey import Gooey, GooeyParser
import random
import string

@Gooey(program_name="Password Generator")
def main():
    parser = GooeyParser(description="Generate a random password.")
    parser.add_argument("--length", type=int, help="Enter the desired password length (6-20)", widget="IntegerField", gooey_options={"min": 6, "max": 20})
    parser.add_argument("--include_digits", action="store_true", help="Include digits in the password")
    parser.add_argument("--include_symbols", action="store_true", help="Include symbols in the password")
    args = parser.parse_args()

    characters = string.ascii_letters
    if args.include_digits:
        characters += string.digits
    if args.include_symbols:
        characters += string.punctuation
    if args.length and characters:
        password = ''.join(random.choice(characters) for _ in range(args.length))
        print(f"Generated Password: {password}")
    else:
        print("Please specify a valid length and at least one character type.")

if __name__ == "__main__":
    main()

