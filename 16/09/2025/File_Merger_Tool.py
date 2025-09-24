# 6. File Merger Tool Inputs: Select two .txt files using FileChooser. Output: A new file with contents of both merged.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="File Merger")
def main():
    parser = GooeyParser(description="Merge two text files.")
    parser.add_argument("--file1", widget="FileChooser", help="Select the first .txt file", gooey_options={"filetypes": [("Text files", "*.txt")]})
    parser.add_argument("--file2", widget="FileChooser", help="Select the second .txt file", gooey_options={"filetypes": [("Text files", "*.txt")]})
    args = parser.parse_args()

    if args.file1 and args.file2:
        with open(args.file1, 'r') as f1, open(args.file2, 'r') as f2, open("merged.txt", 'w') as fout:
            fout.write(f1.read())
            fout.write("\n")
            fout.write(f2.read())
        print("Files merged successfully into 'merged.txt'.")

if __name__ == "__main__":
    main()
