#!/usr/bin/python3
import cgi
# HTML is following  
print("Content-Type: text/html")     
# blank line, end of headers  
print()   
print("<title> This is a CGI script output</title>")  
print("<h1>This is my first CGI script</h1>")  
print("Hello, JavaTpoint!<br>")  
link = cgi.FieldStorage()
NU1 = int(link["number1"].value)
NU2 = int(link["number2"].value)
SUM = NU1 + NU2
print("Result= %i" % ( SUM ))
