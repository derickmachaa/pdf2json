#!/usr/bin/env python3
import json
import subprocess
import os
import sys


def help():
    print(f"Usage:\n{os.path.basename(sys.argv[0])} output.json input.pdf\nYou can also specify multiple comma seperated files as input: input.pdf,input1.pdf,input3.pdf as long as file names dont contain ,")

def pdfinfo(filename):
    print(filename)
    cmd=f'pdfinfo "{filename}"'
    if not os.path.exists(filename):
        print(f"file {filename} does not exists")
    else:
        output=subprocess.getoutput(cmd)
        for line in map(str, output.splitlines()):
            if('Pages' in line):
                return(line.split(':')[1].strip())


def main():
    print(len(sys.argv))
    if ( not len(sys.argv) == 3 or sys.argv[1]=="-h" or sys.argv[1]=='--help'):
        help()
    else:
        total={}
        outfile=sys.argv[1]
        sources=sys.argv[2]
        filenames=sources.split(',')
        for name in filenames:
            notes=[]
            pagejs={}
            pageNo=0
            pageNo=int(pdfinfo(name))
            print(f"Converting: {name}")
            for page in range(1,pageNo+1):
                print(f"Converting {page}/{pageNo}",end="\r")
                pageText=(subprocess.getoutput(f"pdf2txt.py -p {page} '{name}'")).strip()
                pagejs={page:pageText}
                notes.append(pagejs)
            total.update({name:notes})
        with open(f"{outfile}","w")as file:
            json.dump(total,file,indent=4)
        print()
        print("Done!!!")
if __name__ == "__main__":
    main()
