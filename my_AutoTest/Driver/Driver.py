from selenium import webdriver

def browser():
    driver=webdriver.Chrome()
    #driver=webdriver.Firefox()
    #driver=webdriver.Ie()
    #driver.get('http://10.68.8.41:18080')
    return  driver


if __name__ == '__main__':
    browser()