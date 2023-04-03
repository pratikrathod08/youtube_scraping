# import requests
from flask import Flask,render_template,request
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# !pip3 install -U selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import logging
# import pandas 
logging.basicConfig(filename="youtube_scrapper.log",level=logging.INFO)
from webdriver_manager.chrome import ChromeDriverManager

app= Flask(__name__)

@app.route("/",methods=["POST","GET"])
def homepage():
    return render_template('index.html')

@app.route('/review',methods=['POST',"GET"])
def index():
    if request.method == "POST":
        logging.info("get request successfully")
        try:
            url=request.form['content'].replace(" ","")
            driver = Chrome(executable_path=r"C:\PRATIK\APPLICATIONS\webdriver\chromedriver.exe")
            # driver = Chrome()
            # driver= Chrome(ChromeDriverManager().install())
            driver.get(url)
            # time.sleep(5)
            videos=driver.find_elements(By.CLASS_NAME,"style-scope ytd-rich-grid-media")
            # time.sleep(2)
            logging.info("connection successfull")
            list_pw=[]
            for i in range(0,5):
                url1=videos[i].find_element(By.XPATH,'.//*[@id="thumbnail"]').get_attribute('href')
                title=videos[i].find_element(By.XPATH,'.//*[@id="video-title"]').text
                view=videos[i].find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
                upload=videos[i].find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
                tb=videos[i].find_element(By.XPATH,'.//*[@id="thumbnail"]/yt-image/img').get_attribute('src')
                logging.info('data collected')
                time.sleep(1)
            #     print(url)
            #     print(title)
            #     print(view)
            #     print(upload)
            #     print(tb)
                mydict={
                    'No':i+1,
                    'Title':title,
                    'View':view,
                    'Upload':upload,
                    'Url':url1,
                    "Thumbnail":tb
                }
                list_pw.append(mydict)
                logging.info("data get into dict")
            print(list_pw)

        except Exception as e:
            logging.info(e,'there is some issue')
            print(e,"there is some issue ")
        return render_template("result.html",list_pw=list_pw)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)