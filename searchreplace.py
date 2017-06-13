import fileinput
import os

directory = "./On-board/doors-opening"
textToFind = "doors-opening"
textToReplace = "doors-closing"

for subdir, dirs, files in os.walk(directory):
    for singlefile in files:
        filepath = subdir + os.sep + singlefile
        if filepath.endswith(".html"):
            with fileinput.FileInput(filepath, inplace=True, backup=False) as file:
                for line in file:
                    print(line.replace(textToFind, textToReplace), end="")
