#-*-coding:utf-8-*-
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get('http://www.attop.com/')
time.sleep(5)

driver.add_cookie({'name':'JSESSIONID','value':''})
driver.add_cookie({'name':'dang_ticket','value':''})
driver.refresh()

time.sleep(1)

driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1042')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1043')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1044')
time.sleep(1020)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1045')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1046')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1047')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1048')
time.sleep(920)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1049')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1050')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1051')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1052')
time.sleep(660)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1053')
time.sleep(480)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1054')
time.sleep(960)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1055')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1056')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1057')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1058')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1059')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1060')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1061')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1062')
time.sleep(960)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1063')
time.sleep(1080)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1064')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1065')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1066')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1067')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1068')
time.sleep(840)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1069')
time.sleep(480)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1070')
time.sleep(600)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1071')
time.sleep(420)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1072')
time.sleep(420)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1073')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1074')
time.sleep(840)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1075')
time.sleep(840)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1076')
time.sleep(900)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1077')
time.sleep(720)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1078')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1079')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1080')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1081')
time.sleep(480)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1082')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1083')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1084')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1085')
time.sleep(480)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1086')
time.sleep(300)
driver.get('http://www.attop.com/wk/learn.htm?id=42&jid=1087')
time.sleep(300)








