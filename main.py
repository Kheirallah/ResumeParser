import json
from resume_parser import resumeparse
from pyresparser import ResumeParser

# Resume parser https://pypi.org/project/resume-parser/
data = resumeparse.read_file('Kheirallah_Ashkar_Resume.pdf') #Add path to any resume here
jsonData = json.dumps(data, indent=4)

# Writing to resume-parser-output.json
with open("resume-parser-output.json", "w") as outfile:
    outfile.write(jsonData)

#Py Resume Parser https://pypi.org/project/pyresparser/
data = ResumeParser('Kheirallah_Ashkar_Resume.pdf').get_extracted_data() #Add path to any resume here
jsonData = json.dumps(data, indent=4)

# Writing to pyresparser-output.json
with open("pyresparser-output.json", "w") as outfile:
    outfile.write(jsonData)

