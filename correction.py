#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os
import ginger
import output


if __name__=='__main__':
    form = cgi.FieldStorage()
    fileitem = form['uploadReview']
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        name,ext=os.path.splitext(fileitem.filename)
        open('files/' + str(name)+str(ext), 'wb').write(fileitem.file.read())
        filename=str(name)+str(ext)
        ginger.main('files/'+filename)
    output.show(1)
    
    
