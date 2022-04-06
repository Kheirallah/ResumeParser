<h1>Resume Parser Example</h1>

The following project takes a resume as a pdf or docx and returns different fields parsed into output jsons

<h2>Prerequisites</h2>

Python 3.8

`https://www.python.org/downloads/release/python-380/`

Java

`https://java.com/en/download/`

<h2>Setup</h2>

<h3>Pre-Checks</h3>

Ensure you are using Python 3.8 by using the following command in CMD/Terminal

`python --version`

Output should show _Python 3.8.0_

Ensure you are using Java 18 by using the following command in CMD/Terminal

`java -version`

Output should show _java version "18" 2022-03-22_

<h3>Virtual Environment</h3>

Python venv allows us to keep all dependencies for this project self-contained within this project

**_Run all commands at the root of this repository_**

Create the virtual environment
`python -m venv ./venv`

Source the virtual environment to run commands in it going forward 
'.\venv\Scripts\activate'

**_if you get the following error then run the below command_**
`resume\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on    
this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.`

**_allows script execution on Windows for the current user_** `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`

You should now see (venv) in your command prompt if successful, For example
`(venv) PS C:\Users\kheir\Desktop\Repos\resume>`

**Congrats you have created a virtual environment for python!**

<h3>Project Requirements</h3>

Install the latest pip setup tools using the following `  python -m pip install -U pip setuptools`

You can install dependencies needed with the following command in our venv
`pip install -r .\requirements.txt`

Install exact version of spacy required for resume-parser 
`pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz`

Install NLTK, _note this will install on your computer not the venv_
`python -m nltk.downloader all`

<h3>Running the Script</h3>
Run the program with the following command `python main.py`

You should receive two json files as output. One for each result from each resume parser library

Congrats! You have parsed a resume! Feel free to try different resumes as well.

<h2>Reference</h2>

Resume-Parser

`https://pypi.org/project/resume-parser/`

Pyresparser

`https://pypi.org/project/pyresparser/`