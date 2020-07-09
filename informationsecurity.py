#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi")


# In[3]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.ptt.cc/bbs/Food/index.html")

num_page = int(input("取的頁數 : "))

while num_page > 0:
    print('========新頁面=========')
    c_url = web.current_url
    web.get(c_url)
    html = web.page_source
    soup=BeautifulSoup(html,'html.parser')
    container = soup.select('.r-ent')
    for each_item in container:
        print('日期: ' + each_item.select('div.date')[0].text)
        print('作者: ' + each_item.select('div.author')[0].text)
        print('標題: ' + each_item.select('div.title')[0].text)
    
    web.find_element_by_link_text('‹ 上頁').click()
    num_page = num_page-1

web.close()


# In[9]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.informationsecurity.com.tw/article/article_list.aspx?mod=2-1")

print('========新頁面=========')
c_url = web.current_url
web.get(c_url)
html = web.page_source
soup=BeautifulSoup(html,'html.parser')
alldiv = soup.find_all('div',class_='pic_word_box')
for div in alldiv:
    print(div)
web.close()


# In[35]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.informationsecurity.com.tw/article/article_list.aspx?mod=2-1")


c_url = web.current_url
web.get(c_url)
html = web.page_source
soup=BeautifulSoup(html,'html.parser')
alldiv = soup.find_all('div',class_='pic_word_box')
for div in alldiv:
    print(' ---------一篇新聞起頭----- ')
    print('"標題"')
    print(div.find('div',class_='center_box_title').text)
    print('"連結"')
    link=div.find('a').get('href')
    newlink=link.split('..')
    finallink="https://www.informationsecurity.com.tw"+newlink[1]
    print(finallink)
    print('"內文"')
    content=div.find('div',class_='box_text').text
    newcontent=content.split('...') 
    print(newcontent[0])
    print('"日期"')
    print(newcontent[1])
    print(' ---------一篇新聞結束----- ')
web.close()


# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.informationsecurity.com.tw/article/article_list.aspx?mod=2-1")




TotalData=[]
num_page = int(input("輸入要爬取的頁數 : "))
while num_page > 0:
    c_url = web.current_url
    web.get(c_url)
    html = web.page_source
    soup=BeautifulSoup(html,'html.parser')
    alldiv = soup.find_all('div',class_='pic_word_box')
    for div in alldiv:
        print(' ---------一篇新聞起頭----- ')
       # print('"標題"')
        title=div.find('div',class_='center_box_title').text
        title=title.lstrip()
       # print('"連結"')
        link=div.find('a').get('href')
        newlink=link.split('..')
        finallink="https://www.informationsecurity.com.tw"+newlink[1]

        #print('"內文"')
        content=div.find('div',class_='box_text').text
        newcontent=content.split('...') 
        content=newcontent[0].lstrip()
       # print('"日期"')
        date=newcontent[1].strip()

        print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, finallink))
        TotalData.append({'title':title,'content':content,'date':date,'link':finallink})
        print("TotalData儲存成功")
        print(' ---------一篇新聞結束----- ')
    web.find_element_by_class_name('arrow_r_out').click()
    num_page = num_page-1
print(' ---------爬蟲結束------- ')    
web.close()


# In[2]:


import json

print(TotalData)

with open('informationsecurityman_1.json', 'w', encoding='utf-8') as f:
    json.dump(TotalData, f,ensure_ascii=False,indent=2)

##寫檔


# In[3]:


input_file = open ('informationsecurityman_1.json',encoding = 'utf8')
json_array = json.load(input_file)
print(json_array[0]['content'])
##讀檔


# In[ ]:




