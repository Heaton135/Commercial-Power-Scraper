import os
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date
import time
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()

# Getting current working directory for file download navigation
global cwd
cwd = os.getcwd()

# Setting chrome options 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {'download.default_directory' : cwd}
chrome_options.add_experimental_option('prefs', prefs)

# Pass in our custom options to chrome
driver = webdriver.Chrome(chrome_options=chrome_options)

PPLZips = []
failZips = []

def main():

    first = True
    zips = getZips()

    for x in zips['19501']:
        print("Checking:    ", x)
        checkZip(first, x)
        first = False

    df = pd.DataFrame(PPLZips)
    df.to_csv('PPL-Zip-Codes.csv')
    df2 = pd.DataFrame(failZips)
    df2.to_csv('failedzips.csv')


def getZips():
    THIS_FOLDER = Path(__file__).parent.resolve()
    my_file = THIS_FOLDER / "ZipCodes.csv"
    zips = pd.read_csv(my_file)
    zips = zips.astype(str)
    zips = zips.drop_duplicates(subset=['19501'])
    print(len(zips), " zip codes retrieved...")
    return zips

def checkZip(first, zipcode):
    url = 'https://www.papowerswitch.com/shop-for-electricity/shop-for-your-home?type=all&zip=' + str(zipcode)
    driver.get(url)
    get_source = driver.page_source
     # Handles website tutorial case
    if(first == True):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.introjs-button.introjs-skipbutton"))).click()
        except:
            pass
    # Handles multi-distributor home case

    search_text = "PPL Electric Utilities"
 
    # print True if text is present else False
    if(search_text in get_source):
        print(zipcode, ":   TRUE")
        PPLZips.append(zipcode)
    else:
        print(zipcode, ":   FALSE")
        failZips.append(zipcode)
    # try:
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-id='27513']"))).click()
    #     PPLZips.append(zipcode)
    #     print("Added: ", zipcode)
    # except:
    #     pass


main()