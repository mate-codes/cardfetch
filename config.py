import os
from colorama import *

ascii_color = Fore.RESET
text_info = Fore.RESET
text_color = Fore.RESET  
title_color = Fore.RESET
dash_color = Fore.RESET
print(Back.RESET)  
print(Style.NORMAL)  

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

path = r"ascii.txt"
ascii_art = open(path, 'r').read()


colored_ascii_art = f"{ascii_color}{ascii_art}{Fore.RESET}"

text = f"""{title_color}           Your Name{ascii_color}
{dash_color}--------------------------------{ascii_color}
{text_color}Age: {text_info}your age{ascii_color}
{text_color}Gender: {text_info}your gender{ascii_color}
{text_color}Pronouns: {text_info}your pronouns{ascii_color}
{text_color}Email: {text_info}your email{ascii_color}
{text_color}Phone 1: {text_info}your phone number 1{ascii_color}
{text_color}Phone 2: {text_info}your phone number 2{ascii_color}
{text_color}Website: {text_info}your website{ascii_color}
{text_color}YouTube: {text_info}your youtube channel{ascii_color}
{text_color}Discord: {text_info}your discord username{ascii_color}
{text_color}Matrix: {text_info}your matrix{ascii_color}
{text_color}Lemmy: {text_info}your lemmy account{ascii_color}
{text_color}Git: {text_info}your github or gitlab{ascii_color}
{text_color}Twitch: {text_info}your twitch{ascii_color}
{text_color}TikTok: {text_info}your tiktok acc{ascii_color}
{text_color}Twitter / X: {text_info}your Twitter / X acc{ascii_color}
{text_color}Reddit: {text_info}your u/username{ascii_color}

(Config me on config.py)
(Config ASCII Art on ascii.txt)
"""

ascii_lines = colored_ascii_art.split('\n')
text_lines = text.split('\n')

max_lines = max(len(ascii_lines), len(text_lines))

for i in range(max_lines):
    ascii_line = ascii_lines[i] if i < len(ascii_lines) else ''
    text_line = text_lines[i] if i < len(text_lines) else ''
    print(f"{ascii_line}   {text_line}")
