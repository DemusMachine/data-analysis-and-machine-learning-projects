#https://gist.github.com/nanda-dash/8e7d723eb5a22dcc97bf32203adb9fa3

import webbrowser
from urllib.parse import quote
import os
import time
import pyautogui
import pandas as pd

df = pd.read_csv('job list')
number = 341 #change according to your position

company_name = df.iloc[number-1].iloc[0]
job_title = df.iloc[number-1].iloc[1]
recipient = df.iloc[number-1].iloc[2]

cv_path = r"C:\Users\Misha\Downloads\STEM\CV.pdf"
transcript_path = r"C:\Users\Misha\Downloads\STEM\hwsrcrtr_cityu.sw_gen_crtr.pdf"

def copy_files(file_paths):
    files_str = ",".join([f"'{p}'" for p in file_paths])
    if files_str:
        os.system(f"powershell Set-Clipboard -LiteralPath {files_str}")

subject = "STEM Internship Scheme"
body = f"""Dear {company_name} HR Team, \n\nI would like to apply for the "{job_title}" position at your company under the STEM Internship program. I have attached a transcript for the first year and my CV to this email.\n
Sincerely,
Mikhail"""

encoded_subject = quote(subject)
encoded_body = quote(body)
 
mailto_url = f"mailto:{recipient}?subject={encoded_subject}&body={encoded_body}"

webbrowser.open(mailto_url)

time.sleep(3)
copy_files([cv_path,transcript_path])
time.sleep(0.1)
pyautogui.hotkey('ctrl','v')