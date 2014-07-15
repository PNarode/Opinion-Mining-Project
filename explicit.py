#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os
import output
import extraction


if __name__=='__main__':
    extraction.mine("comments.txt")
    output.show(3)
