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
import shutil

def main():
    path_to_fold = input("Path: ")
    if not os.path.exists(path_to_fold):
        print("This does not exist")
        main()
    else:
        for path_item in os.listdir(path_to_fold):
            filename, file_extension = os.path.splitext(path_item)
            
            # the path to the extension folder (regardless as to whether it exists)
            extfolder = os.path.join(path_to_fold, f"{file_extension} folder")
            
            print(f"{filename}, {file_extension}") # TEMP
            
            # path_item =\= file_path
            # This is for the file_path, which links to the item in question
            file_path = os.path.join(path_to_fold, path_item)
            if os.path.exists(extfolder):
                move_file(file_path, extfolder)
            else:
                make_folder(extfolder) # makes the external folder
                move_file(file_path, extfolder)

# moves the file from the file_path to the folder_path
def move_file(file_path, fold_path) -> None:
    shutil.move(file_path, fold_path)

# makes folder with name of fold_name, at fold_path
def make_folder(fold_name) -> None:
    os.mkdir(fold_name)


if __name__ == "__main__":
    main()
    print("it ran")