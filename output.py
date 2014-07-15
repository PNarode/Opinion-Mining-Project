#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os
import index


def show(i):
    print """Content-type: text/html\n\n
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Opinion Mining</title>

<link href="templatemo_style.css" rel="stylesheet" type="text/css" />

    
    <script src="js/jquery-1.2.1.pack.js" type="text/javascript"></script>
    <script src="js/jquery-easing.1.2.pack.js" type="text/javascript"></script>
    <script src="js/jquery-easing-compatibility.1.2.pack.js" type="text/javascript"></script>
    <script src="js/coda-slider.1.1.1.pack.js" type="text/javascript"></script>
    <!-- 
    The CSS. You can of course have this in an external .css file if you like.
    Please note that not all these styles may be necessary for your use of Coda-Slider, so feel free to take out what you don't need.
    -->
    <!-- Initialize each slider on the page. Each slider must have a unique id -->
    <script type="text/javascript">
    jQuery(window).bind("load", function() {
    jQuery("div#slider1").codaSlider()
    // jQuery("div#slider2").codaSlider()
    // etc, etc. Beware of cross-linking difficulties if using multiple sliders on one page.
    });
    </script>

</head>
<body>

<img1><img src="images/opinion.png"/></img1>

<div id="templatemo_content_wrapper">

  <div id="templatemo_content">
    
    <!-- start of slider -->

<div class="slider-wrap">
	<div id="slider1" class="csw">
<div class="panelContainer">"""
    if i==1:
        text=(file("corrected.txt").read()).split("\n")
        print """<div class="panel" title="Output">
<form action="separate.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<text>The file which you have given as input is properly processed.</text><br><br>
		<texthead>%d comments processed.</texthead><br><br><text>The ouptut is stored in <a href="corrected.txt">corrected.txt</a></text>""" % (len(text)-1,)
        print """<br><br><br><br><button><input type="Submit" value="Fact Separation"></button><br><br><br><br><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.py"><font size="5"><img src="images/arrow-left.gif">Try Another</font></a>
</form>
</div>"""
    if i==2:
        fact=(file("facts.txt").read()).split("\n")
        com=(file("comments.txt").read()).split("\n")
        print """<div class="panel" title="Output">
<form action="explicit.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>The file which you have given as input is properly processed.</texthead><br><br>
		<text>%d facts separated and stored in <a href="facts.txt">facts.txt</a></text><br><br><text>%d comments separated and stored in <a href="comments.txt">comments.txt</a></text>""" % (len(fact)-1,len(com)-1,)
        print """<br><br><br><br><button><input type="Submit" value="Explicit Feature Extraction"></button><br><br><br><br><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.py"><font size="5"><img src="images/arrow-left.gif">Try Another</font></a>
</form>
</div>"""
    if i==3:
        ex=(file("explicit.txt").read()).split("\n")
        print """<div class="panel" title="Output">
<form action="implicit.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>The file which you have given as input is properly processed.</texthead><br><br>
		<text>%d explicit comments separated and stored in <a href="explicit.txt">explicit.txt</a></text><br><br><text>The Association Database is stored in <a href="database.txt">database.txt</a></text>""" % (len(ex)-1,)
        print """<br><br><br><br><button><input type="Submit" value="Implicit Feature Identification"></button><br><br><br><br><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.py"><font size="5"><img src="images/arrow-left.gif">Try Another</font></a>
</form>
</div>"""
    if i==4:
        rank=(file("implicit.txt").read()).split("\n")
        print """<div class="panel" title="Output">
<form action="generate.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>The files which you have given as input is properly</texthead><texthead> processed.</texthead><br><br>
		<text>%d implict comments are processed and stored in <a href="implicit.txt">implicit.txt</a></text><br><br>""" % (1,)
        print """<br><br><br><br><button><input type="Submit" value="Generate Summary"></button><br><br><br><br><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.py"><font size="5"><img src="images/arrow-left.gif">Try Another</font></a>
</form>
</div>"""
    if i==5:
        print """<div class="panel" title="Output">
		<br><br><br><br>
		<texthead>The files which you have given as input is properly processed.</texthead><br><br>
		<text>The feature summary is generated in the form of:</text><br><text><a href="barchart.py">Barchart</a></text><br><text><a href="table.py">Table</a></text><br>"""
        print """<br><br><br><br><br><br><br><br><br><br>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="index.py"><font size="5"><img src="images/arrow-left.gif">Try Another</font></a>
</div>"""
    print """</div>
	</div><!-- #slider1 -->
</div><!-- .slider-wrap -->

<p id="cross-links" style="width:0px; height: 0px; font-size:0; overflow: hidden;">
	Same-page cross-link controls:<br />
	
</p>

    <!-- end of slider -->
	</div> 
	<!-- end of templatemo_content -->
</div> <!-- end of templatemo_content_wrapper -->

<div id="templatemo_footer_wrapper">

	<div id="templatemo_footer">
	    Copyright 2014 <b>PRAN Group</b>
        
	</div> <!-- end of templatemo_footer -->
</div> <!-- end of templatemo_footer_wrapper -->
</body>
</html>"""        
    
