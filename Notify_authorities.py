import paho.mqtt.client as mqtt
import os
import pyperclip
import io
import re
import json
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import datetime 


dict = {}
with open('m.json') as json_file:
	data = json.load(json_file)
	for p in data['whatsappMqtt']:
		print(p["MQTT"])
		print(p["CONTACT"])
		dict[p["MQTT"]]="'"+p["CONTACT"]+"'"  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('/home/vik/Downloads/chromedriver') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
def on_connect(client,userdata,flags,rc):
     if rc==0:
       print("connected ok")
     else:
       print("Bad connection return = ",rc)
def on_message(client,userdata,msg):        
        topic=msg.topic
        print topic
        target=dict[topic]
        print target
        m_decode=str(msg.payload.decode("utf-8"))
        print("message recieved",m_decode)

        string= m_decode
      #  x_arg = '//span[contains(@title,' + target + ')]'
      #  group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
      #  group_title.click() 
      #  inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
      #  input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
        x_arg  =  '//span[contains(@title,' + target +  ')]'
        #print x_arg
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
        group_title.click() 
        inp_xpath = "//div[@contenteditable='true']"
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
        input_box.send_keys(target+string +str(datetime.datetime.now())+Keys.ENTER) 




broker = "broker.hivemq.com"
port = 1883
client = mqtt.Client("python1")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port)
print("connecting to broker")
client.loop_start()


#dict["hacklab/A1"]='"Hacklab Solutions"'
#dict["hacklab/A2"]='"Vikramsir(H)"'
#dict["hacklab/A3"]='"Pavan Sir"'
for key in dict.keys():
    print key
    print('Subscribed',key)
    client.subscribe(key)


  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group 
target = ""


# Replace the below string with your own message 
	
#string = "hi"
while 1: 	
        time.sleep(60)
