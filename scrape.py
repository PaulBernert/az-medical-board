from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.azmd.gov/DoctorSearch/DoctorSearch")
    
def query():
    driver.switch_to.frame(driver.find_element_by_id("Iframe1"))
    select = Select(driver.find_element_by_id('PrimaryField'))
    select.select_by_visible_text('Dermatopathology (Dermatology)')
    driver.find_element_by_id('btnSpecial').click()

def scrape():
    link_path = ['/html/body/div/div[2]/form/div[3]/table/tbody/tr[2]/td/table/tbody/tr['+str(i)+']/td[1]/a' for i in range(1,31)]
    name_path = ['/html/body/div/div[2]/form/div[3]/table/tbody/tr[2]/td/table/tbody/tr['+str(i)+']/td[2]' for i in range(1,31)]
    
    for i in range(len(link_path)):
        print(driver.find_element_by_xpath(link_path[i]).get_attribute('href'))
        print(driver.find_element_by_xpath(name_path[i]).text)
