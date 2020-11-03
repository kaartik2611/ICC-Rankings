from selenium import webdriver
from selenium.webdriver import ActionChains
from tabulate import tabulate
import time


# path of web-driver for google chrome.
driver = webdriver.Chrome(executable_path="C://Users//acer//Documents//chromedriver_v86//chromedriver.exe")

# site to be scrapped.
driver.get('https://www.espncricinfo.com/rankings/content/page/211271.html')

time.sleep(0.5)

print("ICC rankings for Tests, ODIs, T20 & Women's ODI and T20")

# creating an array for storing scrapped data.
tableData = []

# looping through the table rows and appending the scrapped data in the list.
for i in range(1,6):
    rankings = []
    title = ["----------------ICC MEN'S TEST RANKINGS----------------","----------------ICC MEN'S ODI RANKINGS----------------","----------------ICC MEN'S T-20 RANKINGS----------------","----------------ICC WOMEN'S ODI RANKINGS----------------","----------------ICC WOMEN'S T-20 RANKINGS----------------"]
    for x in range(2, 12):
        for y in range(1, 6):
            # path in form of x-path of desired content to get scrapped
            path_text = f'//html/body/div[4]/div/div/div[3]/div/table[{i}]/tbody/tr[{x}]/td[{y}]'
            sel_text = driver.find_element_by_xpath(path_text)
            data_ls = ((sel_text.text).splitlines())
            data_str = ""
            data_str = data_str.join(data_ls)

            tableData.append(data_str)
        rankings.append(tableData)
        tableData = []
    print()
    print(title[i-1])
    print()
    print(tabulate(rankings,headers=['Rank',"country-name","matches","points","rating"],tablefmt="pretty"))

# closing the tab.
driver.close()
