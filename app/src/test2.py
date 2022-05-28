import os
import datetime
import time
import schedule

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)


# Y!トピックからランキングtop10を取ってくる
def job():
    print(f'ジョブ開始日時：{datetime.datetime.now().strftime("%Y年%m月%d日%H:%M:%S")}')
    driver.get('https://news.yahoo.co.jp/topics')
    driver.implicitly_wait(0.5)
    yjnSub_list_item = []
    yjnSub_section_title = ""
    try:
        yjnSub_section = driver.find_element(by=By.CLASS_NAME, value="yjnSub_section")
        yjnSub_section_title = yjnSub_section.find_element(by=By.CLASS_NAME, value='yjnSub_section_title').text
        yjnSub_list_item = yjnSub_section.find_elements(by=By.CLASS_NAME, value='yjnSub_list_item')
    except NoSuchElementException as e:
        print("そんな要素ないぞ")
        print(e)
    print(yjnSub_section_title)
    for item in yjnSub_list_item:
        rank = item.find_element(by=By.CLASS_NAME, value="yjnSub_list_rankNum").text
        headline = item.find_element(by=By.CLASS_NAME, value="yjnSub_list_headline").text
        link = item.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
        print(f'{rank} ヘッドライン：{headline}')
        print(link)
    print(f'ジョブ終了日時：{datetime.datetime.now().strftime("%Y年%m月%d日%H:%M:%S")}')


job()

# schedule.every(10).minutes.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
