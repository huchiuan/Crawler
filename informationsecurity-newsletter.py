#!/usr/bin/env python
# coding: utf-8

# In[42]:


from selenium import webdriver
from bs4 import BeautifulSoup
chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.informationsecurity.com.tw/e-newsletter/")
TotalData=[]

for element in web.find_elements_by_xpath("//div[@class='newsletter_contect']/ul/li/a"):
    now_handle = web.current_window_handle
  #  print (now_handle)視窗控制代碼 
    print(' ---------一篇新聞開始----- ')
    href=element.get_attribute('href')
    text =element.get_attribute('text')
    if '資安人週報' in text:
       # print(href)
        #print(text) 
        web.find_element_by_partial_link_text(text).click()
        all_handles = web.window_handles 
        for handle in all_handles:  
            if handle!=now_handle:     
                #輸出待選擇的視窗控制代碼  
                # print( handle ) 
                web.switch_to_window(handle)  
                  

                
                numberspan= web.find_element_by_id('Li_eid')
                number=numberspan.text.strip()  #text is a property of the WebElement class, thus it is not callable.
                #print('新介面數字:',number)
                
                datespan= web.find_element_by_id('li_date')
                date=datespan.text.strip()  #text is a property of the WebElement class, thus it is not callable.
               # print('新介面日期:',date)
                
                contentp= web.find_element_by_xpath("//p[@class='title_c']/a")
                content=contentp.text.strip()  #text is a property of the WebElement class, thus it is not callable.
               # print('內文:',content)
                
                newtitle="資安人電子報(No.{}期) - ({})".format(number,date)
               # print(newtitle)
                
                print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(newtitle, content,date, href))
                TotalData.append({'title':newtitle,'content':content,'date':date,'link':href})
                print("TotalData儲存成功")
                web.close()  
              
              #輸出主視窗控制代碼  
      #  print( now_handle  )
        web.switch_to_window(now_handle) #返回主視窗 開始下一個跳轉    
    else: 
        break
# for div in alldiv:
#     print(' ---------一篇新聞起頭----- ')
#    # print('"標題"')
#     title=div.find('div',class_='center_box_title').text
#     title=title.lstrip()
#     web.find_element_by_link_text('下一頁 ›').click()
    
#    # print('"連結"')
#     link=div.find('a').get('href')
#     newlink=link.split('..')
#     finallink="https://www.informationsecurity.com.tw"+newlink[1]

#     #print('"內文"')
#     content=div.find('div',class_='box_text').text
#     newcontent=content.split('...') 
#     content=newcontent[0].lstrip()
#    # print('"日期"')
#     date=newcontent[1].strip()

#     print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, finallink))
#     TotalData.append({'title':title,'content':content,'date':date,'link':finallink})
#     print("TotalData儲存成功")
    print(' ---------一篇新聞結束----- ')

print(' ---------爬蟲結束------- ')    
web.close()


# In[43]:


import json

print(TotalData)

with open('C:\\Users\\edison-hu\\Desktop\\7月9\\Crawler-\\informationsecurityman_newsletter.json', 'w', encoding='utf-8') as f:
    json.dump(TotalData, f,ensure_ascii=False,indent=2)

##寫檔


# In[44]:


input_file = open ('C:\\Users\\edison-hu\\Desktop\\7月9\\Crawler-\\informationsecurityman_newsletter.json',encoding = 'utf8')
json_array = json.load(input_file)
print(json_array[0]['content'])
##讀檔


# In[ ]:




