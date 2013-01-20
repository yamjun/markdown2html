#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import markdown
import sys
import os

def main():
    argvs = sys.argv

    
    md = markdown.Markdown()
    md.convertFile(input=str(argvs[1]) , output=str(argvs[1]) + '.tmp' , encoding="utf8")
    
    f = open(str(argvs[1]) + '.tmp', 'r')
    text = f.read()
    f.close()
    os.remove(str(argvs[1]) + '.tmp')

    fw = open(str(argvs[1]) + '.html', 'w+')
    fw.write(open('head.html', 'r').read())
    fw.write(text)
    fw.write(open('end.html', 'r').read())
    fw.close()



if __name__ == '__main__':
    main()
