from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


my_url='https://realpython.github.io/fake-jobs/'

cont=ureq(my_url)
page_html=cont.read()
# print(page_html)
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"column is-half"})
# print(len(containers))
# print(soup.prettify(containers[0]))

container=containers[0]
#To print image in container
# print(container.div.img['src'])

# To print position
# print(container.div.h2.text)

#company details
# print(container.div.h3.text)

# Location
# print(container.div.p.text)

# print(container.div.time.text)


f=open("job_details","w")
header="Job details:Position,Company,Location and Date"
f.write(header)


for item in containers:
    logo = item.div.img['src']
    position = item.div.h2.text
    company = item.div.h3.text
    location = item.div.p.text.strip()
    date = item.div.time.text

    # print("Logo : ",logo)
    # print("Position : ",position)
    # print("Company :",company)
    # print("Location :",location)
    # print("Date :",date)

    f.write("\nLogo : "+ logo)
    f.write("\nPosition : "+position)
    f.write("\nCompany :"+company)
    f.write("\nLocation :"+location)
    f.write("\nDate :"+date)
    f.write("\n")