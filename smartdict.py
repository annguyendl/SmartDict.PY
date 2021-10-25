import difflib
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./data/data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        app_dic = difflib.get_close_matches(word.lower(), data.keys(), n=3, cutoff=0.8)
        app_len = len(app_dic)
        result = ''
        if app_len > 0:
            i = 0
            while i < app_len:
                key = input("Did you mean '%s'? (y/n/q): " % (difflib.get_close_matches(word.lower(), data.keys(), n=5, cutoff=0.8)[i]) )
                if key.lower() == "y":
                    result = data[difflib.get_close_matches(word.lower(), data.keys(), n=3, cutoff=0.8)[i]]
                    break
                elif key.lower() == "n":
                    i = i + 1
                else:
                    result = "We don't know your decision"
        
        if result == '':
            result = "This word doesn't exit in program dictionary"
        return result

word = input("Enter English word: ")
define = translate(word)

if (type(define) == list):
    for item in define:
        print("- " + item)
else:
    print("- " + define)
