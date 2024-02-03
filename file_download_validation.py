from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import shutil


url = 'https://clevelandoh.govqa.us/WEBAPP/_rs/(S(ldxq0tdwkmepsdytv2cfxdsw))/AnswerDetail.aspx?sSessionID=&aid=74904'

files = []
file_names = []
DN = []
file_count = 0

#set up Selenium driver to manipulate Chrome browser
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r".\files"
  })
browser = webdriver.Chrome(options=options)
browser.get(url)
html_source = browser.page_source


#get a list of the files names on the webpage
files = browser.find_elements(By.CSS_SELECTOR, "a.dxbButton_Moderno span")

for i in files:
    #print(i.get_attribute("innerHTML"))
    file_names.append(i.get_attribute("innerHTML"))

#compare the files on the webpage vs the files that were downloaded.

#get the files from new_files folder
list = os.listdir('./new_files')

#sometimes a folder will have the .DS_Store file in it. 
#this file is a file used by the MacOS Finder tool 
#remove this file from list[]
for i in list:
    if i == '.DS_Store':
        list.remove('.DS_Store')

#sort the file_names[] and list[] so all files are in alphabetical order
file_names.sort()
list.sort()

#compare the files in file_names[] and list[] to see differences in the files on the webpage vs the files that were downloaded 
#first, check that the number of files on the webpage is the same number of files that were downloaded

if len(file_names) != len(list):
    print("Not all files were downloaded")
    print("files_names count: " + str(len(file_names)))
    print("list count: " + str(len(list)))  

#from file_names[], check if that file is in list[]
for i in file_names:
    if i in list:
        continue
    else:
        print("missing file: " + i)
        


#print(file_names)
#print(list)