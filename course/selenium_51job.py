from selenium import webdriver
import xlwt

driver = webdriver.Chrome()
driver.get('https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html')
a = driver.find_elements_by_class_name('e')
#/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[7]
#/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[4]
#/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]