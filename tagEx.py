from bs4 import BeautifulSoup as bs
import os
from sys import argv

class TagContext(object):

    def __init__(self, htmlsource):
        self.htmlsource = htmlsource 
        self.bs = self.bsInit()
        self.currentTag = 0
        self.subset = '' 
        pass

    def bsInit(self):
        with open(self.htmlsource, 'r') as f:
            conn = bs(f.read(), 'html5lib')

        return conn

    def htmlfromUrl(self):
        pass

    def setSubset(self):
        tag = input("Tag Group to Check > ")
        self.subset = self.bs.find_all(tag)

    def getAttrib(self):
        attr = input("Attr > ")
        return print('\n'+self.subset[self.currentTag].get(attr)+'\n')

    def setCurrentTag(self):
        self.printself()
        self.currentTag = int(input("New Tag Number > "))


    def printself(self):
        for i in range(len(self.subset)):
            if i == self.currentTag:
                print(" >>\t"+str(self.subset[i]))
            else:
                print(str(i)+' - '+str(self.subset[i]))



def MainLoop(htmlsource):


    context = TagContext(htmlsource)
    context.setSubset()
    cmdContext = {0:context.printself,
                  1:context.setSubset,
                  2:context.setCurrentTag,
                  3:context.getAttrib
                  }

    context.printself()

    while True:
        print("[0] Print Selected Tags")
        print("[1] Select New Tag Group to Check")
        print("[2] Select Individual Tag")
        print("[3] Extract Tag Attribute")
        print("[X] Exit\n")

        command = input("cmd: ")

        os.system("clear")

        if command == "x" or command == "X":
            break

        if not command.isnumeric():
            continue

        command = int(command)


        cmdContext[command]()


if __name__ == "__main__":

    if len(argv) < 1:
        print("Pass an html source (file or url)")
        exit(1)

    MainLoop(argv[1])
