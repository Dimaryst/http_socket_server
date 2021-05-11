#! /usr/bin/env python3
import cgi
import html
import subprocess


# подпроцесс для вызова nmap
def process(command):
    pr = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)  # запуск команды которую передали в функцию
    op = pr.communicate()[0].decode('utf-8')  # вывод в дайтах поэтому после получения декодируем вывод nmap
    return op


form = cgi.FieldStorage()
print("Content-type: text/html\n")
print("<title>Reply Page</title>")
if not "request" in form:
    print("<h1>Error. Check you request form and try again.</h1>")
else:
    cmd = f"nmap localhost | grep \"" + html.escape(form["request"].value) + "\""
    output = process(cmd)
    print("<p>Request:</p> <code>%s</code>" % cmd)
    print("<p>Command output :</p> <code>%s</code>" % output)
