from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# https://github.com/usernam121

driver = webdriver.Chrome()
driver.get("https://github.com/usernam121")
repo = "https://github.com/usernam121"
# time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "repo")
# time.sleep(2)
# price = driver.find_element(By.CLASS_NAME, "reinventPricePriceToPayMargin")
links = []
flink = []


def going_for_raw(second_page):
    driver.get(second_page)
    time.sleep(2)
    # Target Raw button by link text so auto-generated CSS classes don't break it
    raw = driver.find_element(By.LINK_TEXT, "Raw")
    raw.click()
    time.sleep(1)
    html = driver.page_source
    if "password" in html:
        print(f"Password found {second_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
    for a in res2:
        pass
        # print(a.text)
    if "py" in a.text:
        second_page = f"{repo}/respository/blob/main/{a.text}"
        going_for_raw(second_page)
        # print(second_page)


for i in res:
    links.append(i.text)
# print(links)
for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)
# print(flink)



driver.quit()
