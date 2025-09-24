# 8. Number Guessing Game Input: Guess a number between 1–10. Output: ‘Correct’ or ‘Try Again’ (program generates random number). 
from gooey import Gooey, GooeyParser
import random

@Gooey
def main():
    parser = GooeyParser(description="Number Guessing Game")
    parser.add_argument("--guess", type=int, help="Guess a number between 1 and 10", widget="IntegerField", gooey_options={"min": 1, "max": 10})
    args = parser.parse_args()

    if args.guess is not None:
        random_number = random.randint(1, 10)
        if args.guess == random_number:
            print("Correct!")
        else:
            print("Try Again!")
    else:
        print("Please enter a valid guess.")

if __name__ == "__main__":
    main()
