# Script for removing a tag from an html file

This script takes a tag from an html file and its class or id and rewrites
the file without that particular tag.
 
## Use

```
usage: removeTag.py [-h] [-r] [-d] -t TAG [-c TAG_CLASS] [-i TAG_ID]
                    FILES [FILES ...]

positional arguments:
  FILES                 HTML Files to be processed

optional arguments:
  -h, --help            show this help message and exit
  -r, --recursive       parse subfolders
  -d, --debug           Prints errors and warnings parsing the file
  -t TAG, --tag TAG     tag of the file to be removed
  -c TAG_CLASS, --tag-class TAG_CLASS
                        class of the tag to be removed
  -i TAG_ID, --tag-id TAG_ID
                        id of the tag to be removed
```
