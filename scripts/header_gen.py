#!/usr/bin/python

## Little scipt to add a default header for pandoc to pdf from markdown.
## Default setting have
##  * Title name {parent} {date}
##  * Author = Stephen Slatky
##  * Sections numbered
## TODO add better parsing
## TODO add error chekcing.
## TODO Check if header is there

import os,os.path
import sys


def main():
    files = get_files()
    for name in files:
        if not (already_has_header(name)):
            header = create_header(name)
            line_prepender(name , header)

## Settings added in header
##  * Title name {parent} {date}
##  * Author = Stephen Slatky
##  * Sections numbered
def create_header(filename):
    name = filename.split(".")[0]
    parentdir = (os.path.abspath(os.path.join("./" + filename, os.pardir)).split("/"))
    year = parentdir[len(parentdir) -2]
    subject = parentdir[len(parentdir)-1]
    header = "---\ntitle: " + subject + " " + name + "-" + year + "\nauthor: Stephen Slatky\ngeometry: margin=1in\nnumbersections: true\n---\n"
    return header


## Checks first line to see if the first line is the one used in creation of header
## Cna fail if 3 dashs are used to make a line as first line. Very uncommon in my notes.
def already_has_header(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        if line == "---\n":
            return True
        else:
           return False


def get_files():
    return sys.argv[1:]


# Writes to the top of a file.
# Stores it all in memorey so it can not be a big file.
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


if __name__ == "__main__":
    main()
