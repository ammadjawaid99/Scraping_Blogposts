"""
@author: Ammad
"""

location = r'store the chromedriver.exe in the same folder where the script is and give here the location'
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import feedparser
import os
import string
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
    
link1 = 'https://www.zdnet.com/news/rss.xml'

# zdnet.com posts
# =============================================================================
# # Using feedparser to get all the blogs links
# =============================================================================

rssFeed = feedparser.parse(link1)
posts = rssFeed.entries

zdnetPosts = dict()

postList = []

for post in posts:
    details = dict()
    
    try:
        details["title"] = post.title
        details["link"] = post.link
    except:
        pass
      
    postList.append(details)

zdnetPosts["posts"] = postList

print('The total number of blogposts in the zdnet website are:', len(zdnetPosts['posts']))
# =============================================================================
# # Extracting the blog content
# =============================================================================
for index, blogs in enumerate(zdnetPosts['posts']):
    
    time.sleep(10)
    
    title, link = blogs.values()
    
    # Remove punctuation from title
    title = title.translate(str.maketrans('', '', string.punctuation))
    
    driver = webdriver.Chrome(location + '//chromedriver.exe', chrome_options=chrome_options)

    driver.get(link)


    
    outputFolder = location + '\\blogs\\zdnet'
    
    try:
        content = (driver.find_element_by_xpath("//*[starts-with(@id, 'article-')]").text).replace('\n', '\n\n')

        isExist = os.path.exists(outputFolder)
        if not isExist:
            os.makedirs(outputFolder)
        
        textFile = open(outputFolder + '\\' + title + '.txt', 'w+')
        textFile.write(content)
        textFile.close()
    
    except:
        pass
    
    driver.quit()
    
    print(index + 1)



# =============================================================================
# =============================================================================
# # 
# =============================================================================
# =============================================================================



# # gadgets360.com posts
# =============================================================================
# # Using feedparser to get all the blogs links
# =============================================================================

link2 = 'https://gadgets360.com/rss/feeds'

rssFeed = feedparser.parse(link2)
posts = rssFeed.entries

g360Posts = dict()

postList = []

for post in posts:
    details = dict()
    
    try:
        details["title"] = post.title
        details["link"] = post.link
    except:
        pass
      
    postList.append(details)

g360Posts["posts"] = postList

print('The total number of blogposts in the zdnet website are:', len(g360Posts['posts']))

# =============================================================================
# # Extracting the blog content
# =============================================================================
for index, blogs in enumerate(g360Posts['posts']):
    time.sleep(10)
    
    title, link = blogs.values()
    
    # Remove punctuation from title
    title = title.translate(str.maketrans('', '', string.punctuation))
    
    driver = webdriver.Chrome(location + '//chromedriver.exe', chrome_options=chrome_options)

    driver.get(link)
    
    outputFolder = location + '\\blogs\\gadgets360'
    
    try:
        content = (driver.find_element_by_xpath("//*[starts-with(@class, 'content_text row description')]").text).replace('\n', '\n\n')
        
        isExist = os.path.exists(outputFolder)
        if not isExist:
            os.makedirs(outputFolder)
        
        textFile = open(outputFolder + '\\' + title + '.txt', 'w+')
        textFile.write(content)
        textFile.close()
    
    except:
        pass
    
    driver.quit()

    print(index + 1)
    
