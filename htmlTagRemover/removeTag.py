from bs4 import BeautifulSoup as bs
import argparse
import sys
import os

def parse_file(fileName, html_tag, tag_class, tag_id, debugMode = False):
    htmlFile = ""
    doc = ""
    try:
        htmlFile = open(fileName,"rb")
    except IOError as e:
        print("Error parsing file: " + fileName )
        print(str(e))
        return

    try:
        fileSoup = bs(htmlFile, "lxml")
        if (fileSoup is None):
            print("ERROR WHILE PARSING THE FILE")
        
        # Creating the filter
        html_filter = dict()

        # Add class if exist
        if (tag_class != ""):
            html_filter['class'] = tag_class
        
        # Add id if exist
        if (tag_id != ""):
            html_filter['id'] = tag_id
        if(debugMode):
            print("File = " + fileName +" :")
            print(fileSoup.findAll(html_tag,html_filter))

        for s in fileSoup.findAll(html_tag,html_filter):
            s.decompose()

        if(debugMode):
            print(fileSoup.findAll(html_tag,html_filter))
        htmlFile = open(fileName,"w")
        htmlFile.write(str(fileSoup.prettify()))
    except BaseException as e:
        print("Error processing file :" + fileName)
        print(" -- " + str(sys.exc_info()[0]))
        print(" -- " + e.__doc__)
        print(" -- " + format(e))
    htmlFile.close()
    return

def main():
#{
    ## Program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="FILES", type=str, default=[], nargs="+",help="HTML Files to be processed")
    parser.add_argument("-r", "--recursive",action='store_true', help="parse subfolders")
    parser.add_argument("-d", "--debug", action='store_true', help="Prints errors and warnings parsing the file")
    parser.add_argument("-t", "--tag", default="", required=True, type=str, help="tag of the file to be removed")
    parser.add_argument("-c", "--tag-class", default="", type=str, help="class of the tag to be removed")
    parser.add_argument("-i", "--tag-id", default="", type=str, help="id of the tag to be removed")
    ## Parsing the arguments
    args = parser.parse_args()
    debugMode = True if args.debug else False
    recursive = True if args.recursive else False
    files = args.files
    tag = args.tag
    tag_class = args.tag_class
    tag_id = args.tag_id
    if (recursive):
        print("RECURSIVE MODE ENABLED")
    if (debugMode):
        print("DEBUG MODE ENABLED")
    if (not recursive):
        for aFile in files:
            if (debugMode):
                print("Processing file: " + aFile + " with tag " + tag + " with class " + tag_class + " with id " + tag_id)
            parse_file(aFile,tag,tag_class,tag_id,debugMode)
    else:
        for aFile in files:
            for path, dirs, filesInDir in os.walk(aFile):
                for filename in filesInDir:
                    if filename.lower().endswith(('.html','shtml','dhtml')):
                        fullpath = os.path.join(path, filename)
                        if (debugMode):
                            print("Processing file: " + aFile + " with tag " + tag + " with class " + tag_class + " with id " + tag_id)
                        parse_file(fullpath,tag,tag_class,tag_id,debugMode)
#}

## Main sentinel
if __name__ == "__main__":
    main()
