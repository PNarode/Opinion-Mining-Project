#!/Installed Setup/Python/python


import cgi, os
import cgitb; cgitb.enable()
import os




if __name__=="__main__":
    text=str(file('ranked.txt').read()).split('\n')
    print """ Content-type: text/html\n\n<html>
<head>
<title>Summary Table</title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<center>
<h1><font color='RED'>Feature Count</font></h1>
<table border='1'>
<tr><td><b>Feature</b></td><td><pos>Positive Opinion</pos></td><td><neg>Negative Opinion</neg></td></tr>"""
    for i in range(len(text)-1):
        temp=str(text[i]).split('=')
        print "<tr><td>%s</text></td><td><pos>%s</pos></td><td><neg>%s</neg></td></tr>" % (str(temp[0]),str(temp[3]),str(temp[4]),)
    print """</table></center></body></html>"""
