#!/usr/bin/env python3
import json
import subprocess
import os
import sys


def help():
    print(f"Usage:\n{os.path.basename(sys.argv[0])} input.pdf out.json\nYou can also specify multiple comma seperated files as input: input.pdf,input1.pdf")

def pdfinfo(filename):
    cmd=f'pdfinfo {filename}'
    if not os.path.exists(filename):
        print(f"file {filename} does not exists")
    else:
        output=subprocess.getoutput(cmd)
        for line in map(str, output.splitlines()):
            if('Pages' in line):
                return(line.split(':')[1].strip())


def main():
    if ( not len(sys.argv) == 3 or sys.argv[1]=="-h" or sys.argv[1]=='--help'):
        help()
    else:
        total={}
        filenames=sys.argv[1].split(',')
        for name in filenames:
            notes=[]
            pagejs={}
            pageNo=0
            pageNo=int(pdfinfo(f'{name}'))
            print(f"Converting: {name}")
            for page in range(1,pageNo+1):
                print(f"Converting {page}/{pageNo}",end="\r")
                pageText=(subprocess.getoutput(f"pdf2txt.py -p {page} {name}")).strip()
                pagejs={page:pageText}
                notes.append(pagejs)
            total.update({name:notes})
        with open(f"{sys.argv[2]}","w")as file:
            json.dump(total,file,indent=4)
pdfinfo('python-basics-sample-chapters.pdf')
if __name__ == "__main__":
    main()
