# 引入selenium
# 引入chromedriver
# 引入Select用于选择
# 引入time对频率进行控制
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

# 打开Chrome
chrome = Chrome()
# 打开教务系统
chrome.get("http://jwxt.buaa.edu.cn:7001/ieas2.1/welcome?falg=1")

# 通过xpath定位iframe元素
iframe = chrome.find_element_by_xpath("/html/body/iframe")
# 使得chrome对象聚焦于iframe
chrome.switch_to.frame(iframe)
# 定位用户名并输入用户名，用send_keys函数来输入
chrome.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/input").send_keys("123456")
# 密码
chrome.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/input').send_keys("******")

# 点击登录
chrome.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div[1]/div[7]/input").click()

# 点击学生选课
chrome.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/a[6]/div").click()
# sleep是为了等待网页动画
time.sleep(0.5)
# 点击专业课程
chrome.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[6]/div/a[4]/span[2]").click()

# 通过xpath定位iframe元素
iframe = chrome.find_element_by_xpath("/html/body/div[4]/div[1]/iframe")
# 使得chrome对象聚焦于iframe，注意，switch_to后chrome将持续处于此iframe中，因此不需要多次使用switch_to
chrome.switch_to.frame(iframe)
# 点击一般专业类
chrome.find_element_by_xpath("/html/body/div[7]/div/div[3]/table/tbody/tr/td[1]/ul/li[2]/a").click()

# 定位选择框元素的位置
select = chrome.find_element_by_xpath("/html/body/div[7]/div/div[4]/form/ul/li[3]/select")
# 通过select tag构造一个Select对象s
s = Select(select)
# 用option tag中的value实现选择，此处选择06，即计算机学院
s.select_by_value("06")

flag = True
while flag:
    # 点击查询按钮
    chrome.find_element_by_xpath("/html/body/div[7]/div/div[4]/form/ul/li[6]/div/a/span").click()
    # 找到人数，numbers = '57/80 对外:0/2'，字符串类型
    numbers = chrome.find_element_by_xpath("/html/body/div[7]/div/div[6]/table/tbody/tr[2]/td[15]").text
    # 对字符串找到对外剩余人数，number = 0
    number = int(numbers.split(sep=':')[1].split(sep='/')[0])
    if number > 0:
        # 点击选课按钮
        chrome.find_element_by_xpath("/html/body/div[7]/div/div[6]/table/tbody/tr[2]/td[1]/div/a/span").click()
        flag = False
        print("Got it")
