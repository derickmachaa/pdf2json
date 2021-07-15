#!/usr/bin/env python3

#script to do mambos
import re
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style
from timeit import default_timer as timer
import json

def quit():
    print('Bye')
    sys.exit(0)
pages=[]
def extract_text_by_page(js_path):
    global pages
    pages=[]
    with open(js_path,'r')as fh:
        print("\33[5m\33[100m[*]Scanning\33[0m\33[0m",end='\r')
        notes=json.load(fh)
        for chapter in notes.keys():
            for pageNo,ebook in enumerate(notes.get(chapter),1):
                text=ebook.get(f"{pageNo}")
                yield chapter,pageNo,text
            pages.append(pageNo)


def scan(js_path,search,verbose):
    for chapter,pageNo,text in (extract_text_by_page(js_path)):
        scanned=re.search(search,text,re.I)
        if(scanned):
            if(verbose):
                print(f"\033[94m[+]Found in {chapter} page:\033[0m\033[92m{pageNo}\033[0m")
                found=re.sub(scanned.group(),f"\033[91m{scanned.group()}\033[0m",text)
                print(found)
            else:
                print(f"\033[94m[+]Found in {chapter} page:\033[0m\033[92m{pageNo}\033[0m")
    return True

def main():
    hist=InMemoryHistory()
    style=Style.from_dict({'string':'yellow'},{'prmpt':'white'})
    inp=[('class:string','Find'),('class:prompt','->')]
    #run until ctrl+c
    while True:
        notes=sys.argv[1].split(',')
        #decision=prompt('\033[37mFind>\033[0m').split(':')
        decision=prompt(inp,style=style,history=hist).split(':')
        try:
            search=decision[0]
        except IndexError:
            search=''
        try:
            verbose=decision[1]
            if(verbose == 1 or verbose == 'y' or verbose == 'yes'):
                verbose=1
            else:
                verbose=0
        except IndexError:
            verbose=0
        start=timer()
        for note in notes:
            scan(note,search,verbose)
        print(f"\33[33mscanned {sum(pages)} pages in \033[0m\033[92m{round(timer()-start,4)} seconds\n\033[0m")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
