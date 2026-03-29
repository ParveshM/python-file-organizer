import os
def getPromt(files):
     return f'''
You are a file organizer assistant.

I will give you a list of filenames.
Your job is to categorize each file into a folder name based on its filename and extension.

Rules:
- Return only a valid JSON object, nothing else
- No explanations, no extra text, no markdown, no code blocks
- Use this exact structure: {{category :[filenames] }}
- Keep category names simple, single word, capitalized (e.g. Finance, Images, Documents)
- If you are unsure, put it in "Others"

Example output:
{{finance :[budget.xlsx, gst.xlsx], images :[photo.jpg, logo.png]}}
Here are the filenames:
{files}
'''

def is_file(base_dir,file):
    return os.path.isfile(os.path.join(base_dir,file))