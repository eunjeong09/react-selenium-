# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# # 간단예제
# def print_hi(name):
#     print(f'Hi, {name}')
# if __name__ == '__main__':
#     print_hi('PyCharm')


# 셀레늄 예제
from selenium import webdriver
driver = webdriver.Chrome('/Users/go-eunjeong/Desktop/chromedriver')
driver.implicitly_wait(2)
driver.get('http://192.168.1.4:3000')

import time

# 버튼 누르는 부분
driver.implicitly_wait(5)

for i in range(3):
    time.sleep(1)
    driver.find_element_by_id('plus').click()
for j in range(4):
    time.sleep(1)
    driver.find_element_by_id('minus').click()


driver.close()

