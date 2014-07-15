#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os


def display():
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
<div class="panelContainer">
<div class="panel" title="Pre-Processing">
<form action="correction.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>Select the file which contains the comments that should</texthead> <br><texthead>be processed.</texthead><br><br><br><br><br>
		<text>Select the File: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span><input type="file" name="uploadReview" file-accept="txt" file-maxsize="10240" /></text>
		<br><br><br><br><br>
		<br>
		<button><input type="Submit" name="submit" value="Pre-Processing"/></button>
</form>
</div>
<div class="panel" title="Separate Facts">
<form action="separate.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>Select the corrected file which contains the comments that</texthead> <br><texthead>should be processed to separate the facts.</texthead><br><br><br><br><br>
		<text>Select the File: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span><input type="file" name="uploadReview" file-accept="txt" file-maxsize="10240" /></text>
		<br><br><br><br><br>
		<br>
		<button><input type="Submit" name="submit" value="Fact Separation"/></button>
</form>
</div>
<div class="panel" title="Explicit Features">
<form action="explicit.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>Select the proper file which contains the comments </texthead> <br><texthead>separated from facts that should be processed.</texthead><br><br><br><br><br>
		<text>Select the File: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span><input type="file" name="uploadReview" file-accept="txt" file-maxsize="10240" /></text>
		<br><br><br><br><br>
		<br>
		<button><input type="Submit" name="submit" value="Explicit Feature Extraction"/></button>
</form>
</div>
<div class="panel" title="Implicit Feature">
<form action="implicit.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>Select the file which contains the comments that should</texthead> <br><texthead>be ranked.</texthead><br><br><br><br><br>
		<text>Select the File: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span><input type="file" name="uploadReview" file-accept="txt" file-maxsize="10240" /></text>
		<br><br><br><br><br>
		<br>
		<button><input type="Submit" name="submit" value="Implicit Feature Extraction"/></button>
</form>
</div>
<div class="panel" title="Summary">
<form action="generate.py" method="POST" enctype="multipart/form-data" accept-charset="utf-8">
		<br><br><br><br>
		<texthead>Select the file which contains the ranked comments on the</texthead> <br><texthead>basis of which the summary is to be generated.</texthead><br><br><br><br><br>
		<text>Select the File: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span><input type="file" name="uploadReview" file-accept="txt" file-maxsize="10240" /></text>
		<br><br><br><br><br>
		<br>
		<button><input type="Submit" name="submit" value="Generate Summary"/></button>
</form>
</div>
</div>
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
    return



if __name__=='__main__':
    display()
            
    
