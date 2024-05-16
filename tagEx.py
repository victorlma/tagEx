from bs4 import BeautifulSoup as bs
import os
from sys import argv
import requests as rq

class TagContext(object):

    def __init__(self, htmlsource):
        self.htmlsource = htmlsource 
        self.bs = self.bsInit()
        self.currentTag = 0
        self.subset = '' 

    def bsInit(self):

        try:
            conn = bs(self.htmlfromUrl(), 'html5lib')
        except:
            with open(self.htmlsource, 'r') as f:
                conn = bs(f.read(), 'html5lib')

        return conn

    def htmlfromUrl(self):
        return rq.get(self.htmlsource).text
        
    def setSubset(self, tag):
        self.subset = self.bs.find_all(tag)

    def getAttrib(self, attr):

        try:
            result = self.subset[self.currentTag].get(attr)
        except:
            result = "No Attrib Found"
        return result

    def setCurrentTag(self, tagNumber):
        self.printself()
        self.currentTag = tagNumber


    def printself(self):
        for i in range(len(self.subset)):
            if i == self.currentTag:
                print(" >>\t"+str(self.subset[i]))
            else:
                print(str(i)+' - '+str(self.subset[i]))

class UI(object):
    close = 0

    def __init__(self, context):
        self.context = context
        self.cmd = {0:self.context.printself,
                  1:self.setContextSubset,
                  2:self.setContextCurrentTag,
                  3:self.getContextAttrib
                  }

    def handleCmd(self):
        command = input("cmd: ")

        if command == "x" or command == "X":
            self.close = 1

        if not command.isnumeric():
            return
        
        command = int(command)

        os.system("clear")

        self.cmd[command]()

    def printOpts(self):
        print("[0] Print Selected Tags")
        print("[1] Select New Tag Group to Check")
        print("[2] Select Individual Tag")
        print("[3] Extract Tag Attribute")
        print("[X] Exit\n")

    def setContextSubset(self):
        tag = input("Tag Group to Check > ")
        self.context.setSubset(tag)

        if (not self.context.subset):
            print("\nNo Tag Group Found")

    def setContextCurrentTag(self):
        tagNumber = int(input("New Tag Number > "))
        self.context.setCurrentTag(tagNumber)

    def getContextAttrib(self):
        attr = str(input("Attr > "))
        print('\n'+ self.context.getAttrib(attr) + '\n')


def MainLoop(htmlsource):


    context = TagContext(htmlsource)


    ui = UI(context)
    ui.setContextSubset()

    context.printself()

    while not ui.close:

        ui.printOpts()
        ui.handleCmd()


if __name__ == "__main__":

    if len(argv) < 1:
        print("Pass an html source (file or url)")
        exit(1)


    if len(argv) == 2:
        MainLoop(argv[1])

    if len(argv) == 4:
        context = TagContext(argv[1])
        context.setSubset(argv[2])
        print(context.getAttrib(argv[3]))

