# import bs4
# import requests
#
# website_link = requests.get("http://onlinetutorial.co.in")
# ab = bs4.BeautifulSoup(website_link.text,'lxml')
# heading2= ab.select("h2")
# print(heading2)

# #To return whole elements i.e. tag with text
# for i in heading2:
#     print(i)
#
# #To return Text only
# for i in heading2:
#     print(i.text)

website_link = requests.get("http://onlinetutorial.co.in")
ab = bs4.BeautifulSoup(website_link.text,'lxml')
heading2= ab.select(".widget_categories")
for i in heading2:
    print(i.text)
