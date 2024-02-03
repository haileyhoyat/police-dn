from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By
import csv
import os


url = 'https://clevelandoh.govqa.us/WEBAPP/_rs/(S(ldxq0tdwkmepsdytv2cfxdsw))/AnswerDetail.aspx?sSessionID=&aid=74904'

#set up Selenium driver to manipulate Chrome browser
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r".\files"
  })
browser = webdriver.Chrome(options=options)
browser.get(url)
html_source = browser.page_source

#download files on the webpage
#note: due to the banner element on the webpage, often the last file on the page will not get donwloaded becuase the banner is in the way

#get files from the webpage
attachment_table = browser.find_elements(By.CSS_SELECTOR, "a.dxbButton_Moderno")

#for each file on the webpage
for file in attachment_table:
    try:
        #scroll the file link into page view
        file.location_once_scrolled_into_view

        #click the file link to download the file
        #file.click()

        #get the file name, file id, and today's date
        file_name = file.find_element(By.CSS_SELECTOR, "span").text
        file_id = file.get_attribute("id")
        time_stamp = date.today().strftime("%Y%m%d")

        #create a new .csv (titled as today's date) to note down the files that are on the webpage today
        with open("documents/" + time_stamp+".csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([file_name, file_id, time_stamp])
    
    except Exception as error:
        print(error)

#check for added files since the last scrape

#for each file on the webpage
for file in attachment_table:

  #get the file name
  file_name = file.find_element(By.CSS_SELECTOR, "span").text
  
  #get the .csv file from the most previous scrape
  arr = os.listdir('documents/')[-2]
  
  #assume that the file on the webpage is a new file that was not on the webpage from the most previous scrape
  is_new_file = True

  #check if the file on the webpage is listed from the most previous scrape
  with open('documents/'+arr, newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      #if the file on the webpage is listed from the most previous scrape, 
      #the file is not a newly added file therefore is_new_file is false
      #break, and continue onto the next file on the webpage
      if file_name == row[0]:
        is_new_file = False
        break

  #if file on the webpage is not listed from the most previous scrape, the file is a newly added file
  if is_new_file:
    print(file_name)
  
browser.quit


#2023-January_DN__23-058.pdf,pnlAttachments_rptAttachments_ctl08_lnkStream,2024-02-02
#Zone__Matthew_Det__1285_Charge_Letter_9-19-22.pdf,pnlAttachments_rptAttachments_ctl279_lnkStream,2024-02-02