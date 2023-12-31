# Commercial-Power-Scraper

## There are three Programs in this repository:

## 1. Commercial-Small-Scraper.py

This program downloads power provider offers from the nine default power distributors in Pennsylvania for small commercial businesses.

The nine default providers are listed below, along with the associated zipcode we are retreiving for each:
1. Duquesne Light : 15106, 
2. Met-Ed : 17325, 
3. PECO : 19109, 
4. Penelec : 16619, 
5. PennPower : 15086, 
6. PPL : 18015,
7. Pike-County-LP : 18324, 
8. UGI : 18622, 
9. WestPenn : 15020


### Instructions:
Navigate to this directory and run ```python3 Commercial-Small-Scraper.py``` in terminal

## 2. GS1-Scraper.py:

This program downloads electricity rates for PPL's Small General Service - Secondary Voltage Service in their service territory. papowerswitch.com is scraped for power rates using the zip codes in '''PPL-Zip-Codes.csv'''

### Instructions:
Navigate to this directory and run ```python3 GS1-Scraper.py``` in terminal

Note: If errors are experienced during the code execution, you may need to update the PPL-Zip-Code list. .

## 3. GS3-Scraper.py
This program downloads electricity rates for PPL's Large General Service - Secondary Voltage in their service territory. papowerswitch.com is scraped for power rates using the zip codes in '''PPL-Zip-Codes.csv'''

### Instructions:
Navigate to this directory and run ```python3 GS3-Scraper.py``` in terminal

Note: If errors are experienced during the code execution, you may need to update the PPL-Zip-Code list. 

## About:
3 functions are included in these program:
1. Main function that serves as the driver, exports results as a csv at the end
2. getRates(): contains our selenium portion of the code. This function takes a zipcode, navigates to papowerswitch.com and downloads the resulting csv file
3. importResults(): processes the downloaded results file from the getRates() function, adds a date, zipcode, and provider column, and then appends the resulting data to the full data of all zip codes for that day

## Contacts:
[Alberto Lamadrid, Ph.D.](https://business.lehigh.edu/directory/alberto-j-lamadrid) ,  Lehigh University, Economics, Associate Professor

[Henry Eaton](hhe223@lehigh.edu), Student, Lehigh University

### References:
[Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)

[Link to updated list of zip codes in PPL Electric Region](https://www.pplelectric.com/-/media/PPLElectric/At-Your-Service/Docs/General-Supplier-Reference-Information/PPLServicingArea-Zipcodes.xls)
