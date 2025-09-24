# 10. Image File Renamer Input: FolderChooser for image folder + prefix text. Output: Rename images as prefix_1.jpg, prefix_2.jpg, …
from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Image File Renamer")
def main():
    parser = GooeyParser(description="Rename image files in a selected folder with a given prefix.")
    parser.add_argument("--folder", widget="DirChooser", help="Select the folder containing images")
    parser.add_argument("--prefix", help="Enter the prefix for renaming images")
    args = parser.parse_args()

    if args.folder and args.prefix:
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
        images = [f for f in os.listdir(args.folder) if f.lower().endswith(image_extensions)]
        
        for index, image in enumerate(images, start=1):
            ext = os.path.splitext(image)[1]
            new_name = f"{args.prefix}_{index}{ext}"
            os.rename(os.path.join(args.folder, image), os.path.join(args.folder, new_name))
        
        print(f"Renamed {len(images)} images with prefix '{args.prefix}'.")
    else:
        print("Please select a folder and enter a prefix.")

if __name__ == "__main__":
    main()
 

