from gooey import Gooey, GooeyParser

@Gooey(program_name="Marks Calculator")
def main():
    parser = GooeyParser(description="Calculate the total and percentage of marks in 5 subjects.")

    # Use optional arguments with
    parser.add_argument("--subject1", type=int, help="Enter marks for Subject 1 (0-100)",
                        widget="IntegerField", gooey_options={"min": 0, "max": 100},)
    parser.add_argument("--subject2", type=int, help="Enter marks for Subject 2 (0-100)",
                        widget="IntegerField", gooey_options={"min": 0, "max": 100},)
    parser.add_argument("--subject3", type=int, help="Enter marks for Subject 3 (0-100)",
                        widget="IntegerField", gooey_options={"min": 0, "max": 100},)
    parser.add_argument("--subject4", type=int, help="Enter marks for Subject 4 (0-100)",
                        widget="IntegerField", gooey_options={"min": 0, "max": 100},)
    parser.add_argument("--subject5", type=int, help="Enter marks for Subject 5 (0-100)",
                        widget="IntegerField", gooey_options={"min": 0, "max": 100},)

    args = parser.parse_args()

    marks = [args.subject1, args.subject2, args.subject3, args.subject4, args.subject5]
    total = sum(marks)
    percentage = total / 5

    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    main()
