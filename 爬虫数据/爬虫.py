import re
import json
import random
from time import  sleep
import requests
import  demjson
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from selenium.webdriver.common.keys import Keys
global web,wait
web=webdriver.Firefox()
web.get("https://wiki.biligame.com/ys/%E8%A7%92%E8%89%B2%E7%AD%9B%E9%80%89")
web.maximize_window()
print(web.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[5]/div/table[2]/tbody/tr[1]/td[2]/a'))
