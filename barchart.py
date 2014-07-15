#!E:/Installed Setup/Python/python

import cgi, os
import cgitb; cgitb.enable()
import os


if __name__=="__main__":
    print """Content-type: text/html\n\n
            <html>
<head>
  <script type="text/javascript">
  window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: "Product Feature Summary(Scoring)"
      },
      data: [
      {
        type: "bar",
        dataPoints: ["""
    text=str(file('ranked.txt').read()).split('\n')
    for i in range(len(text)-1):
        temp=str(text[i]).split('=')
        v=float(temp[1])
        print "{y:%d,label:'%s'}," % (v,str(temp[0]),)
    print """]
      }
]
    });

chart.render();
}
</script>
<script type="text/javascript" src="canvasjs.min.js"></script></head>
<body>
  <div id="chartContainer" style="height: 300px; width: 100%;">
  </div>
</body>
</html>"""
