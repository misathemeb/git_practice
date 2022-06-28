
from bs4 import BeautifulSoup
import os, re, csv, time
from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#instantiate driver object & assign URL for medals page
driver = webdriver.Safari()
driver.get('http://www.olympedia.org/statistics/medal/country')

#utilize .find elem by id method to find year and athlete gender
year_dd = driver.find_element(By.ID, 'edition_select')
gender_dd = driver.find_element(By.ID, 'athlete_gender')

#next collect options for dropdown menu using .find elem by tag method
year_options = year_dd.find_element(By.TAG_NAME, 'option')
gender_options = gender_dd.find_element(By.TAG_NAME, 'option')

year_element = driver.find_element(By.XPATH, "//select[option/@value ='1']")
print(year_element)  

print(year_element.get_attribute('text'))  

        
usa_list = []

#use nested loops to traverse the groups of athletes and then years for every summer games series.
for gender in gender_options[1:]:
    gender.click()
    time.sleep(2)
    gender_val = gender.get_attribute('text')
    
    for year in year_options[1:]:
        year.click()
        time.sleep(1)
        
        
#create a soup object and parse the content
    soup = BeautifulSoup(driver.page_source, 'html.parser')


#organize data & parse the source
    try:
        year_val = year.get_attribute('text')
        head = soup.find(href=re.compile('USA'))     
        head.find_all_next('td', limit=5)

        medal_values = head.find_all_next('td',limit=5)
        val_lst = [x.string for x in medal_values[-4:]]
        
    except:
        val_lst = ['0' for x in range(4)]

    val_lst.append(gender_val)
    val_lst.append(year_val)

    usa_list.append(val_lst)

    if year_val == '2020':
        break

driver.quit()

print(usa_list[30])
print(usa_list[31])


try:
    output_f = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output_f)
    for row in usa_list:
        output_writer.writerow(row)

except:
    pass
finally:
    output_f.close()
    print('done')