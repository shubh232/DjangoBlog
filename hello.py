from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
import BeautifulSoup as bs
driver = webdriver.PhantomJS("/var/lib/openshift/57717e6289f5cfe6d5000198/app-root/data/phantomjs/bin/phantomjs")
driver.set_window_size(1120,550)
driver.get('http://14.139.233.57/mmmut/studentlogin.aspx')
print(driver.title)
elem = driver.find_element_by_name("txtUserName")
elem.send_keys("shubh232@gmail.com")
elem1 = driver.find_element_by_name("txtPassword")
elem1.send_keys("sftr96rs")
elem1.send_keys(Keys.RETURN)
z = driver.page_source
c = bs.BeautifulSoup(z)
a = [t.parent for t in c.findAll(text=re.compile('^[A-Z]{3}-\d+'))]
print a
source = []
for i in a:
    j = i.nextSibling
    while j != None:
        if j.find("a") != None and j.find("a") != -1:
            so = j.find("a")['id']
        j = j.nextSibling
    el = driver.find_element_by_id(str(so))
    el.click()
    x = driver.page_source
    c1 = bs.BeautifulSoup(x).find(rules='all')
    r = c1.find('caption',text=True)
    print r
    print i
    driver.back()
    j = ''

for i in source:
    c1 = bs.BeautifulSoup(i).find(rules='all')
    print c1.find('caption')
