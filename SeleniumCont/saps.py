from selenium import webdriver
from selenium.webdriver.chrome import service

CHROMEDRIVER = r"C:\Users\jyun4\OneDrive\ドキュメント\GitHub\Selenium_Scraping\SeleniumCont\chromedriver.exe"

chrome_service = service.Service(executable_path=CHROMEDRIVER)
driver= webdriver.Chrome(service=chrome_service)


driver.get("https://gamewith.jp/pokemon-bdsp/article/show/307435")

link_text = "https://img.gamewith.jp/article_tools/"

element = driver.find_element_by_partial_link_text(link_text)

print(element)
