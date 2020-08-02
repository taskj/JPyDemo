from selenium import webdriver
import time
import csv


wd = webdriver.Chrome()

wd.get("https://jd.com")

wd.find_element_by_xpath('//*[@id="key"]').send_keys("Python")
wd.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

#模拟下拉
wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#获取页面中的源代码
html = wd.page_source

#初始化csv表头
with open('京东商品信息.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['名称','价格','商铺名'])

    for i in range(0,10):
        time.sleep(2)
        # 获取商品列表
        li_list = wd.find_elements_by_xpath('//*[@id="J_goodsList"]//ul/li')
        for li in li_list:
            goods_price = li.find_element_by_class_name("p-price").find_element_by_tag_name("i").text
            goods_name = li.find_element_by_class_name("p-name").find_element_by_tag_name("em").text
            shop = li.find_element_by_class_name("p-shopnum").text
            writer.writerow([goods_name,goods_price,shop])
        wd.find_element_by_class_name("pn-next").click()

time.sleep(2)
wd.quit()
