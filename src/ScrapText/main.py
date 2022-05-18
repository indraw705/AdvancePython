from selenium import webdriver
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("start-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver


if __name__ == "__main__":
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]").text
    time.sleep(2)
    temprature = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    print(element)
    print(int((temprature.split(": "))[1]))
    driver.close()
