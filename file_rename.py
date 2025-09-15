# File Renamer (FileChooser)
# A simple script to rename files using a file chooser dialog.
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="File Renamer")
def main():
    parser = GooeyParser(description="A simple script to rename files using a file chooser dialog.")
    parser.add_argument('file', widget='FileChooser', help='Select the file to rename')
    parser.add_argument('new_name', help='Enter the new name for the file')
    args = parser.parse_args()
    directory = os.path.dirname(args.file)
    new_path = os.path.join(directory, args.new_name)
    os.rename(args.file, new_path)
    print(f'File renamed to: {new_path}')

if __name__ == '__main__':
    main()

