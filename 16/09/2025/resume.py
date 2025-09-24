# 7. Basic Resume Form Inputs: Name, Age, Skills (MultiLine), FileChooser for photo. Output: Print a formatted resume in console.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Resume Form")
def main():
    parser = GooeyParser(description="Fill out the resume form.")
    parser.add_argument("--name", help="Enter your name", widget="TextField")
    parser.add_argument("--age", type=int, help="Enter your age", widget="IntegerField", gooey_options={"min": 0, "max": 100})
    parser.add_argument("--skills", help="Enter your skills (one per line)", widget="Textarea")
    parser.add_argument("--photo", help="Choose your photo", widget="FileChooser")
    args = parser.parse_args()

    if args.name and args.age is not None and args.skills and args.photo:
        if not os.path.isfile(args.photo):
            print(f"Photo file not found: {args.photo}")
            return

        skills_list = [s.strip() for s in args.skills.strip().splitlines() if s.strip()]
        photo_path = os.path.abspath(args.photo)
        resume = [
            "------------------------------",
            "            RESUME",
            "------------------------------",
            f"Name: {args.name}",
            f"Age: {args.age}",
            "Skills:"
        ]
        resume.extend([f"  - {skill}" for skill in skills_list])
        resume.append(f"Photo Path: {photo_path}")
        resume.append("------------------------------")
        print("\n".join(resume))
    else:
        print("All fields are required.")

if __name__ == "__main__":
    main()


