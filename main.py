import  requests
from bs4 import BeautifulSoup


# url = 'https://www.autoevolution.com/cars/'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
# }
# req = requests.get(url, headers=headers)
#
# src = req.text
# print(src)

# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_div_class = soup.find_all(class_='carman')
minus = False
for i in all_div_class:
    # print(i.contents[0])
    t = BeautifulSoup(str(i.contents[0]), 'lxml')
    print(t.a['title'])
    title = t.a['title']
    minus = len(title) + 1
    # print(t.a['href'])
    # url = str(t.a['href'])
    #
    # headers = {
    #     'Accept': '*/*',
    #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
    # }
    # req = requests.get(url, headers=headers)
    #
    # src = req.text
    # print(src)
    #
    # with open('index_1.html', 'w') as file:
    #     file.write(src)
    break

with open('index_1.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_div_class = soup.find_all(class_='bcol-white')
# print(all_div_class)

for i in all_div_class:
    # print(i)
    # print(i.contents[1].contents[1].text)
    model = i.contents[1].contents[1].text
    print(model[minus:])
    # t = BeautifulSoup(str(i.contents[0]), 'lxml')
    # print(t)
    # print(t.a['href'])
    # break