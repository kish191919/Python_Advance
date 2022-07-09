import requests
from bs4 import BeautifulSoup

with open('./resources/usa_zipcode_list.txt', "r") as f:
    zipcodes = f.readlines()  # 모든 내용을 리스트로 만듦

ziplist = [zipcode.strip("\n").split("\t") for zipcode in zipcodes if zipcode != '']


zipDict = {}
for zip in ziplist:
    zipDict.setdefault(zip[-3], []).append(zip[-2:])

GA_list = zipDict['GA']
All_GA_list = []
for i in range(len(GA_list)):
    start = int(GA_list[i][0])
    end = int(GA_list[i][1]) + 1
    All_GA_list.extend(list(range(start, end)))



for zipcode in All_GA_list[:1]:
    # 세션 활성화
    session  = requests.Session()
    url = "https://www.car.com/buy-cars/{}".format(zipcode)
    request = session.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')
    print(soup.prettify())

    # 세션 비활성화
    session.close()
