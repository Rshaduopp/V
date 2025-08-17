from telethon import TelegramClient,utils
import requests
import json
from bs4 import BeautifulSoup
import html5lib

import csv
phones=[]
api_id=""
hash_id=""
with open('phone.csv') as phonefile:
    csv_reader=csv.reader(phonefile)
    for row in csv_reader:
        phones.append(row[0].strip())
def api_hash(phone):
    print(phone)
    url_send_password="https://my.telegram.org/auth/send_password"
    para={
        "phone":phone
        }
    try:
        result=requests.post(url=url_send_password,data=para).json()
    except Exception as e:
    	print(" retries") 
    else:
        url_login="https://my.telegram.org/auth/login"
        password=input('Enter login code :-')
        data={
            "phone":para['phone'],
            "random_hash":result['random_hash'],
            "password":password
            }
        try:
            result2=requests.post(url=url_login,data=data)
        except Exception as e:
            print(e)
           

        url3="https://my.telegram.org/apps/create"
        url4="https://my.telegram.org/apps"
        cookies=result2.cookies
        try:
            result4=requests.get(url=url4,cookies=cookies)
        except Exception as e:
            print(e)
        else:
            try:
                soup=BeautifulSoup(result4.content ,'html5lib')
                soup.prettify() 
            except Exception as e:
                print(e)
            else:
                try:
                    element=soup.find('input' ,attrs={'name':'hash'})
                except Exception as e:
                    print(e)
                else:
                    if not element:
                        raise Exception("too many retries")
                    data3={
                        "hash":element.get('value'),
                        "app_title": "hduwsjq",
                        "app_shortname":"djwidj",
                        "app_url":"my.telegram.org",
                        "app_platform":'android',
                        "app_desc":""
                        }
                    try:
                        result3=requests.post(url=url3,data=data3,cookies=cookies)
                    except Exception as e:
                        print(e)
                    else:
                        try:
                            result5=requests.get(url=url4,cookies=cookies)

                            soup2=BeautifulSoup(result5.content ,'html5lib')
                            #print(soup2.prettify()) 
                        except Exception as e:
                            print(e)
                        else:
                            try:
                                elements=soup2.find_all('div',attrs={'class':'col-md-7'})
                            except Exception as e:
                                print(e)
                            else:  
                                try:
                                    api_id1=elements[0].findChildren('span',recursive=False)[0].findChildren('strong',recursive=False)[0].get_text()
                                    hash_id1=elements[1].findChildren('span',recursive=False)[0].text
                                except Exception as e:
                                    print(e)
                                else:
                                    print(api_id1)
                                    print(hash_id1)
                                    return {"api_id":api_id1 ,"api_hash":hash_id1}
def makeapirishabh():
    results=[]
    for phone in phones:
        print(phone)
        try:
            result=api_hash(phone=phone)
        except Exception as e:
            print(e)
        else:
            results.append(result)
    with open('api.csv','a') as t:
        write1=csv.writer(t,lineterminator='\n',delimiter=',')
        for result in results:
        	if result:
        	    write1.writerow([result['api_id'],result['api_hash']])
         
        t.close()
#write()