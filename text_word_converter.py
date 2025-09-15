# Text Word Counter (FileChooser)
# A simple script to count the number of words in a text file using a file chooser dialog.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Text Word Counter")
def main():
    parser = GooeyParser(description="A simple script to count the number of words in a text file using a file chooser dialog.")
    parser.add_argument('file', widget='FileChooser', help='Select the text file')
    args = parser.parse_args()
    
    if not os.path.isfile(args.file):
        print("The selected file does not exist.")
        return
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:   # ✅ specify encoding
            content = f.read()
    except UnicodeDecodeError:
        # fallback if the file isn’t UTF-8
        with open(args.file, 'r', encoding='latin-1') as f:
            content = f.read()
    
    word_count = len(content.split())
    print(f'The file contains {word_count} words.')

if __name__ == '__main__':
    main()
