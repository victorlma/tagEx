from bs4 import BeautifulSoup as bs
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

    def setSubset(self, tag):
        self.subset = self.bs.find_all(tag)

    def getAttrib(self, attr):
        return self.subset[self.currentTag].get(attr)

def printcontext(context):
    for i in range(len(context.subset)):
        if i == context.currentTag:
            print(" >>\t"+str(context.subset[i]))
        else:
            print(str(i)+' - '+str(context.subset[i]))


def MainLoop(htmlsource):
    context = TagContext(htmlsource)
    context.setSubset(input("Tag to Check >  "))


    printcontext(context)


if __name__ == "__main__":

    if len(argv) < 1:
        print("Pass an html source (file or url)")
        exit(1)

    MainLoop(argv[1])
