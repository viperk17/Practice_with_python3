# Prints jpg files present in the directory
import glob
import os

# help(glob)
os.chdir("/home/flyboypk/Downloads")
for file in glob.glob("*.jpg"):
    print(file)
