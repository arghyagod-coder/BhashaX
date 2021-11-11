########################################################################
##                      BhashaX EzScript (JS)                         ##
## A Script to make the language conversion easier and faster for BSX ##
##       Author 	: Arghya Sarkar <arghyasarkar.nolan@gmail.com>    ##
##      Website   : https://www.bhashax.krishyadav.com                ##
##  Website	: https://www.krishyadav.github.io/BhashaX/index.html     ##
##      Website	: https://www.arghyagod-coder.github.io               ##
#3      Website	: https://www.krishyadav.com                          ##
########################################################################

#############################################################################
## NOTE: For this script to run properly, you need googletrans dev branch  ##
##                                                                         ##
##                 pip install googletrans==4.0.0rc1                       ##
#############################################################################

####################################
## Importing Google Translate API ##
####################################

from colorama.ansi import Style
from googletrans import Translator
import json
from colorama import Fore, Back, Style

#############################
## Initializing The Client ##
#############################

t = Translator()

###############################
## Check available languages ##
###############################

# import googletrans
# print(googletrans.LANGUAGES)

# Fill In This Area
# UserProfile
class UserLang():
    name: str = "Arghya Sarkar" # Use your real name only. Full Name
    email= "arghyasarkar.nolan@gmail.com" # Use a valid mail ID of yours.
    version="0.4-2" # Version Number. You can use integers, periods, alphabets (small only) here. - and _ are allowed but not any other symbol
    lang_short="ko" # A short name for your language (two letters). Check the available names for your language by running the piece of code at line 36 and 37.
    language="korean" # The full name of your language
    file_extension=".koen" # File extension for your language
    numbers: int="공일이삼사오육칠팔구" # The first 10 numbers (includes 0) of your language (For e.g., 123456789)

# Small Init
un=UserLang()

###########################
## Opening our Base JSON ##
###########################

with open('in.json') as json_file:
    data = json.load(json_file)
    en_keywords = data["KEYWORDS"]
    en_errors = data["ERRORS"]
    en_funcs = data["FUNCTIONS"]

##############################
## Translating each Section ##
##############################

for key, value in en_keywords.items():
    trs = t.translate(key, dest=un.lang_short)
    en_keywords[key] = trs.text

for key, value in en_errors.items():
    trs = t.translate(key, dest=un.lang_short)
    en_errors[key] = trs.text

for key, value in en_funcs.items():
    trs = t.translate(key, dest=un.lang_short)
    en_funcs[key] = trs.text

##########################
## The Final Dictionary ##
##########################

out_dict={
    "AUTHOR": f'{un.name} <{un.email}>',
    "VERSION": un.version,
    "LANG": {f"{un.lang_short.upper()}" : "EN"},
    "LANGUAGE": {f"{un.language.upper()}" : "ENGLISH"},
    "CT":".js",
    "EXTENSION":un.file_extension,
    "SPECIAL_SYMBOLS":"+-*/% = &|^>< .",
    "NUMBERS": {f"{un.numbers}" : "1234567890"},
    "KEYWORDS":en_keywords,
    "FUNCTIONS": en_funcs,
    "ERRORS": en_errors
}

###################################
## Creating the output JSON file ##
###################################

with open(f'{un.language}.json', 'w') as fp:
    fp.write(str(out_dict))

######################################
## Running the final replace script ##
######################################

import subprocess
subprocess.run("sh end.sh", shell=True)

###################
## Final Message ##
###################

print(Fore.YELLOW + f'The language file has been stored in {un.language}.json.\n\nDo not leave it like that. The script was made by a machine and there can be often a times that a machine goes wrong. READ AND EXAMINE THE WORDS BEFORE FINALIZING IT.\n\n~~ BhashaX Team ~~')