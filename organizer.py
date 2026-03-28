import os
import pathlib
import json
import shutil
import argparse

FILE_TYPES = {
    '.pdf': 'pdf',
    '.docx': 'word',
    '.xlsx': 'excel',
    '.jpg': 'image',
    '.png': 'image',
    '.txt': 'text',
    '.mp4': 'video',
}


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", help="Show output message")
args = parser.parse_args()

if not args.src :
     print('Please provide a source directory')
     exit()


# input_dir = r'C:\Users\lenovo\Downloads\test'
input_dir = fr'{args.src}'

if not (pathlib.Path(input_dir).is_dir()):
     print(f"Source path: '{input_dir}' , is not a valid directory")
     exit()

files = os.listdir(input_dir)
grouped_files = {}
total_files = 0
for file in files:
      suffix = pathlib.Path(file).suffix
      
      if(suffix in FILE_TYPES):
            val = FILE_TYPES[suffix]
            if(val in grouped_files):
                grouped_files[val].append(file)
                total_files += 1
            else : grouped_files[val] = []
# Unique files 
unique_arranged = {}
for (key,value) in grouped_files.items():
   if(len(value)>0): 
        unique_arranged[key] = value
        
# List files to move by group
prettySortedfiles = json.dumps(unique_arranged,indent = 4)
print('files found:', total_files, f'\nfiles:{prettySortedfiles}')

# Move files into respective folders
# for key in unique_arranged:
#     new_dir_path = fr'{input_dir}\{key}'
    
#     has_dir = pathlib.Path(new_dir_path).is_dir()
#     if not has_dir: # create new directory if it doesn't exist
#         os.mkdir(new_dir_path)

#     for file in unique_arranged[key]:
#      file_path = fr'{input_dir}\{file}'
#      move_file = fr'{new_dir_path}\{file}'
#      shutil.move(file_path,move_file)

