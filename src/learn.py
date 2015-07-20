# Initial file

import sys
import json
import os.path

def DataLearnFilePath(lang):
    return "../data/" + lang + "/data.json"

# NOTE(hugo): this script needs several arguments
# 0 - the python script (here learn.py)
# 1 - the language to process. english : en
# 1 - the book file to process


if __name__ == "__main__":
    if len(sys.argv) == 3:
        DataLearnFileName = DataLearnFilePath(sys.argv[1])
        print DataLearnFileName
        Data = {}
        DataFile = open(DataLearnFileName, "r+");
        Data = json.loads(DataFile.read())
        Book = open(sys.argv[2], "r").read().split()
        LastWord = ""
        for Word in Book:
            if Word in Data:
                Data[Word]["occ"] += 1
            else:
                Data[Word] = {}
                Data[Word]["suc"] = {}
                Data[Word]["occ"] = 1
            if LastWord != "":
                if Word in Data[LastWord]["suc"]:
                    Data[LastWord]["suc"][Word] += 1
                else:
                    Data[LastWord]["suc"][Word] = 1

            LastWord = Word

        # NOTE(hugo): All data gathered. Time to write in file
        DataFile.seek(0)
        DataFile.write(json.dumps(Data, indent=4, separators=(' , ', ' : ')))

            
        
        print "Sucessfully wrote data in file"
        
    else:
        print "Misuse of the script"
