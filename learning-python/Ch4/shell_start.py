 #
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile


def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        head, tail = path.split(src)
        print(head)
        print(tail)
        print(src)

        dst = src + ".bak"

        shutil.copy(src, dst)

        shutil.copystat(src, dst)

        os.rename("textfile.txt.bak", "newfile.txt")

        root_dir, tail = path.split(src)

        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt")
      
if __name__ == "__main__":
    main()
