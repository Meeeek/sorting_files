# Conrad Fukuzawa
# Sorting Files
# August 2020
# Given a path it sorts the folder by file type
# This is generally supposed to be used on Downloads

# Instructions
# 1. Check what file type
# 2. if file is folder then ignore
# 3. put files into folders corresponding to file type
# 4. if folders for file already exists use preexisting folders

# File name notation
# .py should be "py folder"
import os

def main():
    path_to_fold = input("Path: ")
    if not os.path.exists(path_to_fold):
        print("This does not exist")
        main()
    else:
        for path_item in os.listdir(path_to_fold):
            filename, file_extension = os.path.splitext(path_item)
            
            # getting the extension folder if it exists
            extfolder = os.path.join(path_to_fold, f"{file_extension} folder")
            print(f"{filename}, {file_extension}") # TEMP
            
            if os.path.exists(extfolder):
                move_file(path_item, extfolder)
            else:
                make_folder(path_to_fold, extfolder)
                move_file(path_item, extfolder)

# moves the file from the file_path to the folder_path
def move_file(file_path, fold_path) -> None:
    pass

# makes folder with name of fold_name, at fold_path
def make_folder(fold_path, fold_name) -> None:
    pass


if __name__ == "__main__":
    main()
    print("it ran")