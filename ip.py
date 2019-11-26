import sys
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import datetime

logs_file = "D:\\logs\\logip.txt"

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("D:\\Program Files (x86)\\chromedriver.exe", options=option)
datetime_object = datetime.datetime.now()
f = open(logs_file, "a+")
f.write("\n"+"Inciado as: "+str(datetime_object)+"\n")
f.close()
while (1==1):
    try:
        f = open(logs_file, "a+")
        driver.get("http://192.168.2.1/login.cgi?username=telecomadmin&psd=Br1dg3.")
        time.sleep(1)
        driver.get("http://192.168.2.1/wanInfoGet.json")
        time.sleep(2)

        iptest = driver.execute_script("return (JSON.parse(document.documentElement.outerText)['wanInfo']['wanPppConn'][0]['ExternalIPAddress']).startsWith('100.')")
        ip = driver.execute_script("return JSON.parse(document.documentElement.outerText)['wanInfo']['wanPppConn'][0]['ExternalIPAddress']")

        datetime_object = datetime.datetime.now()
        if(iptest):
            retorno = 'IP Interno (' + ip + ') - ' + str(datetime_object)
            print (retorno)
            f.write(retorno+"\n")
            f.close()
            driver.get("http://192.168.2.1/setwanconfig.html")
            time.sleep(5)
            driver.find_element_by_id("BTN_PppoeReset").click()
            time.sleep(15)
            continue
        else:
            retorno = 'IP público (' + ip + ') - Aguardando 10 minutos antes de reiniciar - ' + str(datetime_object)
            print (retorno)
            f.write(retorno+"\n")
            f.close()
            time.sleep(600)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        continue
