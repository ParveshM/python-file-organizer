import os
import json
import shutil
import argparse
import utils 
from google import genai
from pathlib import Path 
from dotenv import load_dotenv

load_dotenv() 

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", help="Source directory")
args = parser.parse_args()

if not args.src :
     print('Please provide a source directory')
     exit()


input_dir = fr'{args.src}'

if not (Path(input_dir).is_dir()):
     print(f"Source path: '{input_dir}', is not a valid directory")
     exit()


def sort_and_move_files(input_dir):
 try:
    files_list = os.listdir(input_dir)
    files = list(filter(lambda item:utils.is_file(input_dir,item),files_list))
    
    if(len(files) == 0):
        raise ValueError(f"No files found in the directory: '{input_dir}'")
    print('Classifying files with AI, please wait...')
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=utils.getPromt(files)
    )
    grouped_files = json.loads(response.text or '{}')
    print('Classification completed, moving files...')
    total_files = 0
    # Move files into respective folders
    for key in grouped_files:
        new_dir_path = os.path.join(input_dir, key)

        has_dir = Path(new_dir_path).is_dir()
        if not has_dir: # create new directory if it doesn't exist
            os.mkdir(new_dir_path)

        for file in grouped_files[key]:
            total_files += 1
            file_path = os.path.join(input_dir, file)
            move_file = os.path.join(new_dir_path, file)
            shutil.move(file_path, move_file)

    print('files moved:', total_files)
 except Exception as e:
        if isinstance(e,json.JSONDecodeError):
            print('Error: Failed to parse AI response. Please try again.')
            return
        print('Error:', str(e))

sort_and_move_files(input_dir)