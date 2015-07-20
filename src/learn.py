# Initial file

import sys
import json

def DataLearnedFilePath(lang):
    return "../data/" + lang + "data.json"

# NOTE(hugo): this script needs several arguments
# 0 - the python script (here learn.py)
# 1 - the language to process. english : en
# 1 - the book file to process


if __name__ == "__main__":
    if len(sys.argv) == 2:
        DataLearnFileName = DataLearnFilePath(sys.argv[1])
        Data = {}
        if os.path.isfile(DataLearnFileName):
            Data = json.loads(open(DataLearnFileName, "r+").read())
        Book = open(sys.argv[2], "r").read().split()
        LastWord = ""
        for Word in Book:
            if Word in Data:
                Data[Word]["occ"] += 1
            else:
                Data[Word]["occ"] = 1
            if LastWord != "":
                Data[LastWord]["suc"]

            LastWord = Word
            
        
                
        
    else:
        print "Misuse of the script"
