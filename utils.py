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

Here are the filenames:
{files}
'''


FILE_TYPES = {
    '.pdf': 'pdf',
    '.docx': 'word',
    '.xlsx': 'excel',
    '.jpg': 'image',
    '.png': 'image',
    '.txt': 'text',
    '.mp4': 'video',
}