import os
import pathlib
import json
import shutil
import argparse
from google import genai
from dotenv import load_dotenv
import utils 
load_dotenv()

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

files = os.listdir(input_dir)[0:10]

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=utils.getPromt(files)
)
grouped_files = json.loads(response.text)
# grouped_files = {}
# total_files = 0
# for file in files:
#       suffix = pathlib.Path(file).suffix
      
#       if(suffix in utils.FILE_TYPES):
#             val = utils.FILE_TYPES[suffix]
#             if(val in grouped_files):
#                 grouped_files[val].append(file)
#                 total_files += 1
#             else : grouped_files[val] = []
# # Unique files 
# unique_arranged = {}
# for (key,value) in grouped_files.items():
#    if(len(value)>0): 
#         unique_arranged[key] = value
        
# List files to move by group
# prettySortedfiles = json.dumps(grouped_files,indent = 4)
total_files = 0
# Move files into respective folders
for key in grouped_files:
    new_dir_path = fr'{input_dir}\{key}'
    
    has_dir = pathlib.Path(new_dir_path).is_dir()
    if not has_dir: # create new directory if it doesn't exist
        os.mkdir(new_dir_path)

    for file in grouped_files[key]:
     total_files += 1
     file_path = fr'{input_dir}\{file}'
     move_file = fr'{new_dir_path}\{file}'
     shutil.move(file_path,move_file)

print('files moved:', total_files)
