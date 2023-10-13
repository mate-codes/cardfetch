import os
from colorama import *


print(Fore.BLUE) # Text Color (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET)
print(Back.RESET) # Background Color (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET)
print(Style.NORMAL) # Text Style (DIM, NORMAL, BRIGHT, RESET_ALL)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

path = r"ascii.txt"
ascii_art = open(path, 'r').read()



text = """           Your Name
--------------------------------
Age: your age
Gender: your gender
Pronouns: your pronouns
Email: your email
Phone 1: your phone number 1
Phone 2: your phone number 2
Website: your website
YouTube: your youtube channel
Discord: your discord username
Matrix: your matrix
Lemmy: your lemmy account
Git: your github or gitlab
Twitch: your twitch
TikTok: your tiktok acc
Twitter / X: your Twitter / X acc
Reddit: your u/username



(Config me on config.py)
(Config ASCII Art on ascii.txt)
"""


ascii_lines = ascii_art.split('\n')
text_lines = text.split('\n')


max_lines = max(len(ascii_lines), len(text_lines))


for i in range(max_lines):
    ascii_line = ascii_lines[i] if i < len(ascii_lines) else ''
    text_line = text_lines[i] if i < len(text_lines) else ''
    print(f"{ascii_line}   {text_line}")

