from selenium import webdriver

#def test_scores_service():
driver = webdriver.Chrome(executable_path="C:\ChromeDriver")
webpage = driver.get("http://127.0.0.1:5000/score")
score = driver.find_element_by_xpath("//div[@id='score']")
print(score)







#test_scores_service()
#    driver.refresh()
#    website_title_second_run = driver.title
#if website_title_first_run == website_title_second_run:
#    print("the page title is the same")
#else:
#    print("the page title is diffrent")
#score = driver.find_elements_by_id("//div[@id='score']")

#id="score"