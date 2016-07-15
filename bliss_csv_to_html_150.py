"""
based on csv2html.py and other scripts from Rosettacode

"""

# Tweak to make the script work with both python 2 and 3:
from __future__ import print_function


from cgi import escape
import urllib

import sys

#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
#<!DOCTYPE HTML>
#<!doctype html>
print( '''<html>
  <head>
    <meta charset="UTF-8">
    <title>Bliss</title>
  </head>
  <body>
''')

#csvtxt = open("tsv").read()
csvtxt = sys.stdin.read()
 
def _row2tr(row, attr=None):
    cols = escape(row).split('\t')
    raawcols = row.split('\t')
    #
    #src1="bliss_h_transp_png/%s.png" %   urllib.quote(raawcols[1])
    src1="bliss_w100h78_transp_png/%s.png" %   urllib.quote(raawcols[1])
    #
    #imgsrc1 = '<img src="%s">' % src1
    imgsrc1 = '<img src="%s"  width="100" height="78"   >' % src1
    #
    return ('<tr>'
            + ''.join('<td>%s</td>' % data for data in cols)
            + '<td>%s</td>' % imgsrc1
            + '</tr>')
 
def csv2html(txt):
    htmltxt = '<table summary="csv2html program output">\n'
    for rownum, row in enumerate(txt.split('\n')):
        if row <> '':
          htmlrow = _row2tr(row)
          htmlrow = '  %s\n' % htmlrow
          htmltxt += htmlrow
    htmltxt += '</table>\n'
    return htmltxt
 
htmltxt = csv2html(csvtxt)
print(htmltxt)
   
print( '''
  </body>
</html>
''')
