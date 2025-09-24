# 3. using tkinter create a FileChooser to select a .txt file. Output the total number of words and characters in the file.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Word Counter")
def main():
    parser = GooeyParser(description="Count the total number of words and characters in a .txt file.")
    parser.add_argument('file', widget='FileChooser', help='Select the .txt file')
    args = parser.parse_args()
    
    if not os.path.isfile(args.file):
        print("The selected file does not exist.")
        return
    if not args.file.lower().endswith('.txt'):
        print("Please select a .txt file.")
        return
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print("The selected file is not in UTF-8 encoding.")
        return
    word_count = len(content.split())
    char_count = len(content)
    print(f'The file contains {word_count} words and {char_count} characters.')

if __name__ == '__main__':
    main()

