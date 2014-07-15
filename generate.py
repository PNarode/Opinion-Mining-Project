#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os
import output
import ranking



if __name__=="__main__":
    ranking.rank("explicit.txt","implicit.txt")
    output.show(5)
