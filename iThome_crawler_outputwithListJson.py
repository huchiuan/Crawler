#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.ithome.com.tw/tags/資安周報")



TotalData=[]
num_page = int(input("需要爬取的頁數 : "))
print('----開始進行爬蟲----')
while num_page > 0:
    c_url = web.current_url
    web.get(c_url)
    html = web.page_source
    soup=BeautifulSoup(html,'html.parser')
    alldiv = soup.find('div',class_='view-content')
    for div in alldiv:
        print('----一篇新聞開始----')
        if 'NavigableString' in type(div).__name__:
            print('此DIV無內容')
        else:
            try:
                title=div.find('p',class_='title').text   
                try:
                    content=div.find('div',class_='summary').text.strip()
                except:
                    print('內文爬取失敗')
                try:     
                    link='https://www.ithome.com.tw/'+div.find('a').get('href')
                except:
                    print("連結爬取失敗")
                try:
                    date=div.find('p',class_='post-at').text.strip()
                except:
                     print("日期爬取失敗")
                print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, link))

                TotalData.append({'title':title,'content':content,'date':date,'link':link})
                print("TotalData儲存成功")

            except:
                print("標題擷取失敗")
           #########################################################################################     


           # print(div)

        print(' ----一篇新聞結束---- ')
    web.find_element_by_link_text('下一頁 ›').click()
    num_page = num_page-1
   
print(' ---------爬蟲結束------- ')  

web.close()


# In[6]:


import json

print(TotalData)

with open('C:\\Users\\edison-hu\\Desktop\\7月9\\Crawler-\\iThomeNews.json', 'w', encoding='utf-8') as f:
    json.dump(TotalData, f,ensure_ascii=False,indent=2)

##寫檔


# In[8]:


input_file = open ('C:\\Users\\edison-hu\\Desktop\\7月9\\Crawler-\\iThomeNews.json',encoding = 'utf8')
json_array = json.load(input_file)
print(json_array[0]['content'])
print(len(json_array[0]['content']))
##讀檔


# In[2]:





# In[ ]:




