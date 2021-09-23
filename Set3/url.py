import urllib.request

url = "https://www.w3schools.com/xml/simple.xml"
file = (urllib.request.urlopen(url)).read()
html=file.decode("UTF-8")

f=open("writing",'w')
f.write(html)

f=open("writing","r")
for line in f:
    if '<name>' in line:
        nme=(line[line.index('>')+1:])
        name=nme[: nme.index('<')]
        print(name)
    if '<price>' in line:
        prc=(line[line.index('>')+1:])
        price=prc[:prc.index('<')]
        print(price)