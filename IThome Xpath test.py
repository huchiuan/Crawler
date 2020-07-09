#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.ithome.com.tw/tags/資安周報")



TotalData=[]

print('----開始進行爬蟲----')

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
#         try:
#             title=div.find('p',class_='title').text   
#             try:
#                 content=div.find('div',class_='summary').text.strip()
#             except:
#                 print('內文爬取失敗')
#             try:     
#                 link='https://www.ithome.com.tw/'+div.find('a').get('href')
#             except:
#                 print("連結爬取失敗")
#             try:
#                 date=div.find('p',class_='post-at').text.strip()
#             except:
#                  print("日期爬取失敗")
#             print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, link))

#             TotalData.append({'title':title,'content':content,'date':date,'link':link})
#             print("TotalData儲存成功")

#         except:
#             print("標題擷取失敗")
        content = div.find_element_by_xpath("//div[1]")
        print(div)
       #########################################################################################     


       # print(div)

    print(' ----一篇新聞結束---- ')

   
print(' ---------爬蟲結束------- ')  

web.close()


# In[81]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.ithome.com.tw/tags/資安周報")



TotalData=[]

print('----開始進行爬蟲----')

c_url = web.current_url
web.get(c_url)
html = web.page_source
soup=BeautifulSoup(html,'html.parser')
alldiv = soup.find('div',class_='view-content')



for element in web.find_elements_by_xpath("//div[@class='view-content']//div[@class='item']//p[@class='title']/a"):   

    try:

        href=element.get_attribute('href')
        print(href)
        text =element.get_attribute('text')
        print(text)                                      
        
    except OSError:
            print('發生OSError!')
            print(pos)
            break;
       #########################################################################################     


       # print(div)

   

   
print(' ---------爬蟲結束------- ')  

web.close()


# In[ ]:





# In[ ]:





# In[ ]:




