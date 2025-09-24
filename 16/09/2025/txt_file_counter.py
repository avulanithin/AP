# 3. Use a FileChooser to select a .txt file. Output the total number of words and characters in the file.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Text File Counter")
def main():
    parser = GooeyParser(description="Count words and characters in a text file.")
    parser.add_argument("--file", widget="FileChooser", help="Select a .txt file", gooey_options={"filetypes": [("Text files", "*.txt")]})
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
            word_count = len(content.split())
            char_count = len(content)
            print(f"Words: {word_count}, Characters: {char_count}")

if __name__ == "__main__":
    main()
